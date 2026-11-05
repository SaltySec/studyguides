import json
from pathlib import Path

root=Path(__file__).parent
data=json.loads((root/'questions.json').read_text())
cards=data['cards']
questions=[]

def q(page,scope,stem,options,correct,why):
    assert len(options)==4 and 0<=correct<4
    card=next(c for c in cards if c['page']<=page<=c['end'])
    questions.append({'id':'v4q'+str(len(questions)), 'kind':'mcq',
       'cat':card['cat'],'page':page,'scope':scope,'prompt':stem,
       'options':options,'correct':correct,'rationale':why})

# Each distractor is a near threshold, a neighboring branch, or a plausible
# medication/route/interval from the same order. Page references are physical
# PDF pages in the user-supplied June 2024 edition.

q(14,'EMT/BLS','An adult has a regular pulse of 131/min, SBP 118, and no specific complaint. Which ALS-initiation trigger applies?',
  ['Pulse >130/min','Pulse >150/min','SBP <100 mmHg','No trigger without symptoms'],0,'The initiation order lists pulse <60 or >130, or irregularity, independent of complaint.')
q(14,'EMT/BLS','Which isolated adult SBP meets an ALS-initiation vital-sign trigger in this order?',
  ['90 mmHg','200 mmHg','201 mmHg','140 mmHg'],2,'Adult trigger is SBP <90 or >200; equality at 90 or 200 does not meet that threshold.')
q(14,'EMT/BLS','Once ALS care has begun, who must authorize a downgrade to BLS transport?',
  ['Receiving ED after arrival','Online Medical Direction','The transporting EMT alone','The patient after signing the PCR'],1,'The initiation-of-ALS order requires online Medical Direction to downgrade or discontinue ALS.')
q(19,'ALS awareness','What is the initial pediatric defibrillation energy in the dosing guide?',
  ['1 J/kg','2 J/kg','4 J/kg','6 J/kg'],1,'The energy guide gives initial pediatric defibrillation at 2 J/kg, followed by 4 J/kg.')
q(19,'ALS awareness','Which initial pediatric synchronized cardioversion setting appears in the energy guide?',
  ['0.5 J/kg','1 J/kg','2 J/kg','4 J/kg'],1,'The dosing guide lists 1 J/kg initial pediatric synchronized cardioversion.')
q(24,'EMT/BLS','A conscious late-pregnancy patient is unable to speak or cough after choking. Which maneuver does this adult order use?',
  ['Abdominal thrusts','Chest thrusts','Back blows alone','Blind finger sweep'],1,'The adult airway obstruction branch substitutes chest thrusts in late pregnancy or morbid obesity.')
q(25,'EMT/BLS','The adult wheezing patient already used a prescribed inhaler. Before assisting another use, what should the EMT establish?',
  ['Last time the inhaler was used','Whether a 12-lead shows STEMI','Whether SBP exceeds 140','Whether the patient is over 50'],0,'The BLS branch explicitly calls for determining time of last inhaler use and assisting if appropriate; further doses are at Medical Direction discretion.')
q(25,'EMT/BLS','Which nebulized albuterol dose is in the adult BLS wheezing branch, subject to system-specific procedure?',
  ['0.63 mg','1.25 mg','2.5 mg (3 mL)','5 mg (6 mL)'],2,'The adult BLS step lists albuterol 2.5 mg (3 mL) via nebulizer per system-specific procedure.')
q(25,'ALS awareness','Adult severe wheezing persists after epinephrine. Which magnesium regimen is listed?',
  ['1 g IV over 2 min','2 g IV infusion over 10 min','2 g IM once','4 g IV push over 1 min'],1,'The adult reactive lower airway order specifies 2 g in 50–100 mL D5W or NS infused over 10 minutes.')
q(26,'ALS awareness','Adult severe wheezing remains on CPAP and SBP falls to 98 mmHg. What does the order direct first?',
  ['Increase PEEP above 10','Lower PEEP','Give terbutaline by inline nebulizer','Maintain PEEP unchanged until SBP <90'],1,'For instability at SBP <100, lower PEEP; remove CPAP if worsening continues.')
q(26,'ALS awareness','Which patient requires Medical Direction contact before IM epinephrine for refractory adult wheezing?',
  ['Age 49 with no cardiac history','Age 51 with no cardiac history','Age 30 with no cardiac history','Age 18 with no cardiac history'],1,'The order calls for contact when age >50 and/or cardiac disease history.')
q(32,'ALS awareness','In unstable adult bradycardia, what atropine starting dose is specified?',
  ['0.1 mg IV/IO','0.5 mg IV/IO','1 mg IM','2 mg IV/IO'],1,'This June 2024 order lists atropine 0.5 mg rapid IV/IO.')
q(32,'ALS awareness','What is the adult atropine repeat interval and ceiling in this bradycardia order?',
  ['Every 2 min to 1 mg','Every 3–5 min to 3 mg','Every 5 min to 10 mg','One dose only'],1,'Atropine may repeat every 3–5 minutes up to 3 mg until pacing is available.')
q(32,'ALS awareness','The adult remains hypotensive and bradycardic after atropine. Which initial TCP rate is listed?',
  ['50/min','60/min','70/min','100/min'],2,'The order starts transcutaneous pacing at 70 beats/min under system procedure.')
q(39,'ALS awareness','Stable pulmonary edema, SBP 139 mmHg: which statement matches the first NTG step?',
  ['0.4 mg SL now because SBP >100','0.4 mg SL now because SBP ≥130','Do not give under the first-dose SBP >140 threshold','Give 0.8 mg SL instead'],2,'The initial stable pulmonary-edema NTG step requires SBP >140 mmHg.')
