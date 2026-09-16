#!/usr/bin/env python3
"""
Subwoofer Design Calculator
Berekent motor parameters, uitslag (Xmax), spreekspoelkenmerken en basket afmetingen
voor de 15-inch 3D-geprinte subwoofer met neodymium motor.
"""

import math

def calculate_motor_parameters(h_gap_mm, h_vc_mm, clearance_mm, magnet_dia_mm, magnet_thick_mm):
    """
    Berekent de mechanische en magnetische dimensies van de motor.
    """
    xmax_mm = (h_vc_mm - h_gap_mm) / 2.0
    xmech_mm = xmax_mm + clearance_mm

    # Beknopte inschatting van de magnetische fluxdichtheid B_g (Tesla) voor N48 pot motor
    # Remanentie N48 Br ~ 1.4 Tesla
    br_n48 = 1.38 # Tesla
    gap_width_mm = 1.5 # mm luchtspleet breedte tussen poolkern en cup
    bg_est = br_n48 * (magnet_thick_mm / (magnet_thick_mm + (gap_width_mm * 4)))

    return {
        'h_gap_mm': h_gap_mm,
        'h_vc_mm': h_vc_mm,
        'xmax_mm': xmax_mm,
        'clearance_mm': clearance_mm,
        'xmech_max_inward_mm': clearance_mm + (h_vc_mm / 2.0),
        'bg_est_tesla': round(bg_est, 2),
        'magnet_dim': f"⌀{magnet_dia_mm}mm x {magnet_thick_mm}mm N48"
    }

def print_summary():
    print("==================================================")
    print("   15\" 3D-GEPRINTE SUBWOOFER MOTOR CALCULATOR    ")
    print("==================================================")

    # Standaard parameters volgens onze ontwerpspecificatie
    motor = calculate_motor_parameters(
        h_gap_mm=8.0,
        h_vc_mm=38.0,
        clearance_mm=50.0,
        magnet_dia_mm=75.0,
        magnet_thick_mm=15.0
    )

    print(f"Magneet:                      {motor['magnet_dim']}")
    print(f"Luchtspleethoogte (h_gap):    {motor['h_gap_mm']} mm")
    print(f"Spreekspoelhoogte (h_vc):     {motor['h_vc_mm']} mm")
    print(f"Lineaire uitslag (Xmax):       +/- {motor['xmax_mm']} mm ({motor['xmax_mm']*2} mm peak-to-peak)")
    print(f"Inwaartse Bottom-Out Clearance: {motor['clearance_mm']} mm")
    print(f"Geschatte Fluxdichtheid (Bg): ~{motor['bg_est_tesla']} Tesla")
    print("--------------------------------------------------")
    print("Modulaire Basket Specificaties (256x256x256 Bed):")
    print(" - Diameter Frame:            385 mm")
    print(" - Aantal Segmenten:          6 stuks (60 graden per segment)")
    print(" - Maximale segmentdiagonaal: ~210 mm (Past ruim op 256mm bed)")
    print(" - Versterking:               6x M5 RVS Draadeinden + Epoxy")
    print("==================================================")

if __name__ == '__main__':
    print_summary()
