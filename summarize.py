from flask import Flask, request, jsonify
import ollama

client = ollama.Client(
    host='http://ollama:11434/',  # Use the container name as the host
)


app = Flask(__name__)

template = """
fais moi un résumé du texte suivant en liste bullet pint en ne mettant que les informations importantes qui pourrait être utile à un médecin en faisant attention d'y mettre les informations suivantes 'traitement en cours, résultat d examen, antécédents perso et familiale, ' si elles sy trouvent 'Le cas présenté concerne un homme âgé de 61 ans (71 kg, 172 cm, soit un indice de masse corporelle de 23,9 kg/m²) admissible à une transplantation pulmonaire en raison d’une insuffisance respiratoire chronique terminale sur emphysème post-tabagique, sous oxygénothérapie continue (1 L/min) et ventilation non invasive nocturne. Il présente, comme principaux antécédents, une dyslipidémie, une hypertension artérielle et un tabagisme sevré estimé à 21 paquets-années (facteurs de risque cardiovasculaires). Le bilan préopératoire a révélé une hypertension artérielle pulmonaire essentiellement postcapillaire conduisant à l’ajout du périndopril (2 mg par jour) et du furosémide (40 mg par jour). La mise en évidence d’un Elispot (enzyme-linked immunospot) positif pour la tuberculose a motivé l’introduction d’un traitement prophylactique par l’association rifampicine-isoniazide (600-300 mg par jour) pour une durée de trois mois.

Deux mois après le bilan préopératoire, le patient a bénéficié d’une transplantation mono-pulmonaire gauche sans dysfonction primaire du greffon5,6. Le donneur et le receveur présentaient tous deux un statut sérologique positif pour cytomegalovirus (CMV) et Epstein Barr Virus (EBV). Une sérologie positive de la toxoplasmose a été mise en évidence uniquement chez le receveur. Le traitement immunosuppresseur d’induction associait la méthylprednisolone (500 mg à jour 0 et 375 mg à jour +1 post-transplantation) et le basiliximab, anticorps monoclonal dirigé contre l’interleukine-2 (20 mg à jour 0 et jour +4 posttransplantation). À partir de jour +2 post-transplantation, l’immunosuppression a été maintenue par une trithérapie par voie orale comprenant le tacrolimus à une posologie initiale de 5 mg par jour, le mofétil mycophénolate (MMF) 2000 mg par jour et la prednisone 20 mg par jour. Les traitements associés sont présentés dans le tableau I.

L’évolution est marquée par la survenue, au jour +5 posttransplantation, d’une dégradation respiratoire sur œdème pulmonaire gauche de reperfusion, avec possible participation cardiogénique. Le rejet aigu de grade III, évoqué par la présence d’infiltrats lymphocytaires aux biopsies transbronchiques, a été confirmé par l’anatomopathologie. Un traitement intraveineux par méthylprednisolone (1000 mg au jour 1, 500 mg au jour 2, 250 mg au jour 3 puis décroissance progressive par voie orale de la posologie de prednisone de 25 à 50 % tous les trois à quatre jours pour atteindre une posologie de 0,15 mg/kg/jour) a été mis en place. Les biopsies transbronchiques de contrôle, réalisées une semaine après le traitement, retrouvent un rejet non évolutif. La présence d’anticorps anti-HLA (antigènes des leucocytes humains) de type DSA (donor-specific antibody) a conduit à la mise en place d’un traitement immunomodulateur par immunoglobulines polyvalentes (1 g/kg/jour pendant deux jours tous les mois pendant trois mois). Sur le plan biologique, aucune anomalie cliniquement significative n’est mise en évidence, notamment en faveur d’une infection (réaction en chaîne par polymérase (PCR) EBV et CMV négatives, cultures microbiologiques du liquide bronchoalvéolaire stériles, protéine C réactive (CRP) à 9 mg/L, leucocytes à 4,5 G/L). Le suivi thérapeutique a mis en évidence une concentration résiduelle sanguine en tacrolimus infrathérapeutique, persistante depuis le début de la transplantation pulmonaire, malgré une adhésion thérapeutique optimale (Figure 1).

La polymédication des patients transplantés conduit à de nombreuses interactions médicamenteuses potentielles qu’il est important de déceler et de prendre en charge afin de maintenir l’efficacité clinique des traitements immunosuppresseurs.
'
"""

