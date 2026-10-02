#!/usr/bin/env python3
"""
Subwoofer Design Calculator
Berekent motor parameters, uitslag (Xmax), spreekspoelkenmerken en basket afmetingen
voor de 15-inch 3D-geprinte subwoofer met neodymium motor.
"""

import math

def calculate_winding_specifications(wire_bare_mm=0.30, wire_outer_mm=0.34, winding_height_mm=38.0, former_outer_dia_mm=76.4):
    """
    Berekent de exacte winding maten voor de spreekspoel.
    """
    num_layers = 2
    # Windings density per layer (tight packing factor ~0.95 or close)
    turns_per_layer = math.floor(winding_height_mm / wire_outer_mm)
    total_turns = turns_per_layer * num_layers

    # Average diameter for the 2 layers
    # Layer 1 mean dia: former_outer_dia_mm + wire_outer_mm
    # Layer 2 mean dia: former_outer_dia_mm + 3 * wire_outer_mm
    mean_dia_mm = former_outer_dia_mm + num_layers * wire_outer_mm
    mean_circumference_m = (math.pi * mean_dia_mm) / 1000.0

    total_wire_length_single_m = total_turns * mean_circumference_m

    # Copper resistivity: 0.0172 Ohm * mm^2 / m
    cross_section_mm2 = math.pi * ((wire_bare_mm / 2.0) ** 2)
    resistance_single_strand = 0.0172 * total_wire_length_single_m / cross_section_mm2

    # Thermal & Power handling estimations for 4 strands parallel (Quadfilar)
    # Total copper volume & mass
    num_strands = 4
    total_copper_len_m = total_wire_length_single_m * num_strands
    vol_copper_cm3 = (cross_section_mm2 / 100.0) * (total_copper_len_m * 100.0)
    density_copper_g_cm3 = 8.96
    mass_copper_g = vol_copper_cm3 * density_copper_g_cm3

    # Surface area for heat dissipation (Inner & Outer surface of cylinder)
    cyl_area_cm2 = 2 * (math.pi * (former_outer_dia_mm / 10.0) * (winding_height_mm / 10.0))

    # Standard enamelled copper wire current density for short duration vs continuous airflow
    # For aluminum former + forced air movement from movement (pole vent): ~8-12 A/mm2 continuous
    total_cross_section_mm2 = cross_section_mm2 * num_strands
    continuous_current_rms_a = total_cross_section_mm2 * 10.0 # ~10 A/mm2
    re_quadfilar = resistance_single_strand / num_strands
    p_rms_continuous = (continuous_current_rms_a ** 2) * re_quadfilar
    p_music_peak = p_rms_continuous * 2.0

    return {
        'wire_bare_mm': wire_bare_mm,
        'wire_outer_mm': wire_outer_mm,
        'winding_height_mm': winding_height_mm,
        'num_layers': num_layers,
        'turns_per_layer': turns_per_layer,
        'total_turns': total_turns,
        'total_layer_thickness_mm': num_layers * wire_outer_mm,
        'length_per_strand_m': round(total_wire_length_single_m, 2),
        'res_1_strand': round(resistance_single_strand, 2),
        'res_2_parallel': round(resistance_single_strand / 2, 2),
        'res_3_parallel': round(resistance_single_strand / 3, 2),
        'res_4_parallel': round(resistance_single_strand / 4, 2),
        'res_6_parallel': round(resistance_single_strand / 6, 2),
        'res_8_parallel': round(resistance_single_strand / 8, 2),
        'copper_mass_g': round(mass_copper_g, 1),
        'surface_area_cm2': round(cyl_area_cm2, 1),
        'p_rms_watts': round(p_rms_continuous),
        'p_peak_watts': round(p_music_peak)
    }

def print_summary():
    print("==================================================")
    print("   SPREEKSPOEL WINDING MATEN (0.3 mm Draad)       ")
    print("==================================================")

    spec = calculate_winding_specifications()

    print(f"Draaddiameter (koper):        {spec['wire_bare_mm']} mm")
    print(f"Draaddiameter (incl. lak):    {spec['wire_outer_mm']} mm")
    print(f"Windingshoogte (h_vc):        {spec['winding_height_mm']} mm")
    print(f"Aantal Lagen:                 {spec['num_layers']} lagen")
    print(f"Totale Wikkeldikte:           {spec['total_layer_thickness_mm']:.2f} mm")
    print(f"Windingen per Laag:           {spec['turns_per_layer']} windingen")
    print(f"Totaal Windingen (per draad): {spec['total_turns']} windingen")
    print(f"Draadlengte per spoor:        {spec['length_per_strand_m']} meter")
    print("--------------------------------------------------")
    print("PARALLEL OPTIES & WEERSTAND (R_e):")
    print(f" - 2 draden parallel (Bifilair):  R_e = {spec['res_2_parallel']} Ohm")
    print(f" - 4 draden parallel (Quadfilar): R_e = {spec['res_4_parallel']} Ohm  (Dual 2x 6.5 Ohm of single 3.3 Ohm)")
    print(f" - 6 draden parallel (Hexafilar): R_e = {spec['res_6_parallel']} Ohm  (Dual 2x 4.3 Ohm = 2.1 Ohm parallel)")
    print(f" - 8 draden parallel (Octafilar): R_e = {spec['res_8_parallel']} Ohm  (Dual 2x 3.2 Ohm = 1.6 Ohm parallel)")
    print("--------------------------------------------------")
    print("BELASTBAAR VERMOGEN (POWER HANDLING ESTIMATE):")
    print(f" - Kopermassa spoel:          {spec['copper_mass_g']} gram")
    print(f" - Koeloppervlakte spoel:     {spec['surface_area_cm2']} cm²")
    print(f" - Continu Vermogen (RMS):    ~{spec['p_rms_watts']} Watt RMS")
    print(f" - Miek/Muziek Vermogen (Peak): ~{spec['p_peak_watts']} Watt Peak")
    print("==================================================")

if __name__ == '__main__':
    print_summary()
