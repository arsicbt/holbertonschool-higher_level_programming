# Python - Classes and Objects 🐍

Hello ! 👋  
Je m’apprête à plonger à nouveau dans la **programmation orientée objet** (POO) avec **Python**.  
J’avais déjà découvert ce concept en autodidacte, mais cette fois-ci je vais l’explorer de manière plus **structurée et approfondie** grâce à ma formation chez **Holberton**.

---

## 🧠 Pourquoi la POO ?
La POO, c’est un peu comme apprendre à mieux organiser son code :  
- On regroupe données **(attributs)** et comportements **(méthodes)** dans des **classes**.  
- On crée ensuite des **objets** (instances) qui sont comme des "petits clones" personnalisés de ces classes.  

👉 C’est un moyen puissant d’écrire du code **plus clair, réutilisable et modulaire**.

---

## 🔑 Concepts que je vais revoir
- **Classe** → le plan / le modèle de base  
- **Instance** → un objet créé à partir d’une classe  
- **Attributs** → les variables contenues dans une classe (ou une instance)  
- **Méthodes** → les fonctions définies dans une classe  
- **Attributs publics, protégés et privés**  
- **Méthodes de classe, d’instance et statiques**  
- **Constructeur `__init__`**  
- La notion d’**encapsulation**

---

## 📝 Exemple rapide
```python
class Student:
    school = "Holberton"  # attribut de classe (partagé)

    def __init__(self, name):
        self.name = name  # attribut d'instance (propre à chaque objet)

    def introduce(self):
        return f"Salut, je m'appelle {self.name} et j'étudie à {Student.school} !"

# Création d'une instance
me = Student("Arsinoé")
print(me.introduce())

# Résultat : Salut, je m'appelle Arsinoé et j'étudie à Holberton !
```


## 🌱 Objectifs personnels

- **Comprendre en profondeur** la différence entre **attributs de classe et d’instance**

- Savoir **manipuler les attributs publics**, **protégés** et **privés**

- Être capable de construire des projets bien structurés grâce à la POO

- Préparer une base solide pour aller plus loin (héritage, polymorphisme, etc.)

## 🙌 Conclusion

Je suis super enthousiaste de replonger dans la POO avec Python !
Cette fois, ce sera moins de bricolage, plus de rigueur, et surtout beaucoup de **pratique** grâce à Holberton.

💻 Prochaine étape : **coder, tester, expérimenter, et documenter chaque progrès !**
