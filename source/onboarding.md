# Guide d'Intégration & Configuration Client

## Processus d'Onboarding d'un Nouvel Établissement

Lorsqu'un nouvel établissement rejoint la plateforme **Kaliss Core Banking**, la mise en service s'effectue en quelques étapes simples garantissant un démarrage rapide sans perturbation des opérations existantes.

---

## 1. Personnalisation Visuelle (Branding)

Chaque client peut adapter l'interface utilisateur à sa charte graphique :

* **Logo Principal** : Affiché sur l'écran de connexion et dans l'en-tête de navigation.
* **Image de Document & PDFs** : Utilisée pour la génération automatique des reçus de caisse, contrats et relevés de compte.
* **Palette de Couleurs** : Sélection de la couleur primaire (Bleu, Vert, Teal, Indigo, etc.) appliquée automatiquement sur tous les boutons, menus et indicateurs.
* **Coordonnées de l'Institution** : Raison sociale, adresse physique, numéros de téléphone et e-mails de support affichés sur les documents officiels.

---

## 2. Paramétrage des Règles Métier

Depuis l'espace d'administration sécurisé (`/configuration`), l'administrateur de l'établissement peut définir :

* **Découverts et Frais Mensuels** : Autoriser ou restreindre la perception automatique des frais de tenue de compte en cas de découvert.
* **Remboursement de Prêts par Découvert** : Définir si les prélèvements d'échéances de prêt peuvent basculer un compte en solde négatif.
* **Plafonds d'Opérations** : Fixer les montants maximaux pour les dépôts et retraits sans validation préalable du chef d'agence.

---

## 3. Déploiement et Accès Client

Une fois la configuration validée :
1. L'application est déployée sur l'environnement dédié (ex: `client-finances.web.app` ou domaine personnalisé `client.com`).
2. Les comptes administrateurs initiaux sont transmis de manière sécurisée.
3. L'assistant d'installation (**Initial Setup Wizard**) guide l'administrateur lors de la première connexion.