template2 = """
Une patiente âgée de 45 ans, sans antécédents pathologiques a présenté une symptomatologie faite de douleurs lombaires gauches, d'acouphènes, de palpitations, de céphalées et une hypersudation après chaque miction, sans troubles mictionnels ni hématurie.
A l'examen physique, nous avons trouvé une tension artérielle à 130/80 mmHg/ au repos, et 170/100 mm Hg immédiatement après miction. Le reste de l'examen somatique était normal. L'urographie intraveineuse (UIV) a montré une image lacunaire arrondie à contours réguliers faisant 2 cm de grand axe, au niveau du dôme vésical (Figure l). L'échographie sus-pubienne a montré une masse tissulaire du dôme vésical, faisant saillie dans la lumière, de 1,5 cm de diamètre.
L'imagerie par résonance magnétique (IRM) a mis en évidence, une formation arrondie de 17 mm de diamètre, bien limitée avec des contours réguliers, sans signes d'extension extravésicale. Des coupes réalisées sur les loges surrénaliennes ont conclu à l'intégrité des glandes surrénales (Figure 2).

Coupe frontale en pondération T1.

Coupe frontale en pondération T2 montre l'hypersignal de la tumeur.

Coupe sagittale en pondération T1, la tumeur a un signal intermédiaire.

Le diagnostic de phéochromocytome vésical a été suspecté, le dosage de l'acide vanyl-mandélique urinaire (VMA) était normal, le dosage des cathécholamines n'a pas été réalisé.

L'examen du fond de l'œil a révélé des artères rétrécies en rapport avec une hypertension artérielle mal tolérée, ainsi que des signes cicatriciels de choroïdopathie hypertensive en rapport avec des poussées hypertensives aiguës. La cystoscopie a montré une tumeur unique de 15 mm de diamètre environ, au niveau du bas fond vésical, arrondie et hypervascularisée à 3 cm en arrière de la barre interurétérale, recouverte par une muqueuse d'aspect macroscopique normal. La patiente a été opérée par une laparotomie médiane. Après une cystotomie longitudinale et repérage de la tumeur, sa base est clampée à 0,5 cm de la tumeur qui est réséquée au bistouri électrique. Il n'y a pas eu d'élévation de la tension artérielle lors de la mobilisation et de la résection de cette formation tumorale. Les suites opératoires ont été simples.

L'examen anatomo-pathologique de la pièce opératoire, coupée en deux, a montré deux petites formations ovoïdes distinctes de couleur chamois, faites de cellules à cytoplasme basophile finement granuleux, un noyau vésiculeux doté d'une chromatine fine et d'un nucléole, avec des limites cytoplasmiques nettes, les éléments tumoraux se disposaient en travées, en cordons et en structures alvéolaires au sein d'un stroma de type endocrinien riches en capillaires sinusoïdes.
L'évolution postopératoire a été favorable, avec un recul de 28 mois. La patiente est actuellement asymptomatique avec des chiffres tensionnels normaux et une urographie intraveineuse de contrôle normale.
"""

response_template = """
- Homme de 61 ans, 71 kg, 172 cm (IMC 23,9 kg/m²), admissible à une transplantation pulmonaire pour insuffisance respiratoire chronique sur emphysème post-tabagique.
- Antécédents personnels : dyslipidémie, hypertension artérielle, tabagisme sevré (21 paquets-années).
- Traitement en cours avant la transplantation : oxygénothérapie (1 L/min), ventilation non invasive nocturne, périndopril (2 mg/jour), furosémide (40 mg/jour), prophylaxie tuberculose par rifampicine-isoniazide (600-300 mg/jour).
- Résultat d’examen préopératoire : hypertension artérielle pulmonaire, Elispot positif pour tuberculose.
- Traitement post-transplantation :
  - Méthylprednisolone (500 mg à J0, 375 mg à J+1)
  - Basiliximab (20 mg à J0 et J+4)
  - Immunosuppression orale : tacrolimus (5 mg/jour), mycophénolate mofétil (MMF, 2000 mg/jour), prednisone (20 mg/jour).
- Complications post-transplantation : œdème pulmonaire gauche de reperfusion (J+5), rejet aigu de grade III confirmé.
- Traitement du rejet : méthylprednisolone IV (1000 mg J1, 500 mg J2, 250 mg J3) puis décroissance progressive de prednisone.
- Résultat de contrôle : rejet non évolutif, anticorps anti-HLA DSA présents.
- Traitement immunomodulateur : immunoglobulines polyvalentes (1 g/kg/jour, pendant 2 jours tous les mois pour 3 mois).
- Résultats d'examen : PCR EBV et CMV négatives, cultures microbiologiques stériles, CRP à 9 mg/L, leucocytes à 4,5 G/L.
- Suivi thérapeutique : concentration en tacrolimus infrathérapeutique malgré une adhésion optimale.
"""

