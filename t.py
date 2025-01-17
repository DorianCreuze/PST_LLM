import requests
import json

# Define the server endpoint and the message
url = "http://localhost:5000/summarize_2ex"
data = {
    "message": """Le cas présenté concerne un homme âgé de 61 ans (71 kg, 172 cm, soit un indice de masse corporelle de 23,9 kg/m²) admissible à une transplantation pulmonaire en raison d’une insuffisance respiratoire chronique terminale sur emphysème post-tabagique, sous oxygénothérapie continue (1 L/min) et ventilation non invasive nocturne. Il présente, comme principaux antécédents, une dyslipidémie, une hypertension artérielle et un tabagisme sevré estimé à 21 paquets-années (facteurs de risque cardiovasculaires). Le bilan préopératoire a révélé une hypertension artérielle pulmonaire essentiellement postcapillaire conduisant à l’ajout du périndopril (2 mg par jour) et du furosémide (40 mg par jour). La mise en évidence d’un Elispot (enzyme-linked immunospot) positif pour la tuberculose a motivé l’introduction d’un traitement prophylactique par l’association rifampicine-isoniazide (600-300 mg par jour) pour une durée de trois mois.

Deux mois après le bilan préopératoire, le patient a bénéficié d’une transplantation mono-pulmonaire gauche sans dysfonction primaire du greffon5,6. Le donneur et le receveur présentaient tous deux un statut sérologique positif pour cytomegalovirus (CMV) et Epstein Barr Virus (EBV). Une sérologie positive de la toxoplasmose a été mise en évidence uniquement chez le receveur. Le traitement immunosuppresseur d’induction associait la méthylprednisolone (500 mg à jour 0 et 375 mg à jour +1 post-transplantation) et le basiliximab, anticorps monoclonal dirigé contre l’interleukine-2 (20 mg à jour 0 et jour +4 posttransplantation). À partir de jour +2 post-transplantation, l’immunosuppression a été maintenue par une trithérapie par voie orale comprenant le tacrolimus à une posologie initiale de 5 mg par jour, le mofétil mycophénolate (MMF) 2000 mg par jour et la prednisone 20 mg par jour. Les traitements associés sont présentés dans le tableau I.

L’évolution est marquée par la survenue, au jour +5 posttransplantation, d’une dégradation respiratoire sur œdème pulmonaire gauche de reperfusion, avec possible participation cardiogénique. Le rejet aigu de grade III, évoqué par la présence d’infiltrats lymphocytaires aux biopsies transbronchiques, a été confirmé par l’anatomopathologie. Un traitement intraveineux par méthylprednisolone (1000 mg au jour 1, 500 mg au jour 2, 250 mg au jour 3 puis décroissance progressive par voie orale de la posologie de prednisone de 25 à 50 % tous les trois à quatre jours pour atteindre une posologie de 0,15 mg/kg/jour) a été mis en place. Les biopsies transbronchiques de contrôle, réalisées une semaine après le traitement, retrouvent un rejet non évolutif. La présence d’anticorps anti-HLA (antigènes des leucocytes humains) de type DSA (donor-specific antibody) a conduit à la mise en place d’un traitement immunomodulateur par immunoglobulines polyvalentes (1 g/kg/jour pendant deux jours tous les mois pendant trois mois). Sur le plan biologique, aucune anomalie cliniquement significative n’est mise en évidence, notamment en faveur d’une infection (réaction en chaîne par polymérase (PCR) EBV et CMV négatives, cultures microbiologiques du liquide bronchoalvéolaire stériles, protéine C réactive (CRP) à 9 mg/L, leucocytes à 4,5 G/L). Le suivi thérapeutique a mis en évidence une concentration résiduelle sanguine en tacrolimus infrathérapeutique, persistante depuis le début de la transplantation pulmonaire, malgré une adhésion thérapeutique optimale (Figure 1).

La polymédication des patients transplantés conduit à de nombreuses interactions médicamenteuses potentielles qu’il est important de déceler et de prendre en charge afin de maintenir l’efficacité clinique des traitements immunosuppresseurs.
""",
"model_name": "llama3.1:8b"
}


# Send the POST request
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Get the content from the response as a string
    content = response.json()
    # Decode the unicode escape sequences to make it readable
    c = content["summary"]
    print(c)
    
else:
    print("Error:", response.status_code)

