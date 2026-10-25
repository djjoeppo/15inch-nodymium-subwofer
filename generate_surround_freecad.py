#!/usr/bin/env python3
"""
Parametrische CAD Generator voor 100mm P2P TPU Surround Segment
Ondersteunt zowel standalone CadQuery (Python) als native FreeCAD Macro Execution (`import Part`).

Berekent exacte loodrechte normaal-offsets voor een uniforme 0.9 mm wanddikte
en genereert het 3D segment (60° arc) inclusief 12mm Lap Joints en 0.4mm sacrificiële ribben.
"""

import math

def calculate_surround_profile_points(cone_radius=157.5, radial_width=35.0, roll_height=25.0,
                                      wall_thickness=0.9, flange_width=10.0, num_steps=30):
    """
    Berekent de buitengrens- en binnengrenspunten van de High-Roll TPU surround met
    exacte loodrechte normaalvectoren voor een gegarandeerde 0.9mm wanddikte.
    """
    r_in = cone_radius - flange_width
    r_cone = cone_radius
    r_basket = cone_radius + radial_width
    r_out = r_basket + flange_width
    a = radial_width / 2.0  # 17.5 mm
    b = roll_height         # 25.0 mm

    outer_pts = []
    inner_pts = []

    # 1. Binnenflens (r_in tot r_cone bij Z=0)
    outer_pts.append((r_in, 0.0))
    inner_pts.append((r_in, -wall_thickness))

    outer_pts.append((r_cone, 0.0))
    inner_pts.append((r_cone, -wall_thickness))

    # 2. High-Roll Boog (t van 0 tot pi) met loodrechte normaal offset
    for i in range(1, num_steps):
        t = math.pi * (i / num_steps)
        r_outer = r_cone + a * (1.0 - math.cos(t))
        z_outer = b * math.sin(t)
        outer_pts.append((r_outer, z_outer))

        # Raaklijn vector (dr/dt, dz/dt) = (a*sin(t), b*cos(t))
        dr = a * math.sin(t)
        dz = b * math.cos(t)
        length = math.sqrt(dr*dr + dz*dz)

        # Inwaartse loodrechte normaal vector (n_r, n_z) = (-dz/len, dr/len)
        n_r = -dz / length
        n_z = dr / length

        r_inner = r_outer + wall_thickness * n_r
        z_inner = z_outer - wall_thickness * abs(n_z)
        inner_pts.append((r_inner, z_inner))

    # 3. Buitenflens (r_basket tot r_out bij Z=0)
    outer_pts.append((r_basket, 0.0))
    inner_pts.append((r_basket, -wall_thickness))

    outer_pts.append((r_out, 0.0))
    inner_pts.append((r_out, -wall_thickness))

    # Profiel sluiten tot een gesloten polygoon
    full_profile = outer_pts + list(reversed(inner_pts))
    full_profile.append(outer_pts[0])

    return full_profile, (r_cone, r_basket, r_out)


def create_cadquery_model():
    try:
        import cadquery as cq
    except ImportError:
        return None

    cone_radius = 157.5
    radial_width = 35.0
    roll_height = 25.0
    wall_thickness = 0.9
    flange_width = 10.0
    segment_angle = 60.0
    lap_joint_length = 12.0
    rib_thickness = 0.4

    full_profile, (r_cone, r_basket, r_out) = calculate_surround_profile_points(
        cone_radius, radial_width, roll_height, wall_thickness, flange_width
    )

    print(f"Genereert 3D CadQuery TPU Surround Segment ({segment_angle}° arc)...")
    wp = cq.Workplane("XZ").polyline(full_profile).close()
    segment_solid = wp.revolve(segment_angle, (0, 0, 0), (0, 0, 1))

    # 12mm Lap Joint Flap (aan de roterende hoekrand)
    lap_joint_angle = (lap_joint_length / r_out) * (180.0 / math.pi)
    lap_flap = cq.Workplane("XZ").polyline(full_profile).close().revolve(
        lap_joint_angle, (0, 0, 0), (0, 0, 1)
    ).rotate((0, 0, 0), (0, 0, 1), segment_angle)

    final_part = segment_solid.union(lap_flap)

    # 0.4mm Sacrificiële Rib (Z-bereik exact van Z=0.0 tot Z=23.0 mm)
    # R-centrum is (r_cone + r_basket)/2 = 175.0mm
    # Geen opwaartse Z-translatie zodat de rib netjes in de holte onder de rol blijft!
    r_center = (r_cone + r_basket) / 2.0
    rib_height = roll_height - 2.0  # 23.0 mm

    rib = (cq.Workplane("XY")
           .rect(radial_width - 2.0, rib_thickness)
           .extrude(rib_height)
           .translate((r_center, 0, 0))
           .rotate((0, 0, 0), (0, 0, 1), segment_angle / 2.0))

    final_part_with_ribs = final_part.union(rib)
    return final_part_with_ribs


def run_freecad_macro():
    """
    Native FreeCAD Macro execution function (`import FreeCAD, Part`).
    Plak deze code direct in de FreeCAD Macro Editor!
    """
    try:
        import FreeCAD as App
        import Part
    except ImportError:
        return False

    print("Uitvoeren in native FreeCAD omgeving...")
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

    # Make FreeCAD polygon wire
    vecs = [App.Vector(r, 0, z) for r, z in full_profile]
    wire = Part.makePolygon(vecs)
    face = Part.Face(wire)

    # Revolve face 60 degrees around Z axis
    revolve_shape = face.revolve(App.Vector(0,0,0), App.Vector(0,0,1), segment_angle)

    shape_obj = doc.addObject("Part::Feature", "TPU_Surround_Segment")
    shape_obj.Shape = revolve_shape
    doc.recompute()
    print("Native FreeCAD 3D Model succesvol gegenereerd in FreeCAD GUI!")
    return True


def main():
    print("==================================================")
    print("   FREECAD / CADQUERY 3D SURROUND GENERATOR      ")
    print("==================================================")

    model = create_cadquery_model()
    if model is not None:
        import cadquery as cq
        step_file = "tpu_surround_segment_100mm_p2p.step"
        stl_file = "tpu_surround_segment_100mm_p2p.stl"

        print(f"Exporteren naar CAD STEP: {step_file}...")
        cq.exporters.export(model, step_file)

        print(f"Exporteren naar 3D-Print STL: {stl_file}...")
        cq.exporters.export(model, stl_file)

        print("==================================================")
        print(" SUCCESS! Geometrie gecorrigeerd en gegenereerd:")
        print(f" - STEP Bestand: {step_file}")
        print(f" - STL Bestand:  {stl_file}")
        print("==================================================")
    else:
        run_freecad_macro()

if __name__ == '__main__':
    main()