response_template2 = """
- Patiente âgée de 45 ans, sans antécédents pathologiques.
- Symptômes : douleurs lombaires gauches, acouphènes, palpitations, céphalées, hypersudation après miction, sans troubles mictionnels ni hématurie.
- Tension artérielle : 130/80 mmHg au repos, 170/100 mmHg après miction.
- Résultat d'examen : 
  - UIV : image lacunaire arrondie à contours réguliers (2 cm) au dôme vésical.
  - Échographie : masse tissulaire du dôme vésical (1,5 cm).
  - IRM : formation arrondie (17 mm), bien limitée, sans signes d'extension extravésicale.
  - Cystoscopie : tumeur unique (15 mm), hypervascularisée, au bas fond vésical.
- Diagnostic suspecté : phéochromocytome vésical.
- Traitement en cours : opération par laparotomie médiane, résection de la tumeur sans élévation de la tension artérielle.
- Examen anatomo-pathologique : formations ovoïdes distinctes, cellules à cytoplasme basophile et noyau vésiculeux.
- Évolution postopératoire favorable, recul de 28 mois, patiente asymptomatique, chiffres tensionnels normaux, UIV de contrôle normale.
"""


#give a string that contains the text you want summarized, calls the model with 2 examples for context
def summarize_2ex(message, model):

    summary = client.chat(model=model, messages=[{"role": "user", "content": template},{"role": "assistant", "content": response_template},{"role": "user", "content": template2},{"role": "assistant", "content": response_template2},{"role": "user", "content": f"fais moi un résumé du texte suivant en liste bullet pint en ne mettant que les informations importantes qui pourrait être utile à un médecin en faisant attention d'y mettre les informations suivantes 'traitement en cours, résultat d examen, antécédents perso et familiale, ' si elles sy trouvent, précise que le résumé est généré par IA, présente le patient et le problème actuel, résume le cas suivant '{message}'"}])


    return summary['message']['content']


#give a string that contains the text you want summarized, calls the model with 1 examples for context
def summarize_1ex(message, model):

    summary = client.chat(model=model, messages=[{"role": "user", "content": template},{"role": "assistant", "content": response_template},{"role": "user", "content": f"fais moi un résumé du texte suivant en liste bullet pint en ne mettant que les informations importantes qui pourrait être utile à un médecin en faisant attention d'y mettre les informations suivantes 'traitement en cours, résultat d examen, antécédents perso et familiale, ' si elles sy trouvent, précise que le résumé est généré par IA, présente le patient et le problème actuel, résume le cas suivant '{message}'"}])


    return summary['message']['content']


# Flask route to expose the function
@app.route('/summarize_2ex', methods=['POST'])
def summarize2Ex():
    
    data = request.json
    
    message = data.get('message', '')
    model = data.get('model_name', '')
    

    result = summarize_2ex(message, model)

    if not result:
        return jsonify({'error': 'did not get result'}), 401
    return jsonify({'summary': result})

@app.route('/summarize_1ex', methods=['POST'])
def summarize1Ex():
    
    data = request.json
    
    message = data.get('message', '')
    message = data.get('message', '')
    model = data.get('model_name', '')
    

    result = summarize_1ex(message, model)

    if not result:
        return jsonify({'error': 'did not get result'}), 401
    return jsonify({'summary': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
