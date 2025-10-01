# 🐍 Projet Python – Serialization
## 💁🏼‍♀️ Contexte

Ce projet fait suite à mon apprentissage du Python chez Holberton School.
L’objectif était de comprendre la **sérialisation** : c’est-à-dire transformer des **objets Python** en **formats pouvant être stockés** (fichiers) ou transmis (réseau), puis les **reconstruire**.

**En gros :** \
➡️ **Sérialiser** = transformer un objet Python en un format comme JSON, Pickle, etc. \
➡️ **Désérialiser** = faire l’inverse, récupérer l’objet initial.

## 🌷 Contenu du projet
#### **Ce que j’ai appris :**

* **Manipuler différents formats** de **sérialisation** (json, pickle, éventuellement yaml).
* **Sauvegarder des objets Python** dans un fichier.
* **Charger ces objets** pour les réutiliser plus tard.
* Voir les **avantages/inconvénients** entre formats lisibles (JSON) et formats binaires (Pickle).

#### **Fichiers importants :**

-  *serialization.py* → contient les fonctions principales.
- *data.json* → exemple de fichier de données sérialisées.
 - *test_serialization.py* → tests pour vérifier que tout fonctionne.


## ⭐ Conclusion

Au début, je pensais que la sérialisation c’était juste “écrire dans un fichier”, mais en fait c’est beaucoup plus puissant, surtout pour l’échange de données entre programmes. 

Le plus pratique pour moi reste JSON car il est, je trouve, plus lisible. \
Pickle est cool mais “magique” (on ne voit pas ce qu’il y a dedans)

*Merci d'avoir pris le temps de regarder ce projet, si tu as des conseils / idées à me partager se serait avec plaisir* 🌺