import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_motor_designs():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
    fig.suptitle('Motor Ontwerp Vergelijking (Cross-section)', fontsize=16, fontweight='bold')

    # --- Optie A: Traditional Overhung Design ---
    ax1.set_title('Optie A: Traditionele Overhung Motor', fontsize=12, fontweight='bold', pad=10)

    # Backplate
    ax1.add_patch(patches.Rectangle((-50, -10), 100, 10, facecolor='#7f8c8d', edgecolor='black', label='Staal (Back/Top plate)'))
    # Pole piece
    ax1.add_patch(patches.Rectangle((-37.5, 0), 75, 40, facecolor='#95a5a6', edgecolor='black', label='Staal Pole Piece'))
    # Magnet
    ax1.add_patch(patches.Rectangle((-37.5, 0), 75, 15, facecolor='#e74c3c', edgecolor='black', alpha=0.7, label='N48 Magneet (⌀75x15)'))
    # Pole piece top extension
    ax1.add_patch(patches.Rectangle((-37.5, 15), 75, 25, facecolor='#95a5a6', edgecolor='black'))
    # Top plate (left & right)
    ax1.add_patch(patches.Rectangle((-65, 30), 22.5, 10, facecolor='#7f8c8d', edgecolor='black'))
    ax1.add_patch(patches.Rectangle((42.5, 30), 22.5, 10, facecolor='#7f8c8d', edgecolor='black'))

    # Voice coil & Former (left & right)
    ax1.add_patch(patches.Rectangle((-41, 15), 2, 35, facecolor='#f39c12', edgecolor='black', label='Spreekspoel + Former'))
    ax1.add_patch(patches.Rectangle((39, 15), 2, 35, facecolor='#f39c12', edgecolor='black'))

    # Annotations
    ax1.annotate('Luchtspleet (Gap)', xy=(40, 35), xytext=(55, 50),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6), fontsize=9)
    ax1.annotate('50mm Vrije Ruimte\n(Bumper Zone)', xy=(0, -2), xytext=(0, -25),
                 arrowprops=dict(facecolor='blue', shrink=0.05, width=1, headwidth=6),
                 ha='center', fontsize=9, color='blue')

    ax1.set_xlim(-80, 80)
    ax1.set_ylim(-35, 65)
    ax1.set_aspect('equal')
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.set_ylabel('Hoogte (mm)')
    ax1.set_xlabel('Radius / Diameter (mm)')

    # --- Optie B: Neodymium Pot / Cup Design ---
    ax2.set_title('Optie B: Neodymium Pot / Cup Motor (Aanbevolen)', fontsize=12, fontweight='bold', pad=10)

    # Steel Cup / Pot Body
    ax2.add_patch(patches.Rectangle((-50, 0), 100, 10, facecolor='#7f8c8d', edgecolor='black')) # Bottom
    ax2.add_patch(patches.Rectangle((-50, 10), 8, 30, facecolor='#7f8c8d', edgecolor='black'))  # Left wall
    ax2.add_patch(patches.Rectangle((42, 10), 8, 30, facecolor='#7f8c8d', edgecolor='black'))   # Right wall

    # Magnet inside cup
    ax2.add_patch(patches.Rectangle((-37.5, 10), 75, 15, facecolor='#e74c3c', edgecolor='black', alpha=0.7))
    # Pole piece on magnet
    ax2.add_patch(patches.Rectangle((-37.5, 25), 75, 15, facecolor='#95a5a6', edgecolor='black'))

    # Voice coil & Former
    ax2.add_patch(patches.Rectangle((-40, 10), 2, 35, facecolor='#f39c12', edgecolor='black'))
    ax2.add_patch(patches.Rectangle((38, 10), 2, 35, facecolor='#f39c12', edgecolor='black'))

    # Bumper clearance extension
    ax2.add_patch(patches.Rectangle((-37.5, -40), 75, 40, facecolor='#bdc3c7', edgecolor='black', linestyle=':', label='Verdiepte Poolkern (50mm clearance)'))

    # Annotations
    ax2.annotate('Gefocuste Flux Gap', xy=(40, 32.5), xytext=(55, 45),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6), fontsize=9)
    ax2.annotate('Extra 50mm Diepte\ntegen Bottom-Out', xy=(0, -20), xytext=(0, -35),
                 arrowprops=dict(facecolor='blue', shrink=0.05, width=1, headwidth=6),
                 ha='center', fontsize=9, color='blue')

    ax2.set_xlim(-80, 80)
    ax2.set_ylim(-45, 65)
    ax2.set_aspect('equal')
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.set_xlabel('Radius / Diameter (mm)')

    # Legend
    handles, labels = ax1.get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center', ncol=4, bbox_to_anchor=(0.5, 0.02))

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.18)
    plt.savefig('motor_ontwerpen_vergelijking.png', dpi=150)
    print("Afbeelding gegenereerd: motor_ontwerpen_vergelijking.png")

if __name__ == '__main__':
    draw_motor_designs()
