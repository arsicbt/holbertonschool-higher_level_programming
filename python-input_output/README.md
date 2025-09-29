# 🐍 Python - Input/Output

Je continue mon aventure avec **Python**, et cette fois je plonge dans un concept incontournable : \
les **entrées/sorties** (Input/Output).

**L’idée est simple :** savoir *récupérer des infos*, *les afficher*, et surtout *les stocker dans des fichiers*. Ça peut paraître basique, mais c’est la base de beaucoup de programmes utiles.

## 👩🏼‍🎓 Concepts clés que j’explore
### 1️⃣ Lire un fichier texte

*Ouvrir un fichier et afficher son contenu.*
```
with open("data.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

Ici, with open() permet de gérer automatiquement la fermeture du fichier.

### 2️⃣ Écrire dans un fichier

*Créer un fichier (ou écraser son contenu) avec le mode w.*`

````
with open("notes.txt", "w", encoding="utf-8") as f:
   f.write("Hello world ✨")
````

Après ça, notes.txt contiendra exactement Hello world.

### 3️⃣ Ajouter du contenu (sans tout effacer)

*Le mode a (append) permet de compléter un fichier existant.*

````
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("\nNouvelle ligne ajoutée")
````

Le texte est rajouté à la suite, sans supprimer ce qu’il y avait avant.

### 4️⃣ Récupérer une entrée utilisateur

*Demander une info à l’utilisateur avec input().*

````
name = input("Ton prénom ? ")
print(f"Enchantée, {name} !")
````

Le programme interagit avec la personne qui le lance → trop pratique pour rendre le code plus vivant.

### 5️⃣ Lire un fichier ligne par ligne

*Pratique pour manipuler des fichiers volumineux.*

````
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
````

.strip() sert à enlever les retours à la ligne superflus.

## 🌺 Conclusion

Ce projet m’a permis de comprendre que :

- **Lire/écrire** dans des fichiers est une compétence de base indispensable en Python.
- with **open()** est mon meilleur ami.
- Les petits détails comme **les modes** (r, w, a) ou **l’encodage** (utf-8) peuvent faire toute la différence.

👉 Bref, les **Input/Output**, c’est comme donner une voix et une mémoire à son programme. Et c’est carrément **motivant** pour la suite !
