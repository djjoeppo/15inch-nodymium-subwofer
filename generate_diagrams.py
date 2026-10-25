import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_correct_motor_design():
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.suptitle('Fysisch Accurate Doorsnede: Neodymium Pot-Motor met 50mm Inwaartse Kamer', fontsize=14, fontweight='bold')

    # Dimensions in mm
    # Center axis x=0
    # Magnet: Dia 75mm -> radius 37.5mm, thickness 15mm
    # Pole piece: Dia 75mm -> radius 37.5mm, height 8mm (gap height)
    # Voice coil Former: Dia 3" (76.2mm) -> inner radius 38.1mm, outer radius ~39.0mm
    # Voice coil winding height: 38mm
    # Magnetic Gap: x = 37.5 to 39.0 (1.5mm gap width), y = 15 to 23 (8mm gap height)
    # Internal clearance chamber depth: 50mm below gap (from y = -35 to y = 15)

    # 1. Outer Steel Cup (Stalen Pot Behuizing)
    # Bottom plate of cup: x = -55 to 55, y = -45 to -35 (10mm thick steel)
    ax.add_patch(patches.Rectangle((-55, -45), 110, 10, facecolor='#7f8c8d', edgecolor='black', label='Stalen Pot Behuizing (1008 Staal)'))

    # Outer Cup Vertical Wall: x = -55 to -40 and x = 40 to 55, y = -35 to 23
    ax.add_patch(patches.Rectangle((-55, -35), 15, 58, facecolor='#7f8c8d', edgecolor='black'))
    ax.add_patch(patches.Rectangle((40, -35), 15, 58, facecolor='#7f8c8d', edgecolor='black'))

    # Gap Ring / Top Wall Narrowing (Forms outer boundary of magnetic gap): x = -40 to -39, y = 15 to 23
    ax.add_patch(patches.Rectangle((-42, 15), 3, 8, facecolor='#34495e', edgecolor='black', label='Top Plate / Gap Ring (8mm)'))
    ax.add_patch(patches.Rectangle((39, 15), 3, 8, facecolor='#34495e', edgecolor='black'))

    # 2. Central Magnet Assembly
    # Pedestal under magnet (to raise magnet/pole piece level with top gap ring):
    ax.add_patch(patches.Rectangle((-37.5, -35), 75, 35, facecolor='#95a5a6', edgecolor='black', label='Stalen Verhoging / Voetstuk'))
    # Magnet (N48 ⌀75x15mm): x = -37.5 to 37.5, y = 0 to 15
    ax.add_patch(patches.Rectangle((-37.5, 0), 75, 15, facecolor='#e74c3c', edgecolor='black', alpha=0.8, label='N48 Magneet (⌀75x15mm)'))
    # Central Pole Piece: x = -37.5 to 37.5, y = 15 to 23 (8mm height)
    ax.add_patch(patches.Rectangle((-37.5, 15), 75, 8, facecolor='#95a5a6', edgecolor='black', label='Stalen Poolkern (Pole Piece)'))

    # Pole vent (Centraal koelkanaal): x = -10 to 10, y = -45 to 23
    ax.add_patch(patches.Rectangle((-10, -45), 20, 68, facecolor='white', edgecolor='black', linestyle='--', label='Centraal Koelkanaal (Pole Vent)'))

    # 3. Voice Coil & Former Assembly (Spreekspoel + Drager)
    # Former (Alu/Titanium 0.1mm): radius 38.1mm to 38.3mm, length 60mm (y = -5 to 55)
    # Coil windings: y = 0 to 38 (38mm winding height)
    # Left side:
    ax.add_patch(patches.Rectangle((-38.5, -5), 0.4, 60, facecolor='#f39c12', edgecolor='black', label='Spreekspoeldrager (Former)'))
    ax.add_patch(patches.Rectangle((-38.9, 0), 0.8, 38, facecolor='#d35400', edgecolor='black', label='Koper Spreekspoel (38mm)'))
    # Right side:
    ax.add_patch(patches.Rectangle((38.1, -5), 0.4, 60, facecolor='#f39c12', edgecolor='black'))
    ax.add_patch(patches.Rectangle((38.1, 0), 0.8, 38, facecolor='#d35400', edgecolor='black'))

    # 4. Internal Clearance Chamber (50mm Bottom-Out Protection Zone)
    # Highlight the ring cavity between x=37.5 and x=40, y=-35 to 15
    ax.add_patch(patches.Rectangle((37.5, -35), 2.5, 50, facecolor='#3498db', alpha=0.3, hatch='//', label='50mm Inwaartse Speling (Inwendige Kamer)'))
    ax.add_patch(patches.Rectangle((-40, -35), 2.5, 50, facecolor='#3498db', alpha=0.3, hatch='//'))

    # Annotations
    ax.annotate('8mm Magnetische Luchtspleet (B = 0.99T)', xy=(38.2, 19), xytext=(60, 30),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=6), fontsize=10, fontweight='bold')

    ax.annotate('Inwendige Ringvormige Kamer (50mm Diep)\nSpreekspoel zak naar binnen zonder bodem te raken',
                xy=(38.5, -15), xytext=(55, -15),
                arrowprops=dict(facecolor='blue', shrink=0.05, width=1.5, headwidth=6),
                fontsize=10, color='blue', fontweight='bold')

    ax.annotate('Xmax = +/- 15mm\n(Lineaire Uitslag)', xy=(38.5, 5), xytext=(-80, 5),
                 arrowprops=dict(facecolor='red', shrink=0.05, width=1.5, headwidth=6),
                 fontsize=10, color='red', fontweight='bold')

    ax.set_xlim(-90, 110)
    ax.set_ylim(-55, 65)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_ylabel('Hoogte / Diepte (mm)', fontsize=11)
    ax.set_xlabel('Radius t.o.v. Hartlijn (mm)', fontsize=11)

    plt.legend(loc='upper right', bbox_to_anchor=(1.0, 0.98), fontsize=8)
    plt.tight_layout()
    plt.savefig('motor_ontwerpen_vergelijking.png', dpi=150)
    print("Fysisch accurate doorsnede gegenereerd: motor_ontwerpen_vergelijking.png")


