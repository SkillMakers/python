# Python — De zéro à l'essentiel

Le code des exemples de la formation Python gratuite de la chaîne YouTube
[ItSkillsMaker](https://www.youtube.com/@ItSkillsMaker).

▶️ **La formation complète en une seule vidéo (2h) :** https://youtu.be/PSE-Q7ndR6w

📂 **La playlist, section par section :**
https://www.youtube.com/playlist?list=PLe6-9MbhEih4iKO3s9BT_tp4VyfGJvDiB

## Le code, section par section

| Section | Vidéo | Fichiers |
|---|---|---|
| 1. Installer Python et VS Code | [13:52](https://youtu.be/T1d1tZ9jKn8) | — |
| 2. Les bases : variables, conditions, boucles, fonctions | [23:19](https://youtu.be/UTkEDUl4atY) | `variables.py`, `conditions.py`, `Boucles.py`, `fonctions.py` |
| 3. Les structures de données | [19:27](https://youtu.be/iVGk7DJD0cc) | `listes.py`, `création d'un dictionnaire.py`, `Cas pratiques concrets.py` |
| 4. Les classes et la POO | [20:50](https://youtu.be/BOqUYUp2DGU) | `Définition d'une classe appelée Person.py`, `CompteBancaire.py` |
| 5. Lire et traiter un fichier CSV | [16:51](https://youtu.be/rdMp9IHYbis) | `import csv.py`, `import csv-amelioration.py`, `clients.csv` |
| 6. Consommer une API REST | [12:59](https://youtu.be/qher3Jaz5-E) | `import requests.py` |
| 7. L'héritage | [6:35](https://youtu.be/iMOd2NpVavM) | `heritageMultiple.py` |
| 8. Que faire après avoir appris Python ? | [8:31](https://youtu.be/Sxoe9NfXuB4) | — |

### Ce que contient chaque fichier

- **`variables.py`** — déclarer, afficher et modifier une variable, lire son type.
- **`conditions.py`** — `if` / `elif` / `else` à partir d'un âge saisi au clavier.
- **`Boucles.py`** — la boucle `for` avec `range()`, puis la boucle `while`.
- **`fonctions.py`** — une fonction qui affiche, une fonction qui renvoie un résultat.
- **`listes.py`** — créer une liste, ajouter un élément, la parcourir, compter ses éléments.
- **`création d'un dictionnaire.py`** — accéder à une valeur, la modifier, parcourir clés et valeurs.
- **`Cas pratiques concrets.py`** — six situations réelles qui combinent listes, dictionnaires,
  tuples et sets, puis un récapitulatif pour choisir la bonne structure.
- **`Définition d'une classe appelée Person.py`** — une classe `Personne`, son constructeur et
  une méthode.
- **`CompteBancaire.py`** — une classe avec un état qui évolue : dépôt, retrait, solde insuffisant.
- **`import csv.py`** — lire `clients.csv` ligne par ligne avec `csv.reader`.
- **`import csv-amelioration.py`** — la même lecture, réécrite proprement : `csv.DictReader`,
  des fonctions dédiées et un point d'entrée `main()`.
- **`import requests.py`** — appeler une API avec `requests`, lire le JSON, gérer timeout et
  erreurs HTTP.
- **`heritageMultiple.py`** — une classe qui hérite de trois classes à la fois.

## Utiliser ce code

Il faut **Python 3.6 ou plus récent**. La section 1 montre l'installation.

```bash
git clone https://github.com/SkillMakers/python.git
cd python
python variables.py
```

⚠️ Plusieurs noms de fichiers contiennent des **espaces** : il faut les mettre entre guillemets.

```bash
python "Cas pratiques concrets.py"
python "import csv-amelioration.py"
```

Les scripts de la section 5 retrouvent `clients.csv` à côté d'eux : tu peux les lancer depuis
n'importe quel dossier.

La section 6 utilise la bibliothèque `requests`, à installer une fois :

```bash
pip install requests
python "import requests.py"
```

## Aller plus loin

Toutes les vidéos sont gratuites sur la chaîne. Si le code t'a servi, le meilleur moyen de
soutenir le projet est de t'abonner :
https://www.youtube.com/@ItSkillsMaker?sub_confirmation=1