q(39,'ALS awareness','After the first NTG dose in stable pulmonary edema, what SBP threshold is used for repeat 0.4 mg SL doses?',
  ['>100 mmHg','≥120 mmHg','≥140 mmHg','>160 mmHg'],2,'This order uses >140 for the first dose and ≥140 for repeat doses every five minutes.')
q(39,'ALS awareness','CPAP in pulmonary edema requires respiratory distress plus how many additional listed criteria?',
  ['One','Two','Three','All five'],1,'The inclusion box requires respiratory distress and two or more listed findings.')
q(40,'ALS awareness','Pulseless torsades: what initial magnesium dose and route are listed?',
  ['1 g IM','2 g IV/IO over 2 min','2 g nebulized','4 g IV/IO over 10 min'],1,'The pulseless polymorphic VT order gives magnesium sulfate 2 g IV/IO diluted in 10 mL NS over two minutes.')
q(41,'ALS awareness','For regular adult SVT, which first two adenosine doses are listed?',
  ['3 then 6 mg rapid IV','6 then 12 mg rapid IV','12 then 12 mg IM','6 then 6 mg slow IV'],1,'The adult SVT order uses 6 mg then 12 mg rapid IV, each with a 10 mL saline flush.')
q(41,'ALS awareness','An adult tachycardia is narrow-complex but irregular. Which specific medication is cautioned against?',
  ['Adenosine','Magnesium sulfate','Atropine','Amiodarone'],0,'The SVT order cautions against adenosine for an irregular rapid rhythm.')
q(42,'EMT/BLS','Which SBP permits assisting an ACS patient with one prescribed 0.4 mg SL NTG self-dose, assuming no other contraindication?',
  ['110 mmHg','139 mmHg','140 mmHg','141 mmHg'],3,'The BLS ACS order requires SBP strictly >140 mmHg, prescribed NTG, and no maximum dose or contraindication.')
q(42,'EMT/BLS','In the BLS ACS order, which SBP is a reason to withhold assistance with prescribed NTG?',
  ['160 mmHg','180 mmHg','150 mmHg','110 mmHg'],3,'The June 2024 Region VIII BLS threshold is >140 mmHg; 110 does not qualify.')
q(42,'EMT/BLS','A patient took 162 mg aspirin four hours ago. What additional dose reaches the order’s 324 mg total in eight hours?',
  ['81 mg','162 mg','243 mg','324 mg'],1,'The ACS order allows giving aspirin to reach 324 mg total within the last eight hours.')
q(42,'EMT/BLS','The patient took 324 mg aspirin seven hours ago. Which aspirin choice follows the ACS order?',
  ['Give another 81 mg','Give another 162 mg','May omit additional aspirin','Repeat 324 mg now'],2,'Aspirin may be omitted after ≥324 mg within eight hours, absent another reason for treatment.')
q(42,'EMT/BLS','Which recent medication use requires withholding NTG under the ACS order?',
  ['Tadalafil 36 hours ago','Acetaminophen 36 hours ago','Albuterol 36 hours ago','Aspirin 36 hours ago'],0,'The ACS list includes tadalafil and several PDE-5/pulmonary-hypertension agents within 48 hours.')
q(42,'ALS awareness','For an ALS repeat NTG dose in stable ACS, what additional condition is required?',
  ['An IV established and SBP >140','An IV established and SBP >100','SBP ≥140 with no IV','A second aspirin dose'],0,'The repeat 0.4 mg SL dose after five minutes requires SBP >140 and established IV; the initial dose may precede IV.')
q(42,'ALS awareness','Inferior STEMI leads II, III, aVF: which drug does the ACS special-considerations box say to avoid?',
  ['Lidocaine','Aspirin','Normal saline','Albuterol'],0,'The order specifically cautions to avoid lidocaine in suspected inferior wall MI.')
q(43,'ALS awareness','Adult VF/pulseless VT: which antiarrhythmic is first-listed when available?',
  ['Lidocaine 1 mg/kg','Amiodarone 300 mg IV/IO','Magnesium 2 g IV/IO','Adenosine 6 mg IV'],1,'The order reserves lidocaine for when amiodarone is unavailable; initial amiodarone is 300 mg IV/IO.')
q(44,'ALS awareness','Adult VF remains after initial amiodarone. Which later amiodarone dose appears?',
  ['50 mg IV/IO','100 mg IV/IO','150 mg IV/IO','300 mg IV/IO again'],2,'The later repeat amiodarone dose is 150 mg IV/IO.')
q(47,'EMT/BLS','A COPD-history adult is breathing adequately with SpO₂ 89%. Which target is given in initial adult care?',
  ['About 88%','About 92%','100% for every patient','Withhold oxygen entirely'],1,'The adult initial-care oxygen table calls for titration around 92% for COPD/history of COPD.')
q(50,'ALS awareness','Adult non-anaphylactic reaction: what diphenhydramine regimen is listed?',
  ['25 mg PO q5 min','50 mg slow IV/IO/IM once','1 mg/kg IV up to 100 mg','50 mg rapid IV every 3 min'],1,'The non-anaphylaxis order lists diphenhydramine 50 mg slow IV/IO/IM for one dose.')
q(51,'EMT/BLS','Adult anaphylaxis: what can BLS give under the system protocol at Medical Control direction?',
  ['0.15 mg epinephrine IM once','0.3 mg epinephrine IM auto-injector once','0.3 mg epinephrine IV/IO once','0.5 mg epinephrine IM every 3 min'],1,'The BLS branch specifies one 0.3 mg IM 1:1,000 auto-injector dose at Medical Control direction.')
