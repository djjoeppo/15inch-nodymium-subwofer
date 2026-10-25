# Ontwerpspecificatie: 15-inch 3D-Geprinte Subwoofer met Neodymium Motor & 100mm P2P Surround

## 1. Projectoverzicht en Doelstellingen
Dit document bevat de volledige specificatie, berekeningen en bouwrichtlijnen voor een hoogwaardige 15-inch (381 mm) 3D-geprinte subwoofer. Het doel is een geoptimaliseerd, modulair en robuust luidsprekersysteem te bouwen op basis van een custom neodymium magneetmotor, TPU-ophanging geschikt voor extreme mechanische uitslagen tot **100 mm Peak-to-Peak (±50 mm)**, en een modulair frame geschikt voor standaard FDM 3D-printers met een printbed van **256×256×256 mm**.

---

## 2. Neodymium Motor Ontwerp & Geometrie

### 2.1 Magneet & Topologie
- **Magneet:** 1x N48 Neodymium schijfmagneet (⌀75 mm × 15 mm, houdkracht ca. 250 kg).
- **Motor Topologie:** **Neodymium Pot / Cup Design met Geïntegreerde Inwendige Kamer**.
  - De magneet (⌀75x15mm) en stalen poolkern bevinden zich op een centraal voetstuk in de stalen pot.
  - De opstaande stalen rand van de pot vormt aan de bovenzijde de buitenste luchtspleetring (8 mm hoog).
  - Tussen het centrale voetstuk en de buitenwand bevindt zich een **ringvormige inwendige kamer (50 mm diep)** waar de 3" spreekspoeldrager vrij in kan bewegen.
- **Luchtspleet ($h_{gap}$):** 8 mm hoog ($B \approx 0.99 \text{ Tesla}$).
- **Spreekspoel Diameter:** 3 inch (76.2 mm nominale binnendiameter).

### 2.2 Uitslag ($X_{max}$) & Inwendige 50 mm Bottom-Out Kamer
- **Overhung Geometrie:**
  - Spoelhoogte ($h_{vc}$): **38 mm**
  - Gap hoogte ($h_{gap}$): **8 mm**
  - **Lineaire Uitslag ($X_{max}$):** $(38 - 8) / 2 = \mathbf{15 \text{ mm}}$ (30 mm peak-to-peak).
- **50 mm Inwendige Kamer (Bottom-Out Bescherming):**
  - Binnenin de stalen cup bevindt zich een 50 mm diepe ringvormige sleuf.
  - Bij extreem grote inwaartse uitslag zakt de spreekspoeldrager in deze kamer weg **zonder ooit de bodem van de motor te raken**.
  - **Effect op prestaties:** Magnetische flux ($B_g$) and $BL$-factor blijven 100% geoptimaliseerd, aangezien de magnetische luchtspleet zich uitsluitend bij de bovenste top plate ring en poolkern bevindt.

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
- De basket wordt opgedeeld in **6 symmetrische segmenten van 60°**.
- **Verbindingsmethode:**
  - **M4/M5 Stalen Draadeinden:** Lopen over de volle lengte door de basket-spaken om de constructie onder constante voorspanning te houden.
  - **Pen-en-Gat Uitlijning (Alignment Dowels):** Zorgen voor een exacte positionering en voorkomen afschuiving.
  - **2-Componenten Epoxy (of CA-lijm met activator):** Verlijming op de contactvlakken voor een luchtdichte en monolithische structuur.

---

## 5. TPU Spider en Extreme 100mm P2P Surround Specificaties

### 5.1 TPU Surround Ontwerp (100 mm Peak-to-Peak / ±50 mm $X_{mech}$)
Om een extreme mechanische uitslag van **100 mm peak-to-peak (±50 mm)** op te vangen zonder dat de rubberen rand scheurt, knikt of de conus blokkeert, is een **geoptimaliseerd High-Roll TPU profiel** ontworpen.

#### A. Geometrisch Profiel & Mechanica
- **Profiel Vorm:** **High-Roll Semi-Ellips / Angled High-Roll**.
- **Radiale Breedte ($w$):** **35 mm** (tussen conus buitenrand $\varnothing 315 \text{ mm}$ en basket binnenrand $\varnothing 385 \text{ mm}$).
- **Onbelaste Rolhoogte ($h$):** **25 mm**.
- **Onbelaste Booglengte:** **~134.6 mm**.
- **Vervormingsmechanisme:** Bij een maximale uitslag van ±50 mm bedraagt de gestrekte lineaire afstand tussen conus- en basketrand slechts **61.0 mm** ($\sqrt{35^2 + 50^2}$).
  - Doordat de onbelaste booglengte (134.6 mm) ruim groter is dan de gestrekte afstand (61.0 mm), hoeft het TPU materiaal **niet plastisch te strekken**.
  - De verplaatsing wordt opgevangen door een natuurlijk, geleidelijk **afrollen en buigen** van het profiel.
  - De feitelijke materiaalrek blijft ruimschoots onder **<11%**, wat ver binnen het elastische bereik van TPU ligt (TPU verdraagt >400% rek zonder blijvende vervorming).

