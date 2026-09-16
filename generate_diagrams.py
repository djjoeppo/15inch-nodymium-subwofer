import matplotlib.pyplot as plt
import matplotlib.patches as patches

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

if __name__ == '__main__':
    draw_correct_motor_design()