q(51,'ALS awareness','Anaphylactic shock with IV access: what epinephrine concentration and single-dose increment does this order use?',
  ['1:1,000; 0.3 mg IV','1:10,000; 0.1 mg slow IV/IO','1:10,000; 1 mg IV/IO','1:1,000; 0.15 mg IV'],1,'The hypotensive/shock ALS branch specifies 1:10,000 epinephrine 0.1 mg slow IV/IO q3 min, max total 0.5 mg.')
q(51,'ALS awareness','Adult anaphylaxis with SBP 94 and perfusion maintained: which ALS epinephrine route applies?',
  ['1:1,000 IM','1:10,000 IV/IO','1:1,000 IV push','1:10,000 nebulized'],0,'Normotensive branch (SBP ≥90) specifies 1:1,000, 0.3 mg IM, repeat once after three minutes if needed.')
q(51,'ALS awareness','In adult anaphylaxis, age 52 or cardiac disease history changes which step?',
  ['No epinephrine permitted','Contact Medical Direction before ALS epinephrine','Double diphenhydramine','Use 1:1,000 IV'],1,'Both ALS epinephrine branches call for prior Medical Direction contact for age >50 and/or cardiac disease.')
q(54,'EMT/BLS','An adult with glucose 60 mg/dL, alert and intact gag: does this order’s oral-glucose threshold apply?',
  ['Yes, because ≤60','No, because it requires <60','Yes, if the patient has a pump','No, because it requires <40'],1,'Adult oral glucose consideration uses glucose strictly below 60 mg/dL.')
q(54,'EMT/BLS','An adult with glucose 59 mg/dL is drowsy with no intact gag. What matters for oral glucose?',
  ['Glucose alone qualifies','Alertness and intact gag are also required','Only the presence of an insulin pump','Only SBP above 140'],1,'The adult BLS oral-glucose branch requires both alertness and intact gag reflex.')
q(54,'ALS awareness','Adult hypoglycemia with no IV/IO: which fallback medication and dose are listed?',
  ['Glucagon 1 mg IM once','Glucagon 0.5 mg IM once','D10 5 mL/kg orally','D50 25 g IM'],0,'No-IV/IO branch lists glucagon 1 mg IM once.')
q(54,'ALS awareness','During adult dextrose treatment, how often should blood glucose be reassessed at minimum?',
  ['Every 5 min','Every 10 min','Every 20 min','After arrival only'],1,'The adult order states at least every 10 minutes while dextrose is administered.')
q(57,'ALS awareness','Which minimum SBP permits considering the adult moderate/severe pain medication branch?',
  ['≥80 mmHg','≥90 mmHg','>100 mmHg','>140 mmHg'],1,'The adult pain order uses SBP ≥90 mmHg.')
q(57,'ALS awareness','What is the adult initial fentanyl dose and single-dose ceiling in this order?',
  ['0.5 mcg/kg, 50 mcg','1 mcg/kg, 100 mcg','2 mcg/kg, 200 mcg','1 mg/kg, 100 mg'],1,'Initial fentanyl is 1 mcg/kg IV/IO/IN, up to 100 mcg.')
q(57,'ALS awareness','If adult fentanyl is chosen for pain, what repeat dose is listed?',
  ['0.5 mcg/kg up to 50 mcg','1 mcg/kg up to 100 mcg','2 mcg/kg up to 200 mcg','No repeat under any circumstance'],0,'The repeat fentanyl dose is 0.5 mcg/kg IV/IO/IN up to 50 mcg.')
q(57,'ALS awareness','Which pain medication is reserved when fentanyl, ketamine, and morphine are unavailable?',
  ['Ketorolac','Morphine','Fentanyl','Midazolam'],0,'The adult pain table lists ketorolac only when the other three listed agents are unavailable.')
q(58,'ALS awareness','An actively seizing adult weighs 68 kg. What initial IN/IM midazolam dose appears?',
  ['2 mg','2.5 mg','5 mg','10 mg'],1,'Adult IN/IM table uses 2.5 mg for weight <70 kg.')
q(58,'ALS awareness','An actively seizing adult weighs exactly 70 kg. What IN/IM midazolam dose appears?',
  ['2 mg','2.5 mg','5 mg','10 mg'],2,'The adult IN/IM branch uses 5 mg for ≥70 kg.')
q(58,'ALS awareness','What is the adult IV/IO midazolam pattern for active seizure?',
  ['2 mg every 2 min to 10 mg total','2 mg every 5 min to 4 mg total','5 mg every 2 min to 20 mg total','0.1 mg/kg IM only'],0,'The adult order lists 2 mg IV/IO increments every two minutes to a maximum total of 10 mg.')
q(59,'EMT/BLS','Adult suspected infection with HR 110 and SBP 100 has what shock index?',
  ['0.91','1.0','1.1','1.2'],2,'Shock index is HR ÷ SBP = 110 ÷ 100 = 1.1; ≥1 is one listed adult sepsis criterion.')
q(59,'EMT/BLS','Which adult sepsis screening combination can satisfy the two-criterion rule without fever?',
  ['HR 91 and shock index 1.05','HR 90 and shock index 0.99','HR 91 alone','Temperature 98.6°F alone'],0,'Adult suspected infection requires two listed criteria; HR >90 and shock index ≥1 qualify even without abnormal temperature.')
q(59,'ALS awareness','In adult suspected sepsis, at which SBP does this order call for saline via pressure bag?',
  ['<90 mmHg','<100 mmHg','<110 mmHg','<120 mmHg'],3,'The adult sepsis fluid step is triggered below SBP 120 mmHg.')
q(62,'ALS awareness','Stable suspected hyperkalemia with peaked T waves: which bicarbonate dose is listed?',
  ['0.5 mEq/kg up to 25 mEq','1 mEq/kg up to 50 mEq','50 mEq every 3 min','No bicarbonate until arrest'],1,'The peaked-T branch gives sodium bicarbonate 8.4% 1 mEq/kg IV/IO, up to 50 mEq.')
