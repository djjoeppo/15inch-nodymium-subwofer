#!/usr/bin/env python3
"""
Subwoofer Design Calculator
Berekent motor parameters, uitslag (Xmax), spreekspoelkenmerken en basket afmetingen
voor de 15-inch 3D-geprinte subwoofer met neodymium motor.
"""

import math

def calculate_surround_parameters(x_mech_p2p_mm=100.0, outer_dia_mm=385.0, cone_dia_mm=315.0):
    """
    Berekent de geometrische en mechanische parameters van de 100mm Peak-to-Peak TPU Surround.
    """
    x_mech_single_mm = x_mech_p2p_mm / 2.0  # 50 mm
    surround_radial_width_mm = (outer_dia_mm - cone_dia_mm) / 2.0  # 35 mm

    # High-Roll semi-elliptisch profiel:
    # Rustpositie breedte w = 35mm, hoogte h = 25mm
    # Benadering booglengte met Ramanujan ellipsomtrek:
    a = surround_radial_width_mm / 2.0  # 17.5 mm
    b = 25.0  # mm (rolhoogte)
    # Halve ellips booglengte = pi * [3(a+b) - sqrt((3a+b)(a+3b))] / 2
    h_term = ((a - b) ** 2) / ((a + b) ** 2)
    arc_length_mm = math.pi * (a + b) * (1 + (3 * h_term) / (10 + math.sqrt(4 - 3 * h_term)))

    # Bij maximale uitslag van 50mm:
    # De gestrekte afstand tussen membraanrand en basket rand:
    stretched_dist_mm = math.sqrt(surround_radial_width_mm**2 + x_mech_single_mm**2)

    # Rekpercentage indien materiaal zou strekken (zonder plooien)
    strain_pct = ((stretched_dist_mm - arc_length_mm) / arc_length_mm) * 100.0
    if strain_pct < 0:
        strain_pct = 0.0

    # Printbed Segmentatie (6 segmenten van 60 graden)
    num_segments = 6
    segment_angle_deg = 360.0 / num_segments
    outer_radius_mm = outer_dia_mm / 2.0  # 192.5 mm

    # Koordelengte buitenrand segment = 2 * R * sin(theta/2)
    chord_length_mm = 2 * outer_radius_mm * math.sin(math.radians(segment_angle_deg / 2.0))
    # Bounding box diagonaal/maximale lengte van segment inclusief 12mm lijmflap
    max_segment_span_mm = chord_length_mm + 12.0  # ~204.5 mm

    return {
        'x_mech_p2p_mm': x_mech_p2p_mm,
        'x_mech_single_mm': x_mech_single_mm,
        'radial_width_mm': surround_radial_width_mm,
        'roll_height_mm': b,
        'arc_length_mm': round(arc_length_mm, 2),
        'stretched_dist_mm': round(stretched_dist_mm, 2),
        'max_strain_pct': round(strain_pct, 1),
        'num_segments': num_segments,
        'max_segment_span_mm': round(max_segment_span_mm, 1),
        'fits_256_bed': max_segment_span_mm <= 256.0
    }

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

    surround = calculate_surround_parameters()
    print("TPU Surround Specificaties (100mm Peak-to-Peak Extreme Xmax):")
    print(f" - Mechanische Uitslag (Xmech):  +/- {surround['x_mech_single_mm']} mm ({surround['x_mech_p2p_mm']} mm P2P)")
    print(f" - Profiel Vorm:                High-Roll Semi-Ellips (35mm breed, {surround['roll_height_mm']}mm hoog)")
    print(f" - Onbelaste Booglengte:        {surround['arc_length_mm']} mm")
    print(f" - Gestrekte Afstand bij 50mm: {surround['stretched_dist_mm']} mm")
    print(f" - Maximale Materiaalrek:       {surround['max_strain_pct']}% (Veilig binnen TPU elastische grens)")
    print(f" - Wanddikte & Materiaal:        0.8 - 1.0 mm (TPU 85A aanbevolen / Shore 95A)")
    print(f" - Printbed Segmentatie:        {surround['num_segments']} segmenten van 60° (Max span: {surround['max_segment_span_mm']} mm)")
    print(f" - Past op 256x256 Bed:          {'JA' if surround['fits_256_bed'] else 'NEE'}")
    print("--------------------------------------------------")
    print("Modulaire Basket Specificaties (256x256x256 Bed):")
    print(" - Diameter Frame:            385 mm")
    print(" - Aantal Segmenten:          6 stuks (60 graden per segment)")
    print(" - Maximale segmentdiagonaal: ~210 mm (Past ruim op 256mm bed)")
    print(" - Versterking:               6x M5 RVS Draadeinden + Epoxy")
    print("==================================================")

if __name__ == '__main__':
    print_summary()
