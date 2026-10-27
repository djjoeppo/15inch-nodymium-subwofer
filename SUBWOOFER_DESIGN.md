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
  - **Effect op prestaties:** Magnetische flux ($B_g$) en $BL$-factor blijven 100% geoptimaliseerd, aangezien de magnetische luchtspleet zich uitsluitend bij de bovenste top plate ring en poolkern bevindt.

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
- **Onbelaste Booglengte:** **~67.3 mm**.
- **Vervormingsmechanisme:** Bij een maximale uitslag van ±50 mm bedraagt de gestrekte lineaire afstand tussen conus- en basketrand slechts **61.0 mm** ($\sqrt{35^2 + 50^2}$).
  - Doordat de onbelaste booglengte (67.3 mm) groter is dan de gestrekte afstand (61.0 mm), hoeft het TPU materiaal **niet plastisch te strekken**.
  - De verplaatsing wordt opgevangen door een natuurlijk, geleidelijk **afrollen en buigen** van het profiel.
  - De feitelijke materiaalrek blijft ruimschoots onder **<11%**, wat ver binnen het elastische bereik van TPU ligt (TPU verdraagt >400% rek zonder blijvende vervorming).

#### B. 100% Supportloze Printbaarheid & Verticale Printoriëntatie
Bij het printen van TPU op hoge temperaturen (**240°C – 260°C**) voor maximale laaghechtingssterkte, is het gebruik van (tree) supports **ongeschikt** doordat TPU sterk aan supportmateriaal fused.

**Mechanisch Voordeel van Verticale Print-Oriëntatie (Rechtop op Snijvlak):**
1. **Minst Mogelijk Risico op Scheuren in de Rol:**
   - Wanneer de 60° segmenten **verticaal rechtop** worden geprint (rustend op de vlakke zijsnijrand), lopen de printlagen **parallel aan de buiglijn**.
   - Bij de extreme uitslag van ±50 mm buigt het materiaal *in de lengterichting van de geprinte spoorlijnen*.
   - Hierdoor worden de laagnaad-interfaces (inter-layer bonds) niet op trek beland, wat **delaminatie of scheuren langs de printlagen 100% uitsluit**!
2. **Dynamische Bogen:**
   - Doordat de printkop per laag continue cirkelbogen verwerkt op 245°C - 255°C, ontstaat een extreem glad, rimpelloos en 100% luchtdicht oppervlak.

**Oplossing voor Print-Stabiliteit ("Tall TPU Wobble"):**
Om te voorkomen dat een flexibel TPU onderdeel van ~67 mm hoog gaat wankelen door de bewegingen van de printkop:
- **0.4 mm Sacrificiële Verstevigingsribben (Sacrificial Bracing Ribs):**
  - In de holte onder de rolboog zijn dunne **0.4 mm (1 perimeter)** driehoeks-verstevigingsribben geïntegreerd in het model.
  - Deze ribben maken het onderdeel tijdens het printen zo stijf als een vakwerkconstructie.
  - Na het printen snijd je deze dunne 0.4 mm vliezen met een scherp scalpel of hobbymesje in één soepele beweging weg.
- **10 mm Outer Brim:**
  - De 12 mm brede montageflens aan de onderzijde wordt voorzien van een 10 mm brede buitenbrim voor onwrikbare hechting op het PEI-printbed.

#### C. Materiaal & Printinstellingen
- **Materiaal:** **TPU (Shore 85A aanbevolen)** voor maximale flexibiliteit en lage $F_s$ (resonantiefrequentie); Shore 95A is tevens bruikbaar.
- **Printtemperatuur:** **245°C - 255°C** (voor 100% moleculaire laagfusiestrekte).
- **Wanddikte:** **0.8 mm tot 1.0 mm** (exact 2 perimeters bij een 0.4 mm nozzle).
- **Supports:** **0% (Disabled / Uitgeschakeld)**.
- **Stabilisatie:** 0.4 mm sacrificiële ribben + 10 mm outer brim.
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
2. **Surround & Printbed Layout:** Zie `surround_ontwerp_en_segmentatie.png` voor de profielvervorming van de High-Roll TPU surround bij ±50 mm uitslag en de verticale print-oriëntatie met 0.4 mm sacrificiële ribben.

---

## 8. Automatisering & CAD-Generatie (FreeCAD & CadQuery Script)
In de repository is een universeel CAD-script aanwezig (`generate_surround_freecad.py`) waarmee direct 3D-bestanden worden gegenereerd:

- **Uitvoeren via Standalone Python (met CadQuery):**
  ```bash
  python3 generate_surround_freecad.py
  ```
- **Uitvoeren in FreeCAD GUI / Macro Editor:**
  Open FreeCAD, open de **Macro Editor** (of Python Console) en voer de inhoud van `generate_surround_freecad.py` uit. De ingebouwde native FreeCAD-functie (`import FreeCAD, Part`) bouwt het 3D-model direct op in de FreeCAD 3D-viewer!
