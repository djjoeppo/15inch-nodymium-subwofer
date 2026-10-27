#!/usr/bin/env python3
"""
Parametrische CAD Generator voor 100mm P2P TPU Surround Segment & Proef-Print Slice.
Ondersteunt zowel standalone CadQuery (Python) als native FreeCAD Macro Execution (`import Part`).

Genereert:
1. Volledig 60° Surround Segment (STEP & STL)
2. 15-Minuten TPU Proef-Print Slice (20mm boog, ~3g TPU) voor risicoloos testen van laaghechtingssterkte en flexibiliteit.
"""

import math

def calculate_surround_profile_points(cone_radius=157.5, radial_width=35.0, roll_height=25.0,
                                      wall_thickness=0.9, flange_width=10.0, num_steps=30):
    """
    Berekent de buitengrens- en binnengrenspunten van de High-Roll TPU surround met
    loodrechte normaalvectoren voor een gegarandeerde 0.9mm wanddikte en
    zonder zelf-intersecties op de flens-overgangen.
    """
    r_in = cone_radius - flange_width
    r_cone = cone_radius
    r_basket = cone_radius + radial_width
    r_out = r_basket + flange_width
    a = radial_width / 2.0  # 17.5 mm
    b = roll_height         # 25.0 mm

    outer_pts = []
    inner_pts = []

    # 1. Buitenprofiel (Binnenflens -> Semi-Ellips Boog -> Buitenflens) op Z >= 0
    outer_pts.append((r_in, 0.0))
    outer_pts.append((r_cone, 0.0))

    for i in range(0, num_steps + 1):
        t = math.pi * (i / num_steps)
        r_outer = r_cone + a * (1.0 - math.cos(t))
        z_outer = b * math.sin(t)
        if i > 0 and i < num_steps:
            outer_pts.append((r_outer, z_outer))

        # Raaklijn vector (dr/dt, dz/dt) = (a*sin(t), b*cos(t))
        dr = a * math.sin(t)
        dz = b * math.cos(t)
        length = math.sqrt(dr*dr + dz*dz)

        # Inwaartse loodrechte normaal vector (n_r, n_z)
        n_r = -dz / length
        n_z = dr / length

        # Inwaartse offset met clamping van Z op minstens -wall_thickness
        r_inner = r_outer + wall_thickness * n_r
        z_inner = z_outer + wall_thickness * n_z
        if z_inner < -wall_thickness:
            z_inner = -wall_thickness

        # Klem R binnen de flensgrenzen om kruisingen te voorkomen
        if r_inner < r_cone:
            r_inner = r_cone
        if r_inner > r_basket:
            r_inner = r_basket

        inner_pts.append((r_inner, z_inner))

    outer_pts.append((r_basket, 0.0))
    outer_pts.append((r_out, 0.0))

    # Binnenprofiel onderzijde op Z = -wall_thickness
    flange_inner_pts = []
    flange_inner_pts.append((r_out, -wall_thickness))
    flange_inner_pts.append((r_basket, -wall_thickness))
    flange_inner_pts.extend(reversed(inner_pts))
    flange_inner_pts.append((r_cone, -wall_thickness))
    flange_inner_pts.append((r_in, -wall_thickness))

    # Gesloten 2D Polygoon samenstellen
    full_profile = outer_pts + flange_inner_pts
    full_profile.append(outer_pts[0])

    return full_profile, (r_cone, r_basket, r_out)