def draw_surround_design_and_segmentation():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    fig.suptitle('TPU Surround Ontwerp voor 100mm Peak-to-Peak (±50mm) Uitslag (100% Supportless)', fontsize=14, fontweight='bold')

    # Subplot 1: Doorsnede en Profiel bij 0mm, +50mm en -50mm uitslag
    ax1.set_title('Angled High-Roll TPU Profiel (45° Supportless Wand)', fontsize=12, fontweight='bold')

    # Parameters: Inner flange at r=157.5mm (Cone edge), Outer flange at r=192.5mm (Basket rim)
    # Radial width w = 35mm. High-Roll height h = 25mm.
    r_cone = 157.5
    r_basket = 192.5

    # 1. Rustpositie (0 mm uitslag)
    theta = np.linspace(0, np.pi, 100)
    r_roll_0 = r_cone + 17.5 * (1 - np.cos(theta))
    z_roll_0 = 25.0 * np.sin(theta)

    # Flanges
    r_flange_inner = np.linspace(147.5, r_cone, 20)
    z_flange_inner = np.zeros_like(r_flange_inner)

    r_flange_outer = np.linspace(r_basket, 202.5, 20)
    z_flange_outer = np.zeros_like(r_flange_outer)

    ax1.plot(np.concatenate([r_flange_inner, r_roll_0, r_flange_outer]),
             np.concatenate([z_flange_inner, z_roll_0, z_flange_outer]),
             'b-', linewidth=3, label='Ruststand (0 mm uitslag)')

    # 2. Uitwaartse Uitslag (+50 mm)
    z_flange_inner_out = np.full_like(r_flange_inner, 50.0)
    z_roll_out = 50.0 * (1 - theta / np.pi) + 18.0 * np.sin(theta)

    ax1.plot(np.concatenate([r_flange_inner, r_roll_0, r_flange_outer]),
             np.concatenate([z_flange_inner_out, z_roll_out, z_flange_outer]),
             'r--', linewidth=2.5, label='Max Uitwaarts (+50 mm Xmech)')

    # 3. Inwaartse Uitslag (-50 mm)
    z_flange_inner_in = np.full_like(r_flange_inner, -50.0)
    z_roll_in = -50.0 * (1 - theta / np.pi) - 18.0 * np.sin(theta)

    ax1.plot(np.concatenate([r_flange_inner, r_roll_0, r_flange_outer]),
             np.concatenate([z_flange_inner_in, z_roll_in, z_flange_outer]),
             'g-.', linewidth=2.5, label='Max Inwaarts (-50 mm Xmech)')

    # Aanduidingen
    ax1.add_patch(patches.Rectangle((142.5, -55), 15, 110, facecolor='#e67e22', alpha=0.3, label='Conus Rand (3D-Geprint)'))
    ax1.add_patch(patches.Rectangle((192.5, -15), 15, 30, facecolor='#7f8c8d', alpha=0.3, label='Basket Bevestigingsrand'))

    ax1.annotate('100mm Peak-to-Peak\nTotale Slaglengte', xy=(147.5, 0), xytext=(115, 0),
                 arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=7),
                 fontsize=10, color='darkred', fontweight='bold')

    ax1.annotate('Max Overhang ≤ 45°\n100% Supportloos Geprint!', xy=(166, 17), xytext=(120, 38),
                 arrowprops=dict(facecolor='green', shrink=0.05, width=2, headwidth=7),
                 fontsize=10, color='darkgreen', fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#e8f8f5', edgecolor='green'))

    ax1.set_xlabel('Radius r (mm)', fontsize=11)
    ax1.set_ylabel('Verticale Positie z (mm)', fontsize=11)
    ax1.set_xlim(110, 215)
    ax1.set_ylim(-65, 65)
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.legend(loc='lower left', fontsize=8)


    # Subplot 2: Vertical Print Orientation & Sacrificial Bracing Ribs
    ax2.set_title('Verticale Print-Oriëntatie (Rechtop op Snijvlak)', fontsize=12, fontweight='bold')

    # Draw Printbed surface (Z=0 line)
    ax2.plot([-80, 80], [0, 0], 'k-', linewidth=4, label='Printbed Oppervlak')
    ax2.add_patch(patches.Rectangle((-80, -10), 160, 10, facecolor='#d5dbdb', edgecolor='black'))

    # Vertical Roll segment standing upright (0 to 134.6mm high)
    # Profile curve standing up
    y_vert = np.linspace(0, 135, 100)
    x_outer_vert = 25.0 * np.sin(np.pi * y_vert / 135.0) + 15.0
    x_inner_vert = x_outer_vert - 1.0  # 1.0mm wall

    ax2.plot(x_outer_vert, y_vert, 'b-', linewidth=2.5, label='TPU Rolwand (0.8-1.0mm)')
    ax2.plot(x_inner_vert, y_vert, 'b-', linewidth=2.5)
    ax2.fill_betweenx(y_vert, x_inner_vert, x_outer_vert, color='#2980b9', alpha=0.6)

    # Sacrificial 0.4mm Bracing Ribs (Driehoeks-vakwerk in holte)
    # Rib 1: y=0 to y=45
    ax2.plot([0, x_inner_vert[33]], [0, y_vert[33]], 'r--', linewidth=1.5, label='0.4mm Sacrificiële Stabilisatierib (Wegsnijdbaar)')
    # Rib 2: y=45 to y=90
    ax2.plot([0, x_inner_vert[66]], [45, y_vert[66]], 'r--', linewidth=1.5)
    # Rib 3: y=90 to y=135
    ax2.plot([0, x_inner_vert[99]], [90, y_vert[99]], 'r--', linewidth=1.5)

    # 10mm Outer Brim
    ax2.add_patch(patches.Rectangle((-15, 0), 15, 1.2, facecolor='#e74c3c', alpha=0.7, label='10mm Outer Brim (Bed Adhesie)'))
    ax2.add_patch(patches.Rectangle((x_outer_vert[0], 0), 15, 1.2, facecolor='#e74c3c', alpha=0.7))

    ax2.annotate('90° Laagopbouw!\nLagen evenwijdig aan buiging,\nVOORKOMT SCHEUREN op laagnaad',
                xy=(x_outer_vert[50], 67.5), xytext=(x_outer_vert[50]+15, 80),
                arrowprops=dict(facecolor='blue', shrink=0.05, width=1.5, headwidth=6),
                fontsize=9, color='darkblue', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#ebf5fb', edgecolor='blue'))

    ax2.annotate('Sacrificiële Ribben (0.4mm)\nVoorkomt "TPU Wobble"\nSimpel weg te snijden met scalpel',
                xy=(10, 45), xytext=(-70, 45),
                arrowprops=dict(facecolor='red', shrink=0.05, width=1.5, headwidth=6),
                fontsize=9, color='darkred', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#fadbd8', edgecolor='red'))

    ax2.set_xlim(-85, 85)
    ax2.set_ylim(-15, 150)
    ax2.set_xlabel('Transversale Breedte (mm)', fontsize=11)
    ax2.set_ylabel('Printhoogte Z-as (mm)', fontsize=11)
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.legend(loc='upper right', fontsize=8)

    plt.tight_layout()
    plt.savefig('surround_ontwerp_en_segmentatie.png', dpi=150)
    print("Surround ontwerp & segmentatie afbeelding gegenereerd: surround_ontwerp_en_segmentatie.png")

if __name__ == '__main__':
    draw_correct_motor_design()
    draw_surround_design_and_segmentation()