q(62,'ALS awareness','Unstable suspected hyperkalemia with wide QRS: which nebulized albuterol dose is listed?',
  ['2.5 mg (3 mL)','5 mg (6 mL)','10 mg (12 mL)','0.63 mg'],1,'The unstable branch lists albuterol 5 mg (6 mL), may repeat once, with 50 mEq sodium bicarbonate.')
q(64,'ALS awareness','Unstable beta blocker overdose with bradycardic hypoperfusion: which medication is listed?',
  ['Glucagon 1 mg slow IV, may repeat once','Calcium chloride 1 g IV once','Atropine 0.5 mg IM twice','Dextrose 25 g IV only'],0,'The beta blocker overdose ALS branch gives glucagon 1 mg slow IV with one repeat permitted.')
q(65,'ALS awareness','Unstable calcium-channel blocker overdose with bradycardic hypoperfusion: what is this edition’s initial listed medication?',
  ['Glucagon 1 mg slow IV','Glucagon 5 mg IM','Calcium gluconate 3 g IV','Dopamine 20 mcg/kg/min'],0,'The calcium-channel blocker overdose order lists glucagon 1 mg slow IV, may repeat once.')
q(68,'ALS awareness','Adult cyanide exposure: which hydroxocobalamin regimen is listed?',
  ['2.5 g over 5 min','5 g over 15 min','70 mg/kg over 2 min without cap','10 g IV push'],1,'The adult cyanide order specifies hydroxocobalamin 5 g over 15 minutes through a dedicated IV line.')
q(68,'ALS awareness','Which IV setup is required for adult hydroxocobalamin?',
  ['Piggyback into an existing line','Dedicated IV line, not piggyback','Oral administration only','IO only, never IV'],1,'The cyanide order requires its own dedicated IV line; no existing IV or piggyback infusion.')
q(69,'ALS awareness','Unstable cyclic-antidepressant overdose with wide QRS: which bicarbonate dose is listed?',
  ['0.5 mEq/kg max 25 mEq','1 mEq/kg max single 50 mEq','50 mEq IM','2 mEq/kg with no ceiling'],1,'The order gives sodium bicarbonate 8.4% 1 mEq/kg IV/IO, maximum single dose 50 mEq, with saline bolus.')
q(72,'EMT/BLS','Adult opioid exposure with adequate breathing: which BLS approach appears before any naloxone trigger?',
  ['2 mg IN naloxone regardless','Side position and vital-sign monitoring','12 mg IN immediately','0.1 mg/kg IV'],1,'When breathing is adequate, place on side and monitor; naloxone is tied to inadequate breathing or apnea.')
q(72,'EMT/BLS','Adult apnea after opioid exposure: what BLS intranasal naloxone interval and ceiling are listed?',
  ['2 mg every 1 min to 6 mg','2 mg every 2 min to 12 mg','4 mg every 5 min to 8 mg','1 mg every 3 min to 10 mg'],1,'The adult BLS order lists 2 mg IN every two minutes, up to 12 mg, while supporting ventilation.')
q(72,'EMT/BLS','Which breathing finding meets the opioid order’s definition of inadequate respirations?',
  ['Rate 12/min, EtCO₂ 40','Rate 10/min, EtCO₂ 40','Rate 9/min, EtCO₂ 40','Rate 14/min, EtCO₂ 45'],2,'The note defines inadequate as rate <10, EtCO₂ <30, or EtCO₂ >50; exactly 10 does not meet the rate threshold.')
q(72,'EMT/BLS','Which EtCO₂ reading alone meets the opioid order’s inadequate-respiration definition?',
  ['30 mmHg','40 mmHg','50 mmHg','51 mmHg'],3,'The note uses EtCO₂ <30 or >50 mmHg, so 51 meets it while 30 and 50 do not.')
q(74,'ALS awareness','Diphenhydramine overdose with wide QRS and hypoperfusion: which antidysrhythmic therapy is listed?',
  ['Sodium bicarbonate 8.4% 1 mEq/kg, max 50 mEq','Adenosine 6 mg rapid IV','Amiodarone 300 mg IV','Magnesium sulfate 4 g IM'],0,'The sodium-channel blocker order lists 1 mEq/kg sodium bicarbonate IV/IO, max single 50 mEq, plus saline.')

q(75,'EMT/BLS','A severely hypothermic adult appears pulseless. How long does the cold-emergency order allow for a pulse check?',
  ['10 seconds','20 seconds','30–60 seconds','Two full minutes'],2,'The hypothermia order allows a 30–60-second pulse check before deciding there is no pulse.')
q(78,'EMT/BLS','Adult heat emergency with glucose 59 mg/dL: which parallel protocol becomes relevant?',
  ['Adult diabetic/glucose emergencies','Adult ACS only','Adult bradydysrhythmias only','Adult burn transport'],0,'The heat order directs treatment under adult diabetic/glucose emergencies when glucose is <60 mg/dL.')
q(80,'EMT/BLS','After a snakebite, transport exceeds what duration before specialty transport should be considered?',
  ['10 minutes','15 minutes','25 minutes','30 minutes'],1,'Adult snakebite order says consider specialty transport when transport time >15 minutes.')
q(83,'EMT/BLS','A red-criteria trauma patient has an adequate airway; Level I travel is 26 minutes. What does the bypass time rule say absent approval?',
  ['Level I automatically','Closest appropriate facility/Level II','Wait for a helicopter regardless of time','Burn center automatically'],1,'Region VIII trauma bypass generally limits Level I travel to 25 minutes without Medical Direction approval.')
