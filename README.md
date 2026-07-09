# Portfolio — Petits outils web

Une collection d'outils web légers, rapides et **sans dépendances** — un nouveau chaque jour.
Chaque outil tient dans un seul fichier HTML et fonctionne directement dans le navigateur, sans installation ni compilation.

## 🧰 Outils disponibles

| Outil | Description | Catégorie |
|-------|-------------|-----------|
| [🍅 Pomodoro Focus](pomodoro-focus/index.html) | Minuteur de concentration avec liste de tâches, suivi des cycles et notifications sonores. | Productivité |

*Un nouvel outil arrive bientôt — revenez demain !*

## 🚀 Utilisation

Aucune installation requise. Deux façons de lancer le portfolio :

- **Le plus simple** : ouvrez `index.html` d'un double-clic dans votre navigateur.
- **Recommandé** (pour éviter les limitations des fichiers locaux) : servez le dossier localement, par exemple avec Python —

  ```bash
  python3 -m http.server 8000
  ```

  puis ouvrez http://localhost:8000 dans votre navigateur.

## 🗂️ Structure du projet

```
portfolio-outils/
├── index.html          # Page d'accueil du portfolio
└── pomodoro-focus/
    └── index.html      # Outil : minuteur Pomodoro
```

## 🛠️ Technologies

HTML, CSS et JavaScript purs — **zéro dépendance**, zéro étape de build.

## 📄 Licence

Projet personnel à usage de démonstration.
