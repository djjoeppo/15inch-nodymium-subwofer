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
    print("==================================================")

if __name__ == '__main__':
    print_summary()