q(84,'EMT/BLS','A trauma patient meets Level I criteria but the airway cannot be adequately maintained. What destination instruction takes precedence?',
  ['Closest comprehensive emergency department','Level I regardless of airway','Any facility chosen by family','Remain on scene for a full assessment'],0,'The transport order directs the closest comprehensive ED when an adequate airway cannot be established/maintained.')
q(90,'ALS awareness','Adult hemorrhagic shock without signs of head injury: which SBP is the fluid target?',
  ['70 mmHg','90 mmHg','110 mmHg','140 mmHg'],1,'The adult hemorrhagic shock order targets SBP 90 mmHg; suspected head injury changes the target to 110.')
q(90,'ALS awareness','Adult hemorrhagic shock with suspected head injury: which SBP target replaces the usual trauma target?',
  ['90 mmHg','100 mmHg','110 mmHg','140 mmHg'],2,'The order raises the fluid target to SBP 110 mmHg when head-injury signs are present.')
q(91,'ALS awareness','Severe adult head injury with herniation signs: what EtCO₂ target is in the order?',
  ['20 mmHg','30 mmHg','40 mmHg','50 mmHg'],1,'The head-injury order uses a target EtCO₂ around 30 mmHg when signs of herniation are present.')
q(95,'EMT/BLS','After sealing an open chest wound, ventilation deteriorates. What action is specified?',
  ['Lift/remove the dressing briefly to release trapped air','Leave the seal untouched','Add a second fully occlusive layer','Start oral fluids'],0,'The adult thoracic injury order calls for lifting/removing the dressing if the patient worsens.')
q(96,'EMT/BLS','Which care for abdominal evisceration follows the adult order?',
  ['Replace tissue, then cover dry','Saline-moistened sterile dressing and occlusive covering without replacement','Firm direct pressure directly on exposed bowel','Leave exposed until surgical arrival'],1,'The order calls for saline-moistened sterile dressing and occlusive layer; do not replace organs.')
q(105,'ALS awareness','Adult burns requiring fluid resuscitation: what starting saline rate is listed?',
  ['125 mL/hr','250 mL/hr','500 mL/hr','1,000 mL/hr'],2,'The adult general burns order lists normal saline at 500 mL/hr for fluid resuscitation.')
q(106,'EMT/BLS','What is the adult burn-center direct-transport time limit, absent Medical Direction exception?',
  ['15 min','20 min','25 min','30 min'],2,'The adult burn transport guideline uses <25 minutes to a burn center under its criteria.')
q(108,'EMT/BLS','Chemical skin burn without water-reactive concern: what irrigation goal is specified?',
  ['At least 5 min','At least 10 min','At least 20 min','At least 30 min'],3,'The chemical-burn order calls for copious irrigation for a goal of at least 30 minutes, continued during transport.')
q(111,'EMT/BLS','A fresh thermal burn occurred 10 minutes ago. For how long at most should the area be cooled?',
  ['Five minutes','Ten minutes','Fifteen minutes','Thirty minutes'],0,'The adult thermal-burn order limits cooling to five minutes if the injury occurred within 15 minutes.')
q(114,'EMT/BLS','An adult MCI patient starts breathing after airway repositioning. Which triage framework is used?',
  ['START','JumpSTART','APGAR','VAN'],0,'The adult MCI diagram is START; pediatric patients use JumpSTART.')
q(115,'EMT/BLS','A child remains apneic after opening the airway in MCI triage. What pediatric-specific step follows?',
  ['Rescue breaths under JumpSTART','Immediate 12-lead ECG','Aspirin 324 mg','Skip further assessment'],0,'JumpSTART includes rescue breathing before the final apnea determination.')
q(120,'EMT/BLS','After delivery, what interval is given for expected placenta delivery?',
  ['5–10 min','10–15 min','20–30 min','60–90 min'],2,'The postpartum childbirth phase says the placenta should deliver in 20–30 minutes.')
q(120,'EMT/BLS','What estimated postpartum blood-loss threshold activates the hemorrhage actions in the childbirth order?',
  ['>250 mL','>500 mL','>750 mL','>1,000 mL'],1,'The postpartum phase calls out estimated blood loss >500 mL.')
q(125,'ALS awareness','Preeclampsia with qualifying severe findings: what magnesium regimen is listed?',
  ['2 g infusion over 10 min','2 g IV push over 2 min','4 g infusion over 30 min','1 g IM every 5 min'],0,'The preeclampsia order gives magnesium sulfate 2 g in 50–100 mL D5W/NS over ten minutes.')
q(126,'ALS awareness','Eclampsia: what magnesium regimen distinguishes it from the preeclampsia infusion?',
  ['2 g IV/IO over 2 min, may repeat once','2 g IV/IO over 10 min only','0.5 g IM every 5 min','4 g SL once'],0,'The eclampsia order gives 2 g IV/IO over two minutes, may repeat once to 4 g total.')
q(131,'ALS awareness','A 28-kg child remains in severe asthma distress. What epinephrine IM dose is in the pediatric order?',
  ['0.15 mg','0.3 mg','0.5 mg','1 mg'],0,'Pediatric reactive lower airway order uses 0.15 mg IM for <30 kg and 0.3 mg for ≥30 kg.')
q(131,'ALS awareness','What is the maximum pediatric magnesium sulfate dose for severe reactive lower airway disease?',
  ['1 g','2 g','4 g','25 g'],1,'The pediatric asthma order uses 25 mg/kg IV/IO over ten minutes with a maximum of 2 g.')
q(132,'EMT/BLS','A child in respiratory arrest has HR 55/min after effective ventilation. Which order should you enter?',
  ['Pediatric bradydysrhythmias','Pediatric narrow-complex tachycardia','Pediatric opioid overdose regardless of exposure','Pediatric burns'],0,'The pediatric respiratory-arrest order directs bradydysrhythmias when HR <60.')