#### B. 100% Supportloze Printbaarheid (Geen Tree Supports Nodig!)
Bij het printen van TPU op hoge temperaturen (**240°C – 260°C**) voor maximale laagfusiestrekte, is het gebruik van (tree) supports **ongeschikt** doordat TPU sterk aan supportmateriaal fused en het verwijderen ervan de 0.8 mm dunne wand kan beschadigen. Daarom is het TPU surround ontworpen voor **100% supportloos printen**:

1. **Optie 1: Plat Printen op het Bed (Angled High-Roll Profile)**
   - De wanden van de rol stijgen op onder een hoek van **≤ 45°** t.o.v. het printbed.
   - Iedere FDM 3D-printer kan TPU onder 45° overhang strak en vlekkeloos printen zonder enige ondersteuning.
   - De bovenzijde heeft een zachte afronding die door bruggen/gecontroleerde oversteken wordt opgevangen.

2. **Optie 2: Verticale Print-oriëntatie (Rechtop op de 60° Snijrand)**
   - Het 60° segment wordt **rechtop** geprint, rustend op het platte zijsnijvlak op de bouwplaat.
   - Hierdoor veranderen alle radiale bogen in **verticale wanden (90° t.o.v. de bouwplaat)**!
   - Er is nul overhang aanwezig in de rol-zone; de lagen stapelen zich exact horizontaal op met maximale laaghechting en 0% supportmateriaal.
   - Gebruik een 10mm brim of kleine hecht-tab op de montageflens voor stabiliteit op het printbed.

#### C. Materiaal & Printinstellingen
- **Materiaal:** **TPU (Shore 85A aanbevolen)** voor maximale flexibiliteit en lage $F_s$ (resonantiefrequentie); Shore 95A is tevens bruikbaar.
- **Printtemperatuur:** **245°C - 255°C** (voor 100% moleculaire laagfusiestrekte).
- **Wanddikte:** **0.8 mm tot 1.0 mm** (exact 2 perimeters bij een 0.4 mm nozzle).
- **Supports:** **0% (Disabled / Uitgeschakeld)**.
- **Flenzen:** 100% infill op de binnenste en buitenste montageflenzen (12-15 mm breed) voor een luchtdichte en stevige klem/lijmverbinding.

#### D. Printbed Segmentatie (256×256 mm Bed)
- **Aantal Segmenten:** **6 symmetrische segmenten van 60°**.
- **Maximale Span per Segment:** **~204.5 mm** (inclusief 12 mm overlappende lijmflappen).
- **Inpassing:** Past gemakkelijk diagonaal en gecentreerd op een **256×256 mm printbed** (zoals Bambu Lab X1/P1/A1 of Creality K1).

#### E. Montage & Verlijmingshandleiding (Lap Joint Method)
1. **Lijmflappen (Lap Joints):** Elk van de 6 segmenten is voorzien van een 12 mm overlappende rand (lap joint) aan de hoekuiteinden.
2. **Lijmkeuze:** Cyanoacrylaat (CA-lijm / Secondelijm) gecombineerd met een **TPU/Polyurethaan Activator/Primer**, óf elastische Polyurethaan contactlijm (bijv. Seam Grip / Stormsure).
3. **Voorbehandeling:** Schuur de contactoppervlakken licht op met p400 schuurpapier en ontvet grondig met isopropanol (IPA).
4. **Assemblage:**
   - Verlijm de 6 segmenten opeenvolgend in een houten of 3D-geprinte uitlijnmot (jig) tot een volledige ring van 385 mm.
   - Verlijm de binnenflens aan de 3D-geprinte conus met 2-componenten epoxy of CA-lijm.
   - Klem de buitenflens vast op de basket met de 3D-geprinte klemring en M3/M4 schroeven.

---

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

## 7. Schematische Overzichten & Visualisaties
1. **Motor Doorsnede:** Zie `motor_ontwerpen_vergelijking.png` voor de fysisch accurate doorsnede van de neodymium pot-motor inclusief de inwendige 50 mm ringvormige speling kamer.
2. **Surround & Printbed Layout:** Zie `surround_ontwerp_en_segmentatie.png` voor de profielvervorming van de High-Roll TPU surround bij ±50 mm uitslag en de inpassing van een 60° segment op een 256×256 mm printbed.
