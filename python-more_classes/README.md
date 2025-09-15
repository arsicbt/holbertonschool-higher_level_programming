# Python - More Classes and Objects 🐍

Je continue mon aventure en **programmation orientée objet (POO)** avec **Python**, cette fois-ci en approfondissant mes connaissances sur les **classes** et **objets**.


## 👩🏼‍🎓 Concepts avancés que je vais explorer

#### 1️⃣ Héritage

Permet de créer des **classes enfants** à partir de classes existantes.
```python
class Animal:
    def speak(self):
        return "Je fais un son"

class Dog(Animal):  # Dog hérite de Animal
    def speak(self):
        return "Woof !"

dog = Dog()
print(dog.speak())  # Output: Woof !
```

#### 2️⃣ Polymorphisme

Une même **méthode** peut **agir différemment selon l’objet**.
```python
class Cat(Animal):
    def speak(self):
        return "Meow !"

animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())  # Output: Woof ! Meow !
```

#### 3️⃣ Attributs et méthodes privés/protégés

**Protéger** les **données** et **contrôler** l’accès aux **informations internes**.
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # attribut privé

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # Output: 150
```

#### 4️⃣ Méthodes de classe et statiques

Différence entre ce qui appartient à la **classe** et à l’**instance**.
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        return f"{cls.__name__} fournit des utilitaires mathématiques."

print(MathUtils.add(5, 3))          # Output: 8
print(MathUtils.description())       # Output: MathUtils fournit des utilitaires mathématiques.
```
#### 5️⃣ Constructeur __ init __ avancé

**Initialisation flexible** des objets.
```python
class Student:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

student = Student("Alice")
print(student.name, student.age)  # Output: Alice 18
```

## 🌞 Conclusion

Ce projet me permet de passer de la **théorie à la pratique** en POO et de mieux comprendre comment structurer mes programmes Python.
En expérimentant avec **classes**, **objets**, **héritage** et **polymorphisme**, je renforce ma capacité à écrire du code **propre**, **modulable** et **maintenable**.