q(135,'EMT/BLS','For a pulseless infant under one year, only an adult AED is available. Which approach matches the SMO?',
  ['Use AED with pads arranged not to overlap','Withhold all AED use under age one','Overlap pads to fit chest','Use AED only after five rounds of CPR'],0,'Pediatric capability is preferred, but the order allows an AED with careful non-overlapping pad placement.')
q(138,'EMT/BLS','A child remains at HR 58/min with hypoperfusion after effective oxygenation and ventilation. What action is indicated?',
  ['Begin CPR','Observe until HR <40','Give atropine before compressions','Treat as stable bradycardia'],0,'The pediatric bradycardia order starts CPR when HR remains <60 with hypoperfusion despite adequate ventilation.')
q(138,'ALS awareness','Pediatric atropine for vagal/primary AV block: what IV/IO dose is listed?',
  ['0.01 mg/kg','0.02 mg/kg','0.1 mg/kg','0.2 mg/kg'],1,'The pediatric bradycardia order lists atropine 0.02 mg/kg IV/IO.')
q(138,'ALS awareness','What is the pediatric atropine minimum single dose?',
  ['0.02 mg','0.05 mg','0.1 mg','0.5 mg'],2,'The atropine box gives a 0.1 mg minimum, 0.5 mg max single dose.')
q(138,'ALS awareness','For pediatric cardiopulmonary compromise, which epinephrine IV/IO dose is listed?',
  ['0.001 mg/kg','0.01 mg/kg','0.1 mg/kg','1 mg/kg'],1,'Pediatric bradycardia lists 1:10,000 epinephrine 0.01 mg/kg (0.1 mL/kg) IV/IO.')
q(140,'ALS awareness','Pediatric narrow-complex tachycardia: a 10-month-old has HR 221/min. Which age-specific rate threshold is crossed?',
  ['>150/min','>180/min','>200/min','>220/min'],3,'The pediatric order uses >220/min under age one and >180/min for ages one through 15.')
q(140,'ALS awareness','What is the first pediatric adenosine dose for narrow-complex tachycardia?',
  ['0.05 mg/kg max 3 mg','0.1 mg/kg max 6 mg','0.2 mg/kg max 12 mg','0.3 mg/kg max 18 mg'],1,'The first dose is 0.1 mg/kg rapid IV/IO, maximum 6 mg, followed by saline flush.')
q(140,'ALS awareness','What is the pediatric second adenosine dose and maximum?',
  ['0.1 mg/kg max 6 mg','0.2 mg/kg max 12 mg','0.3 mg/kg max 18 mg','1 mg/kg max 20 mg'],1,'The next pediatric adenosine dose is 0.2 mg/kg, maximum 12 mg.')
q(142,'ALS awareness','Pediatric VF/pulseless VT: which shock sequence appears?',
  ['1 then 2 J/kg','2 then 4 J/kg','4 then 6 J/kg','2 then 10 J/kg'],1,'The pediatric VF/VT order begins at 2 J/kg, then 4 J/kg.')
q(142,'ALS awareness','Pediatric VF/pulseless VT: what amiodarone dose is listed?',
  ['1 mg/kg','3 mg/kg','5 mg/kg','10 mg/kg'],2,'The order lists amiodarone 5 mg/kg IV/IO for shockable pulseless arrest, up to three doses.')
q(144,'ALS awareness','Pediatric wide-complex tachycardia with pulse: which initial synchronized cardioversion energy is listed?',
  ['0.5 J/kg','1 J/kg','2 J/kg','4 J/kg'],1,'The pediatric wide-complex tachycardia order uses 1 J/kg initially.')
q(145,'EMT/BLS','A patient is exactly 15 years old. Which initial-care pathway applies in this edition unless an order specifies otherwise?',
  ['Pediatric','Adult','Newborn','Only by Medical Direction'],0,'The pediatric initial medical care order includes patients through age 15.')
q(145,'ALS awareness','Pediatric nausea treatment at 39 kg: which ondansetron option is listed?',
  ['2 mg slow IV once','4 mg ODT once','4 mg IV plus 4 mg ODT','No ondansetron under 40 kg'],0,'Under 40 kg, pediatric initial care lists 2 mg slow IV once with no repeat dose.')
q(145,'ALS awareness','Pediatric nausea treatment at exactly 40 kg: which ondansetron option is listed?',
  ['2 mg IV','4 mg slow IV or 4 mg ODT once','8 mg IV','No ondansetron at 40 kg'],1,'At ≥40 kg, the order lists 4 mg slow IV or 4 mg ODT once, no repeat.')
q(146,'ALS awareness','Pediatric non-anaphylactic allergy: what diphenhydramine dose and ceiling are listed?',
  ['0.5 mg/kg max 25 mg','1 mg/kg max 50 mg','2 mg/kg max 100 mg','50 mg regardless of weight'],1,'The pediatric order uses diphenhydramine 1 mg/kg IM or slow IV, maximum 50 mg.')
q(147,'EMT/BLS','Pediatric anaphylaxis at 29 kg: what auto-injector dose is listed?',
  ['0.1 mg','0.15 mg','0.3 mg','0.5 mg'],1,'Pediatric BLS auto-injector dose is 0.15 mg below 30 kg.')
q(147,'EMT/BLS','Pediatric anaphylaxis at exactly 30 kg: what auto-injector dose is listed?',
  ['0.1 mg','0.15 mg','0.3 mg','0.5 mg'],2,'Pediatric BLS auto-injector dose is 0.3 mg at ≥30 kg.')
