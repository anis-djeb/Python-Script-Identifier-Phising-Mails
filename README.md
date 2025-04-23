# Détection Automatisée de Courriels de Phishing

> Veuillez visiter ce [lien](https://www.coursera.org/professional-certificates/google-cybersecurity) pour plus d'informations.

Ce projet de cybersécurité a pour objectif d’analyser et de détecter automatiquement des courriels frauduleux (phishing), à travers une approche en deux étapes :
- Une analyse manuelle de cas typiques de phishing
- Une détection automatisée par script Python basé sur des règles simples

---

## Objectif

Le phishing est une technique d’ingénierie sociale visant à tromper les utilisateurs pour leur soutirer des informations sensibles. Ce projet a pour but de :

- Identifier des signes typiques de phishing à travers des exemples concrets
- Développer un script Python pour détecter automatiquement ces signes
- Illustrer des compétences pratiques en cybersécurité, automatisation et analyse textuelle

---

## Scénarios manuels d’analyse

### Scénario 1 : Le faux agent du FBI

**Contenu**  
> Bonjour, je m'appelle Albert et je suis un agent du FBI infiltré en Ouganda. Mon adresse e-mail W.A.E. a été compromise. Je vous contacte depuis un compte temporaire car la dictature locale bloque les e-mails vers les pays occidentaux. J'ai besoin d'utiliser votre compte pour envoyer des informations critiques à mon QG. Cela nécessitera l'accès à votre messagerie.

**Analyse**  
Cet e-mail utilise un contexte international alarmiste pour créer un sentiment d'urgence. L’absence totale de professionnalisme, la nature invérifiable de l’histoire et la demande d'accès au compte font de ce message un exemple clair de phishing.

---

### Scénario 2 : Le lien Facebook piégé

**Contenu**  
> Sujet : Facebook ne fonctionne pas  
> De : Jimmy  
> À : moi  
> Je pense que Facebook est hors service, je n'arrive pas à me connecter. Peux-tu essayer ?  
> https://www.facibook.com.ipt/login.htm  
> Merci,  
> Vinny

**Analyse**  
Ce message semble informel mais dissimule un lien piégé. Le domaine `facibook.com.ipt` est manifestement frauduleux et tente d’imiter Facebook. Il s’agit ici d’un cas typique d’hameçonnage via usurpation de lien.

---

### Scénario 3 : La fausse carte cadeau

**Contenu**  
> De : Récompenses X xx  
> À : employe@xmail.com  
> Objet : carte de récompense  
> Bonjour Simon,  
> En reconnaissance de votre travail, vous recevrez une carte cadeau. Veuillez ouvrir la piece jointe pour consultez votre solde. Le montant dépent de votre poste. Cliquez [ici]() pour en savoir plus.

**Analyse**  
Les fautes d’orthographe et le flou du message laissent présager une tentative de phishing. Le message joue sur la gratification et incite au clic sur un lien peu transparent. Aucun contact vérifiable n’est mentionné.

---

## Détection automatisée avec Python

J'ai développé le script `detecteur_phishing.py`, qui s'appuie sur une série de règles simples pour analyser automatiquement un message et identifier les indicateurs de phishing.

### Méthodologie de détection

Le système s’appuie sur 4 critères :

1. **Présence de mots-clés urgents** (ex: "urgent", "immédiatement", "compte bloqué", etc.)
2. **Faux liens (URLs)** avec noms mal orthographiés ou domaines douteux (ex: `facibook.com`, `.ru`, `.xyz`)
3. **Adresses email frauduleuses** (ex: `support-secure@notfacebook.com`)
4. **Fautes d’orthographe ou formulations peu professionnelles**

Chaque élément augmente un score de suspicion entre 0 et 100 %.

---

## Structure du projet

```
📁projet-phishing/
├── detecteur_phishing.py         # Script d’analyse autonome
├── exemple_email.txt             # Exemple d’e-mail à analyser
└── README.md                     # Présentation du projet
```

---

## Lancement de l’analyse

```bash
python detecteur_phishing.py --email exemple_email.txt
```

---

## Exemple de détection

**Contenu de `exemple_email.txt`** :

```
Bonjour, votre compte a été bloqué. Veuillez vous reconnecter immédiatement via ce lien : http://secure-facibook.xyz/login
Merci, le support client.
```

**Résultat du script** :

![Resultat_script](https://github.com/anis-djeb/assets/blob/main/Cybersecurite%20Identifier%20Phising%20Mails/Screenshot_1.png)

---

## Perspectives d'amélioration

- Intégration de modèles de machine learning (Naive Bayes, Random Forest)
- Enrichissement avec des jeux de données publics (SpamAssassin, Kaggle)
- Développement d’une interface web interactive (Streamlit, Flask)
- Intégration dans un système de filtrage mail d’entreprise
