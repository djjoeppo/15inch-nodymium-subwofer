# Ontwerpspecificatie: 15-inch 3D-Geprinte Subwoofer met Neodymium Motor

## 1. Projectoverzicht en Doelstellingen
Dit document bevat de volledige specificatie, berekeningen en bouwrichtlijnen voor een hoogwaardige 15-inch (381 mm) 3D-geprinte subwoofer. Het doel is een geoptimaliseerd, modulair en robuust luidsprekersysteem te bouwen op basis van een custom neodymium magneetmotor, TPU-ophanging en een modulair frame geschikt voor standaard FDM 3D-printers.

---

## 2. Neodymium Motor Ontwerp & Geometrie

### 2.1 Magneet & Topologie
- **Magneet:** 1x N48 Neodymium schijfmagneet (⌀75 mm × 15 mm, houdkracht ca. 250 kg).
- **Motor Topologie:** **Neodymium Pot / Cup Design (Optie B - Aanbevolen)**.
  - De magneet bevindt zich op de bodem van een stalen behuizing (cup).
  - Bovenop de magneet bevindt zich een massieve stalen pole piece.
  - De opstaande stalen rand van de pot vormt de buitenste ring van de luchtspleet.
- **Luchtspleet ($h_{gap}$):** 8 mm hoog.
- **Spreekspoel Diameter:** 3 inch (76.2 mm nominale binnendiameter).

### 2.2 Uitslag ($X_{max}$) & 50 mm Bottom-Out Bescherming
- **Overhung Geometrie:**
  - Spoelhoogte ($h_{vc}$): **38 mm**
  - Gap hoogte ($h_{gap}$): **8 mm**
  - **Lineaire Uitslag ($X_{max}$):** $(38 - 8) / 2 = \mathbf{15 \text{ mm}}$ (30 mm peak-to-peak).
- **50 mm Inwaartse Speling (Bottom-Out Protection):**
  - Om bij extreme experimentele belasting te voorkomen dat de spreekspoel/drager de bodem raakt, wordt een verdiepte kamer (pole chamber) van **50 mm** onder de spreekspoel vrijgehouden.
  - **Effect op prestaties:** Magnetische flux ($B_g$) en $BL$-factor blijven 100% ongewijzigd, aangezien de magnetische luchtspleet zich uitsluitend bij de top plate en poolkern bevindt.

---

## 3. Spreekspoeldrager Materialen: Aluminium vs. Titanium

| Eigenschap | Aluminium Drager (0.10 - 0.15 mm) | Titanium Drager (0.10 mm) |
| :--- | :--- | :--- |
| **Warmtegeleiding** | Extreem hoog (snelle afvoer van warmte) | Matig / Laag |
| **Mechanische Stijfheid** | Goed, maar vervormt sneller onder trek | Uitstekend, zeer hoge treksterkte |
| **Wervelstromen (Eddy Currents)** | Aanwezig (zorgt voor lichte demping) | Vrijwel nihil |
| **Gewicht** | Licht ($\sim 2.7 \text{ g/cm}^3$) | Middel ($\sim 4.5 \text{ g/cm}^3$) |
| **Advies** | **Aanbevolen voor hoge vermogens** vanwege koeling. | Optioneel voor minimale demping / SQ. |

---

## 4. Modulaire 15" Basket Constructie

### 4.1 Opsplitsing voor 256×256×256 mm Printbed
- De buitendiameter van een 15" luidspreker bedraagt ca. 385 mm.
- De basket wordt opgedeeld in **6 symmetrische segmenten**.
- **Verbindingsmethode:**
  - **M4/M5 Stalen Draadeinden:** Lopen over de volle lengte door de basket-spaken om de constructie onder constante voorspanning te houden.
  - **Pen-en-Gat Uitlijning (Alignment Dowels):** Zorgen voor een exacte positionering en voorkomen afschuiving.
  - **2-Componenten Epoxy (of CA-lijm met activator):** Verlijming op de contactvlakken voor een luchtdichte en monolithische structuur.

---

## 5. TPU Spider en Surround Specificaties

### 5.1 TPU Surround (Randschuim/Rubber vervanging)
- **Materiaal:** TPU (Shore 85A of 95A).
- **Vorm:** Meervoudige rol / dubbele rol (roll-geometry) voor lineaire veerkarakteristiek bij uitslagen tot $\pm 20 \text{ mm}$.
- **Wanddikte:** 0.8 mm tot 1.2 mm (2 tot 3 perimeters).

### 5.2 TPU Spider (Ophanging / Centreerspin)
- **Vorm:** Progressieve golving (concentrische ringen) om stijfheid te bieden rond de spreekspoel en flexibiliteit in het horizontale vlak.
- **Centrering:** Houdt de 3" spreekspoel exact in het midden van de luchtspleet van 8 mm.

---

## 6. Frequentiebereik en Behuizing
- **Beoogd Frequentiebereik:** 20 Hz – 100 Hz (Sub-bass).
- **Aanbevolen Behuizings-type:**
  - **Bass-Reflex (Gepoort):** Voor maximale SPL rond 25-35 Hz.
  - **Gesloten Behuizing:** Voor strakke transient response en infrasone uitsturing met DSP correctie.

---

## 7. Schematisch Overzicht Motor
Zie het gegenereerde schematische diagram `motor_ontwerpen_vergelijking.png` voor de visuele doorsnede van de motor inclusief de 50 mm clearance zone.