q(147,'ALS awareness','Pediatric anaphylaxis with IV/IO: what saline bolus is first listed?',
  ['10 mL/kg','20 mL/kg','30 mL/kg','60 mL/kg as a single bolus'],1,'The pediatric anaphylaxis IV/IO branch begins with normal saline 20 mL/kg, repeatable to 60 mL/kg total.')
q(147,'ALS awareness','Pediatric anaphylaxis without IV/IO access: what epinephrine route/dose is listed?',
  ['1:1,000 0.01 mg/kg IM, max 0.3 mg','1:10,000 0.1 mg/kg IV','1:1,000 0.1 mg/kg IM, max 1 mg','1:10,000 0.01 mg/kg nebulized'],0,'The IM branch uses 1:1,000 epinephrine 0.01 mg/kg IM, max 0.3 mg.')
q(149,'ALS awareness','Pediatric hypoglycemia: which glucose value triggers the dextrose treatment branch?',
  ['<40 mg/dL','<60 mg/dL','≤60 mg/dL','≤70 mg/dL'],2,'Pediatric diabetic/glucose emergencies uses glucose ≤60 mg/dL for its ALS treatment branch.')
q(149,'ALS awareness','Pediatric D10 for glucose ≤60: what dose and maximum are listed?',
  ['2 mL/kg max 10 g','5 mL/kg (0.5 g/kg) max 25 g','10 mL/kg max 50 g','25 g for every child'],1,'D10 is 5 mL/kg (0.5 g/kg) up to 25 g, may repeat once after five minutes if needed.')
q(149,'ALS awareness','Without IV/IO, a 7-year-old with glucose ≤60 gets which glucagon IM dose?',
  ['0.25 mg','0.5 mg','1 mg','2 mg'],1,'Pediatric no-IV/IO branch gives 0.5 mg IM at age ≤8 years; >8 years gets 1 mg.')
q(149,'ALS awareness','Without IV/IO, a 9-year-old with glucose ≤60 gets which glucagon IM dose?',
  ['0.25 mg','0.5 mg','1 mg','2 mg'],2,'Pediatric no-IV/IO branch gives 1 mg IM above age eight.')
q(149,'ALS awareness','D10 is unavailable for a 6-year-old. Which dextrose alternative is listed?',
  ['D12.5% 2 mL/kg','D25% 2 mL/kg','D50% 25 g slow push','D5% 10 mL/kg'],1,'Age one through eight uses D25% 2 mL/kg when D10 is unavailable.')
q(149,'ALS awareness','D10 is unavailable for an infant younger than one year. Which dextrose alternative is listed?',
  ['D12.5% 2 mL/kg','D25% 2 mL/kg','D50% 25 g','D10% 25 g'],0,'For age <1 year, the pediatric alternative table uses D12.5% 2 mL/kg.')
q(151,'ALS awareness','A child in hypovolemic shock remains poorly perfused after the first fluid bolus. Which repeat pattern is listed?',
  ['10 mL/kg once only','20 mL/kg boluses up to 60 mL/kg total','30 mL/kg boluses to 90 mL/kg','500 mL regardless of weight'],1,'The pediatric hypovolemic shock order uses 20 mL/kg, repeatable twice to 60 mL/kg total.')
q(153,'ALS awareness','Severe pain in an 8-year-old: which minimum SBP satisfies the medication branch?',
  ['70 mmHg','80 mmHg','86 mmHg','90 mmHg'],2,'The pediatric pain threshold is SBP ≥70 + 2×age = 86 mmHg for age eight.')
q(153,'ALS awareness','What initial pediatric fentanyl dose and maximum are listed?',
  ['0.5 mcg/kg max 50 mcg','1 mcg/kg max 100 mcg','2 mcg/kg max 200 mcg','0.1 mg/kg max 10 mg'],1,'The pediatric pain order lists fentanyl 1 mcg/kg IV/IO/IN, up to 100 mcg; repeat requires Medical Direction.')
q(153,'ALS awareness','After one pediatric fentanyl dose, what is required for a repeat?',
  ['Automatic repeat in 2 min','Automatic repeat in 5 min','Contact Medical Direction','Switch to morphine without approval'],2,'The pediatric pain order requires Medical Direction for either fentanyl or morphine repeat.')
q(154,'ALS awareness','A seizing 65-kg child receives IN midazolam. What maximum single dose is listed for this weight bracket?',
  ['2 mg','2.5 mg','5 mg','10 mg'],1,'The pediatric IN/IM box caps single doses at 2.5 mg below 70 kg.')
q(154,'ALS awareness','A seizing child weighs 70 kg. What IN/IM midazolam maximum single dose applies?',
  ['2 mg','2.5 mg','5 mg','10 mg'],2,'The pediatric IN/IM maximum single dose becomes 5 mg at ≥70 kg.')
q(154,'ALS awareness','Pediatric IV/IO midazolam for active seizure: what dose and single-dose cap are listed?',
  ['0.05 mg/kg max 1 mg','0.1 mg/kg max 2 mg','0.2 mg/kg max 5 mg','1 mg/kg max 10 mg'],1,'The pediatric seizure order uses 0.1 mg/kg IV/IO, max single 2 mg, with one repeat after five minutes.')
q(155,'EMT/BLS','Pediatric suspected sepsis: which finding must be among the two qualifying screening criteria?',
  ['Abnormal temperature','Shock index ≥1','A positive VAN screen','SBP below 120'],0,'Unlike the adult screen, pediatric sepsis requires abnormal temperature as one of at least two criteria.')
q(155,'EMT/BLS','A child has suspected infection, temperature exactly 100.4°F and age-specific tachycardia. Does temperature qualify?',
  ['No; fever must exceed 101°F','Yes; ≥100.4°F qualifies','Only if glucose <60','Only if EtCO₂ <20'],1,'Pediatric sepsis includes temperature ≥100.4°F or ≤96.8°F.')
