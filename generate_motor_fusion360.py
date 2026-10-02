# Script name: generate_motor_fusion360.py
# Description: Fusion 360 Python Script voor het automatisch genereren van de 15" Neodymium Subwoofer Motor.
#
# Hoe te gebruiken in Fusion 360:
# 1. Open Autodesk Fusion 360.
# 2. Ga naar UTILITIES -> Scripts and Add-Ins (of druk op Shift + S).
# 3. Klik op "Create" onder Scripts, kies Python, noem het "GenerateNeodymiumMotor".
# 4. Klik op "Edit" en vervang de inhoud van het geopende bestand door deze code.
# 5. Sla op en klik op "Run" in Fusion 360!

import adsk.core, adsk.fusion, traceback
import math

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        # Controleer of er een actief document is
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        if not design:
            ui.messageBox('Open een actief Fusion 360 ontwerp voordat je dit script uitvoert.')
            return

        # Let op: Fusion 360 API werkt intern in CENTIMETERS (cm).
        # We converteren mm naar cm door te delen door 10.0.
        def mm(value):
            return value / 10.0

        rootComp = design.rootComponent

        # ==========================================
        # DIMENSIES (in millimeter)
        # ==========================================
        # Poolkern & Magneet
        magnet_dia = 75.0
        magnet_rad = magnet_dia / 2.0  # 37.5 mm
        magnet_thick = 15.0            # 15 mm

        pole_height = 8.0              # 8 mm gap hoogte
        pedestal_height = 35.0         # 35 mm verhoging onder magneet

        # Koelkanaal (Pole vent)
        vent_dia = 20.0
        vent_rad = vent_dia / 2.0      # 10 mm

        # Stalen Pot
        cup_bottom_thick = 10.0        # 10 mm bodemplaat
        cup_outer_dia = 110.0
        cup_outer_rad = cup_outer_dia / 2.0 # 55 mm
        cup_inner_wall_rad = 40.0      # 40 mm (vormt 50mm diepe kamer met 37.5mm voetstuk)

        # Top Plate / Gap Ring
        gap_ring_inner_rad = 39.0      # 39 mm (1.5mm luchtspleet t.o.v. 37.5mm poolkern)
        gap_ring_outer_rad = 42.0      # 42 mm
        gap_ring_height = 8.0          # 8 mm

        # Spreekspoel & Drager
        former_inner_rad = 38.1        # 3" inner dia = 76.2mm -> rad 38.1mm
        former_thick = 0.15            # 0.15 mm
        former_height = 60.0
        former_z_start = -5.0

        coil_height = 38.0             # 38 mm wikkelling
        coil_thick = 0.68              # 2 lagen 0.3mm draad (0.34mm incl lak) = 0.68mm

        # Positioneringen op Z-as (mm)
        z_bottom_base = - (cup_bottom_thick + pedestal_height) # -45 mm
        z_pedestal_top = 0.0
        z_magnet_top = magnet_thick                            # +15 mm
        z_pole_top = z_magnet_top + pole_height                # +23 mm

        # Helper functie om een nieuwe component aan te maken
        def create_component(name):
            transform = adsk.core.Matrix3D.create()
            occurrence = rootComp.occurrences.addNewComponent(transform)
            comp = occurrence.component
            comp.name = name
            return comp

        # ==========================================
        # 1. STALEN POT BEHUIZING (CUP ASSEMBLY)
        # ==========================================
        cup_comp = create_component("1. Stalen Pot Behuizing")
        sketches = cup_comp.sketches
        xyPlane = cup_comp.xYConstructionPlane

        # Draai-profiel (Revolve) tekenen voor de pot
        sketch = sketches.add(xyPlane)
        lines = sketch.sketchCurves.sketchLines

        # Punten definitie voor pot profiel (in cm)
        # Bodemplaat + Buitenwand + Gap Ring
        p1 = adsk.core.Point3D.create(mm(vent_rad), mm(z_bottom_base), 0)
        p2 = adsk.core.Point3D.create(mm(cup_outer_rad), mm(z_bottom_base), 0)
        p3 = adsk.core.Point3D.create(mm(cup_outer_rad), mm(z_magnet_top + gap_ring_height), 0)
        p4 = adsk.core.Point3D.create(mm(gap_ring_inner_rad), mm(z_magnet_top + gap_ring_height), 0)
        p5 = adsk.core.Point3D.create(mm(gap_ring_inner_rad), mm(z_magnet_top), 0)
        p6 = adsk.core.Point3D.create(mm(cup_inner_wall_rad), mm(z_magnet_top), 0)
        p7 = adsk.core.Point3D.create(mm(cup_inner_wall_rad), mm(z_bottom_base + cup_bottom_thick), 0)
        p8 = adsk.core.Point3D.create(mm(vent_rad), mm(z_bottom_base + cup_bottom_thick), 0)

        lines.addByTwoPoints(p1, p2)
        lines.addByTwoPoints(p2, p3)
        lines.addByTwoPoints(p3, p4)
        lines.addByTwoPoints(p4, p5)
        lines.addByTwoPoints(p5, p6)
        lines.addByTwoPoints(p6, p7)
        lines.addByTwoPoints(p7, p8)
        lines.addByTwoPoints(p8, p1)

        # Hartlijn voor Revolve (Z-as)
        axis_line = lines.addByTwoPoints(
            adsk.core.Point3D.create(0, mm(z_bottom_base), 0),
            adsk.core.Point3D.create(0, mm(z_pole_top), 0)
        )

        prof = sketch.profiles.item(0)
        revolves = cup_comp.features.revolveFeatures
        revInput = revolves.createInput(prof, axis_line, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(2 * math.pi)
        revInput.setAngleExtent(False, angle)
        revolves.add(revInput)

        # ==========================================
        # 2. STALEN VOETSTUK (PEDESTAL)
        # ==========================================
        ped_comp = create_component("2. Stalen Voetstuk")
        sketch = ped_comp.sketches.add(ped_comp.xYConstructionPlane)
        lines = sketch.sketchCurves.sketchLines

        p1 = adsk.core.Point3D.create(mm(vent_rad), mm(z_bottom_base + cup_bottom_thick), 0)
        p2 = adsk.core.Point3D.create(mm(magnet_rad), mm(z_bottom_base + cup_bottom_thick), 0)
        p3 = adsk.core.Point3D.create(mm(magnet_rad), mm(z_pedestal_top), 0)
        p4 = adsk.core.Point3D.create(mm(vent_rad), mm(z_pedestal_top), 0)

        lines.addByTwoPoints(p1, p2)
        lines.addByTwoPoints(p2, p3)
        lines.addByTwoPoints(p3, p4)
        lines.addByTwoPoints(p4, p1)

        axis_line = lines.addByTwoPoints(
            adsk.core.Point3D.create(0, mm(z_bottom_base), 0),
            adsk.core.Point3D.create(0, mm(z_pole_top), 0)
        )

        prof = sketch.profiles.item(0)
        revInput = ped_comp.features.revolveFeatures.createInput(prof, axis_line, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        revInput.setAngleExtent(False, angle)
        ped_comp.features.revolveFeatures.add(revInput)

        # ==========================================
        # 3. N48 NEODYMIUM MAGNEET
        # ==========================================
        mag_comp = create_component("3. N48 Neodymium Magneet (75x15mm)")
        sketch = mag_comp.sketches.add(mag_comp.xYConstructionPlane)
        lines = sketch.sketchCurves.sketchLines

        p1 = adsk.core.Point3D.create(mm(vent_rad), mm(z_pedestal_top), 0)
        p2 = adsk.core.Point3D.create(mm(magnet_rad), mm(z_pedestal_top), 0)
        p3 = adsk.core.Point3D.create(mm(magnet_rad), mm(z_magnet_top), 0)
        p4 = adsk.core.Point3D.create(mm(vent_rad), mm(z_magnet_top), 0)

        lines.addByTwoPoints(p1, p2)
        lines.addByTwoPoints(p2, p3)
        lines.addByTwoPoints(p3, p4)
        lines.addByTwoPoints(p4, p1)

        axis_line = lines.addByTwoPoints(
            adsk.core.Point3D.create(0, mm(z_bottom_base), 0),
            adsk.core.Point3D.create(0, mm(z_pole_top), 0)
        )

        prof = sketch.profiles.item(0)
        revInput = mag_comp.features.revolveFeatures.createInput(prof, axis_line, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        revInput.setAngleExtent(False, angle)
        mag_comp.features.revolveFeatures.add(revInput)

        # ==========================================
        # 4. STALEN POOLKERN (POLE PIECE)
        # ==========================================
        pole_comp = create_component("4. Stalen Poolkern")
        sketch = pole_comp.sketches.add(pole_comp.xYConstructionPlane)
        lines = sketch.sketchCurves.sketchLines

        p1 = adsk.core.Point3D.create(mm(vent_rad), mm(z_magnet_top), 0)
        p2 = adsk.core.Point3D.create(mm(magnet_rad), mm(z_magnet_top), 0)
        p3 = adsk.core.Point3D.create(mm(magnet_rad), mm(z_pole_top), 0)
        p4 = adsk.core.Point3D.create(mm(vent_rad), mm(z_pole_top), 0)

        lines.addByTwoPoints(p1, p2)
        lines.addByTwoPoints(p2, p3)
        lines.addByTwoPoints(p3, p4)
        lines.addByTwoPoints(p4, p1)

        axis_line = lines.addByTwoPoints(
            adsk.core.Point3D.create(0, mm(z_bottom_base), 0),
            adsk.core.Point3D.create(0, mm(z_pole_top), 0)
        )

        prof = sketch.profiles.item(0)
        revInput = pole_comp.features.revolveFeatures.createInput(prof, axis_line, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        revInput.setAngleExtent(False, angle)
        pole_comp.features.revolveFeatures.add(revInput)

        # ==========================================
        # 5. SPREEKSPOEL & DRAGER (3" FORMER + COIL)
        # ==========================================
        vc_comp = create_component("5. Spreekspoel en Drager Assembly")

        # 5a. Drager (Former)
        sketch_former = vc_comp.sketches.add(vc_comp.xYConstructionPlane)
        lines = sketch_former.sketchCurves.sketchLines

        f_outer_rad = former_inner_rad + former_thick
        p1 = adsk.core.Point3D.create(mm(former_inner_rad), mm(former_z_start), 0)
        p2 = adsk.core.Point3D.create(mm(f_outer_rad), mm(former_z_start), 0)
        p3 = adsk.core.Point3D.create(mm(f_outer_rad), mm(former_z_start + former_height), 0)
        p4 = adsk.core.Point3D.create(mm(former_inner_rad), mm(former_z_start + former_height), 0)

        lines.addByTwoPoints(p1, p2)
        lines.addByTwoPoints(p2, p3)
        lines.addByTwoPoints(p3, p4)
        lines.addByTwoPoints(p4, p1)

        axis_line = lines.addByTwoPoints(
            adsk.core.Point3D.create(0, mm(z_bottom_base), 0),
            adsk.core.Point3D.create(0, mm(z_pole_top), 0)
        )

        prof = sketch_former.profiles.item(0)
        revInput = vc_comp.features.revolveFeatures.createInput(prof, axis_line, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        revInput.setAngleExtent(False, angle)
        vc_comp.features.revolveFeatures.add(revInput)

        # 5b. Windingen (Koper spoel)
        sketch_coil = vc_comp.sketches.add(vc_comp.xYConstructionPlane)
        lines = sketch_coil.sketchCurves.sketchLines

        c_outer_rad = f_outer_rad + coil_thick
        coil_z_start = 0.0 # Winding van z=0 tot z=38mm
        p1 = adsk.core.Point3D.create(mm(f_outer_rad), mm(coil_z_start), 0)
        p2 = adsk.core.Point3D.create(mm(c_outer_rad), mm(coil_z_start), 0)
        p3 = adsk.core.Point3D.create(mm(c_outer_rad), mm(coil_z_start + coil_height), 0)
        p4 = adsk.core.Point3D.create(mm(f_outer_rad), mm(coil_z_start + coil_height), 0)

        lines.addByTwoPoints(p1, p2)
        lines.addByTwoPoints(p2, p3)
        lines.addByTwoPoints(p3, p4)
        lines.addByTwoPoints(p4, p1)

        axis_line = lines.addByTwoPoints(
            adsk.core.Point3D.create(0, mm(z_bottom_base), 0),
            adsk.core.Point3D.create(0, mm(z_pole_top), 0)
        )

        prof = sketch_coil.profiles.item(0)
        revInput = vc_comp.features.revolveFeatures.createInput(prof, axis_line, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        revInput.setAngleExtent(False, angle)
        vc_comp.features.revolveFeatures.add(revInput)

        ui.messageBox('Gefeliciteerd! De Neodymium Subwoofer Motor is succesvol gegenereerd in Fusion 360 met 5 afzonderlijke componenten!')

    except:
        if ui:
            ui.messageBox('Er is een fout opgetreden:\n{}'.format(traceback.format_exc()))

if __name__ == '__main__':
    run(None)
