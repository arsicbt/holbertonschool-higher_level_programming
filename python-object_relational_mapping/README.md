# 📓 Python Object Relational Mapping (ORM)

Salut ! 👋 \
Aujourd'hui je me lance dans la découverte de l’**Object Relational Mapping (ORM)**. Ce projet est mon terrain d’expérimentation pour apprendre à **connecter mes classes Python** à une **base de données MySQL**.

## 📝 Objectif du projet

#### **Apprendre à :**

* **Créer et manipuler** des **tables MySQL** via Python.
* Faire le **lien entre mes classes Python** et mes **tables SQL**.
* Écrire des **scripts sûrs** (anti-injection SQL) et efficaces.
* Utiliser **MySQLdb** pour du SQL classique et **SQLAlchemy** pour de l’ORM.


## 💡 Exemple concret


*En SQLAlchemy, je peux faire quelque chose de magique comme :*
```
state = session.query(State).filter_by(name="Texas").first()
for city in state.cities:
    print(f"{state.name}: ({city.id}) {city.name}")


Résultat :

Texas: (1) Dallas
Texas: (2) Houston
Texas: (3) Austin
```

## 🌱 Ce que j’ai appris jusqu’ici

* La **difféence entre SQL** classique et **ORM**.
* Comment **éviter les injections SQL**.
* La **relation One-to-Many** entre State et City.



*Merci d'etre passer par ici 🌺 \
si tu as des conseils, idées ou bien des pistes d'amélioration à ma partager se serait avec plaisir !*