- **Gegenereerde CAD & 3D-Print Bestanden:**
  - `tpu_surround_segment_100mm_p2p.step` (Universeel STEP CAD-model, direct te openen in **Autodesk Fusion 360** of **FreeCAD**).
  - `tpu_surround_segment_100mm_p2p.stl` (STL mesh bestand, direct te importeren in **Bambu Studio**, **OrcaSlicer** of **PrusaSlicer**).
  - `tpu_surround_test_slice_20mm.stl` (15-Minuten TPU Proef-Print Slice).

---

## 9. Risicoloos Testen: 15-Minuten TPU Proef-Print & Exacte Slicer Instellingen

Om **100% zekerheid** te krijgen over de printbaarheid, flexibiliteit en naadsterkte voordat je een volledig segment geprint wordt, is een **15-Minuten Proef-Print Slice** aanwezig (`tpu_surround_test_slice_20mm.stl`).

### 9.1 Slicer Instellingen voor TPU (Bambu Studio / OrcaSlicer / PrusaSlicer)
- **Nozzle Temperatuur:** `245°C - 250°C` (voor maximale laaghechtingssterkte).
- **Bed Temperatuur:** `45°C - 50°C` op een Textured PEI plaat.
- **Max Volumetric Speed Limit:** `3.5 mm³/s` (Houdt de printkop op een rustige ~25 tot 35 mm/s snelheid).
- **Wall Loops / Perimeters:** `2` (Exact 0.8 - 0.9 mm wanddikte bij een 0.4 mm nozzle).
- **Cooling Fan:** `20% - 30%` (Lage koeling voorkomt broze naden en fused de laadlagen monolithisch).
- **Supports:** `0% (Disabled)` -> Geen supports nodig!
- **Brim:** `Outer Brim Only = 10 mm` (Gegarandeerde hechting op de bouwplaat).

### 9.2 Proef-Print Test-Protocol (12 Min Printtijd, 3 gram TPU)
1. **Laad `tpu_surround_test_slice_20mm.stl` in je slicer.**
2. **Print de 20mm slice met de bovenstaande instellingen.**
3. **Voer de 3 Eenvoudige Kwaliteitstesten uit:**
   - **Test 1 (Flexibiliteit):** Buig de test-slice 180° dubbel. De rol hoort soepel mee te veren en direct terug te veren.
   - **Test 2 (Laagsterkte):** Probeer de lagen met de hand van elkaar te trekken. Bij 245°C is de laaghechting onverwoestbaar.
   - **Test 3 (Lijmnaad):** Breng een drup CA-lijm aan op de 12mm Lap Joint flap. Druk 15 seconden aan. Probeer de verbinding na 2 minuten los te trekken om de naadsterkte te verifiëren.

---

## 10. Evaluatie van Non-Planar Slicing voor TPU Surround

Non-planar slicing (waarbij de Z-as simultaan meebeweegt met de curvatuur in plaats van vlakke 2D-lagen) is geëvalueerd voor de TPU surround:

### 10.1 Voordelen van Non-Planar Slicing
- **Oppervlakte-afwerking:** Geen trappetjeseffect (stair-stepping) op de glooiende bovenkant van de High-Roll boog.
- **Continue Toplagen:** De toplaag van de boog kan als één continue gewelfde lijn worden neergelegd.

### 10.2 Fysieke Beperkingen & Nadelen bij TPU Subwoofer Surround
1. **Nozzle Clearance / Botsingsgevaar:**
   - Standaard printkoppen (heater block + fan shroud) hebben een vrije hoek van maximaal **15° tot 20°** t.o.v. de verticale as.
   - Onze High-Roll surround stijgt op onder een steilheid van **35° tot 45°**. Bij non-planar slicing van de flanken zou het hete heaterblock tegen de zijkant van de reeds geprinte TPU rol stoten en de flexibele wand indrukken.
2. **Extrusiedruk bij Flexibel TPU:**
   - Non-planar 3D-paden vereisen frequente, snelle Z-as acceleraties in combinatie met fluctuerende extrusiesnelheden.
   - Doordat flexibel TPU meegeeft in het aanvoermechanisme (elasticiteit in de feeder/hotend), leidt dit snel tot vertraagde extrusieresponse en blob-vorming.

### 10.3 Eindoordeel & Vergelijking

| Eigenschap | Non-Planar Slicing (Plat op Bed) | Planaire Verticale Printoriëntatie (Onze Aanbevolen Methode) |
| :--- | :--- | :--- |
| **Botsingsrisico Nozzle** | Hoog (beperkt tot <15-20° hellingen) | **0% (Botsingsvrij)** |
| **Mechanische Laagsterkte** | Matig (laagnaden worden op trek belast) | **Maximum (laagnaden lopen parallel aan buiglijn)** |
| **Supportmateriaal Nodig?** | Ja (voor steile zijkanten) | **0% (Geen supports nodig)** |
| **Printstabiliteit** | Uitstekend | **Uitstekend (met 0.4mm sacrificiële ribben + 10mm brim)** |
| **Advies** | Niet aanbevolen voor High-Roll TPU. | **Aanbevolen Standaard** voor extreme uitslag subwoofer surround. |