def create_cadquery_model(slice_angle_deg=60.0):
    try:
        import cadquery as cq
    except ImportError:
        return None, None

    cone_radius = 157.5
    radial_width = 35.0
    roll_height = 25.0
    wall_thickness = 0.9
    flange_width = 10.0
    lap_joint_length = 12.0
    rib_thickness = 0.4

    full_profile, (r_cone, r_basket, r_out) = calculate_surround_profile_points(
        cone_radius, radial_width, roll_height, wall_thickness, flange_width
    )

    print(f"Genereert 3D CadQuery TPU Surround Segment ({slice_angle_deg}° arc)...")
    wp = cq.Workplane("XZ").polyline(full_profile).close()
    segment_solid = wp.revolve(slice_angle_deg, (0, 0, 0), (0, 0, 1))

    # 12mm Lap Joint Flap
    lap_joint_angle = (lap_joint_length / r_out) * (180.0 / math.pi)
    lap_flap = cq.Workplane("XZ").polyline(full_profile).close().revolve(
        lap_joint_angle, (0, 0, 0), (0, 0, 1)
    ).rotate((0, 0, 0), (0, 0, 1), slice_angle_deg)

    final_part = segment_solid.union(lap_flap)

    # 0.4mm Sacrificiële Rib (Z=0 tot Z=23mm)
    r_center = (r_cone + r_basket) / 2.0
    rib_height = roll_height - 2.0

    rib = (cq.Workplane("XY")
           .rect(radial_width - 2.0, rib_thickness)
           .extrude(rib_height)
           .translate((r_center, 0, 0))
           .rotate((0, 0, 0), (0, 0, 1), slice_angle_deg / 2.0))

    final_part_with_ribs = final_part.union(rib)

    # --- Genereren van de 15-Minuten Proef-Print Slice (20mm arc) ---
    print("Genereert 15-Minuten TPU Proef-Print Slice (20mm test-segment)...")
    test_slice_angle = (20.0 / r_out) * (180.0 / math.pi)
    wp_test = cq.Workplane("XZ").polyline(full_profile).close()
    test_segment_solid = wp_test.revolve(test_slice_angle, (0, 0, 0), (0, 0, 1))
    test_lap_flap = cq.Workplane("XZ").polyline(full_profile).close().revolve(
        lap_joint_angle, (0, 0, 0), (0, 0, 1)
    ).rotate((0, 0, 0), (0, 0, 1), test_slice_angle)

    test_slice_part = test_segment_solid.union(test_lap_flap)

    return final_part_with_ribs, test_slice_part


def run_freecad_macro():
    try:
        import FreeCAD as App
        import Part
    except ImportError:
        return False

    cone_radius = 157.5
    radial_width = 35.0
    roll_height = 25.0
    wall_thickness = 0.9
    flange_width = 10.0
    segment_angle = 60.0

    full_profile, _ = calculate_surround_profile_points(
        cone_radius, radial_width, roll_height, wall_thickness, flange_width
    )

    doc = App.newDocument("TPU_Surround_100mm_P2P")
    vecs = [App.Vector(r, 0, z) for r, z in full_profile]
    wire = Part.makePolygon(vecs)
    face = Part.Face(wire)

    revolve_shape = face.revolve(App.Vector(0,0,0), App.Vector(0,0,1), segment_angle)
    shape_obj = doc.addObject("Part::Feature", "TPU_Surround_Segment")
    shape_obj.Shape = revolve_shape
    doc.recompute()
    print("Native FreeCAD 3D Model succesvol gegenereerd!")
    return True


def main():
    print("==================================================")
    print("   FREECAD / CADQUERY 3D SURROUND GENERATOR      ")
    print("==================================================")

    model, test_slice = create_cadquery_model()
    if model is not None:
        import cadquery as cq
        step_file = "tpu_surround_segment_100mm_p2p.step"
        stl_file = "tpu_surround_segment_100mm_p2p.stl"
        test_slice_step_file = "tpu_surround_test_slice_20mm.step"
        test_slice_stl_file = "tpu_surround_test_slice_20mm.stl"

        print(f"Exporteren naar CAD STEP: {step_file}...")
        cq.exporters.export(model, step_file)

        print(f"Exporteren naar 3D-Print STL: {stl_file}...")
        cq.exporters.export(model, stl_file)

        print(f"Exporteren naar Proef-Print Slice STEP: {test_slice_step_file}...")
        cq.exporters.export(test_slice, test_slice_step_file)

        print(f"Exporteren naar Proef-Print Slice STL: {test_slice_stl_file}...")
        cq.exporters.export(test_slice, test_slice_stl_file)

        print("==================================================")
        print(" SUCCESS! 3D CAD & STL Bestanden gegenereerd:")
        print(f" - Volledig Segment STEP: {step_file}")
        print(f" - Volledig Segment STL:  {stl_file}")
        print(f" - 15-Minuten Test Slice STEP: {test_slice_step_file}")
        print(f" - 15-Minuten Test Slice STL:  {test_slice_stl_file}")
        print("==================================================")
    else:
        run_freecad_macro()

if __name__ == '__main__':
    main()
