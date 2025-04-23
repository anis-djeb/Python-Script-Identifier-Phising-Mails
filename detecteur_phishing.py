import re
import argparse

# Liste de mots clés d'urgence typiques dans le phishing
MOTS_URGENCE = ['urgent', 'immédiatement', 'compte bloqué', 'action requise', 'cliquez ici']
# Terminaisons de domaine suspects (souvent utilisés dans le phishing)
TLD_SUSPECTS = ['.ru', '.cn', '.xyz', '.top', '.tk']
# Faux noms de domaine
FAUX_NOMS_DOMAINE = ['facibook', 'amaz0n', 'microsof', 'paiypal', 'g00gle']

def extraire_liens(texte):
    return re.findall(r'(https?://[\w./\-]+)', texte)

def detecter_adresses_suspectes(texte):
    return re.findall(r'[\w\.-]+@[\w\.-]+', texte)

def analyser_email(chemin_fichier):
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        texte = f.read().lower()

    score = 0
    detections = []

    # 1. Mots clés urgents
    urgents = [mot for mot in MOTS_URGENCE if mot in texte]
    if urgents:
        detections.append(f"Mots-clés urgents détectés : {urgents}")
        score += 30

    # 2. Liens suspects
    liens = extraire_liens(texte)
    liens_douteux = [lien for lien in liens if any(tld in lien for tld in TLD_SUSPECTS)
                     or any(nom in lien for nom in FAUX_NOMS_DOMAINE)]
    if liens_douteux:
        detections.append(f"Liens suspects détectés : {liens_douteux}")
        score += 35

    # 3. Adresses email douteuses
    emails = detecter_adresses_suspectes(texte)
    emails_suspects = [mail for mail in emails if not mail.endswith(('.com', '.fr', '.org'))]
    if emails_suspects:
        detections.append(f"Adresses email suspectes : {emails_suspects}")
        score += 20

    # 4. Fautes typiques de phishing
    fautes_simples = re.findall(r'\bteh\b|\benvoi\b|\bmotpasse\b', texte)
    if fautes_simples:
        detections.append(f"Fautes détectées : {fautes_simples}")
        score += 15

    # Affichage des résultats
    print("\n".join(detections))
    print(f"\nScore de phishing : {min(score, 100)}%")

    if score >= 70:
        print("➡️ Risque ÉLEVÉ de phishing.")
    elif score >= 40:
        print("➡️ Risque MOYEN détecté.")
    else:
        print("✅ Aucun risque évident détecté.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyseur de phishing basé sur règles simples.')
    parser.add_argument('--email', type=str, required=True, help='Chemin vers le fichier texte contenant l’e-mail.')
    args = parser.parse_args()

    analyser_email(args.email)