q(155,'ALS awareness','Pediatric sepsis with SBP below age threshold: what initial fluid bolus is listed?',
  ['10 mL/kg','20 mL/kg','30 mL/kg','60 mL/kg at once'],1,'The sepsis order lists normal saline 20 mL/kg IV/IO, repeatable to 60 mL/kg total.')
q(159,'EMT/BLS','A child has smoke exposure and SpO₂ 99% by ordinary pulse oximeter. What does the CO order imply?',
  ['CO ruled out','CO still possible because conventional oximetry is unreliable','Only cyanide can remain','No oxygen needed'],1,'Conventional SpO₂ cannot reliably exclude carbon monoxide exposure.')
q(161,'ALS awareness','Pediatric cyanide exposure: what hydroxocobalamin dose and ceiling are listed?',
  ['25 mg/kg max 2 g','50 mg/kg max 4 g','70 mg/kg max 5 g','100 mg/kg max 10 g'],2,'The pediatric cyanide order uses 70 mg/kg, maximum 5 g.')
q(162,'ALS awareness','Pediatric cyclic antidepressant overdose with wide QRS: what bicarbonate dose is listed?',
  ['0.5 mEq/kg','1 mEq/kg','2 mEq/kg','50 mEq per child regardless of weight'],1,'The pediatric cyclic antidepressant order lists sodium bicarbonate 8.4% 1 mEq/kg IV.')
q(164,'EMT/BLS','Pediatric opioid exposure with adequate breathing: what is the BLS naloxone decision?',
  ['Give 2 mg IN solely for exposure','Monitor and support; naloxone is for inadequate breathing/apnea','Give 0.1 mg/kg IV','Give 12 mg IN immediately'],1,'The pediatric BLS order ties 2 mg IN naloxone to inadequate breathing or apnea.')
q(164,'EMT/BLS','Pediatric opioid exposure with apnea: what BLS IN dose is listed before calling about additional doses?',
  ['0.15 mg','0.3 mg','2 mg','4 mg'],2,'Pediatric BLS lists naloxone 2 mg IN; contact Medical Direction if additional doses are needed.')
q(164,'ALS awareness','A 15-kg child has inadequate respirations after opioid exposure. What ALS naloxone initial dose follows the weight rule?',
  ['0.1 mg/kg','0.2 mg/kg','2 mg fixed','4 mg fixed'],0,'For <20 kg, the ALS branch gives naloxone 0.1 mg/kg IV/IO/IN, max single dose 2 mg.')
q(164,'ALS awareness','A 20-kg child has apnea from opioid exposure. Which ALS initial naloxone dose applies?',
  ['0.1 mg/kg','1 mg fixed','2 mg IV/IO/IN','4 mg IM'],2,'At ≥20 kg, the pediatric ALS branch uses 2 mg IV/IO/IN, repeating q1–2 minutes up to 12 mg total.')
q(175,'EMT/BLS','A child meets red trauma criteria, adequate airway, Level I travel 27 minutes. What is the usual destination rule absent approval?',
  ['Level I automatically','Closest appropriate facility/Level II','Nearest burn center','No transport until a pediatric team arrives'],1,'Pediatric trauma bypass generally limits direct Level I travel to 25 minutes without Medical Direction approval.')
q(180,'ALS awareness','Pediatric hemorrhagic shock: what saline bolus and maximum total are listed?',
  ['10 mL/kg, max 30 mL/kg','20 mL/kg, max 60 mL/kg','30 mL/kg, max 90 mL/kg','500 mL, no repeats'],1,'The pediatric order uses 20 mL/kg boluses, repeated twice if needed to 60 mL/kg total.')
q(194,'ALS awareness','For a burned child aged five with >20% TBSA burns, which starting saline rate is listed?',
  ['125 mL/hr','250 mL/hr','500 mL/hr','1,000 mL/hr'],0,'Pediatric general burns uses 125 mL/hr for age ≤5.')
q(194,'ALS awareness','For a burned child aged ten with >20% TBSA burns, which starting saline rate is listed?',
  ['125 mL/hr','250 mL/hr','500 mL/hr','1,000 mL/hr'],1,'Pediatric general burns uses 250 mL/hr for age 6–12.')
q(194,'ALS awareness','For a burned adolescent aged 13 with >20% TBSA burns, which starting saline rate is listed?',
  ['125 mL/hr','250 mL/hr','500 mL/hr','1,000 mL/hr'],2,'Pediatric general burns uses 500 mL/hr for age ≥13.')
q(195,'EMT/BLS','A burned child weighs 28 kg and has a secure airway. What special destination consideration is listed?',
  ['Consider burn-center bypass even without another listed criterion','Never consider bypass under 30 kg','Only adult Level I trauma center','Treat weight alone as a prohibition'],0,'The pediatric burn transport order specifically notes consideration of burn-center bypass for patients <30 kg.')
q(197,'EMT/BLS','A child’s chemical burn is being irrigated safely. What minimum continuous-irrigation goal appears?',
  ['10 min','20 min','30 min','60 min'],2,'Pediatric chemical-burn order aims for at least 30 minutes of continuous irrigation.')

assert len(questions)>=130,len(questions)
data['cases']=questions
(root/'questions_v4.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')))
print('curated scenarios',len(questions),'medication-related',sum(any(w in x['prompt'].lower() for w in ['mg','mcg','dose','ntg','nitro','epinephrine','naloxone','albuterol','dextrose','glucagon','fentanyl','midazolam','aspirin','atropine','magnesium','bicarbonate','adenosine','saline','ondansetron','hydroxocobalamin']) for x in questions))
