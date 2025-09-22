# Python - Inheritance 🐍

Je continue mon parcours en **programmation orientée objet (POO)** avec Python, et cette fois je replonge dans un concept fondamental : **l’héritage**.  

---

## 👩🏼‍🎓 Concepts clés que je vais explorer

### 1️⃣ Héritage de base
Créer une **classe enfant qui hérite des attributs et méthodes d’une classe parente**.

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

### 2️⃣ Utilisation de super()

**Accéder aux méthodes** de la **classe parente** depuis la classe enfant.

```
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)      # Appel du constructeur parent
        self.student_id = student_id

student = Student("Alice", 1234)
print(student.name, student.student_id)  # Output: Alice 1234
```

#### 3️⃣ Vérifications avec isinstance() et issubclass()

Vérifier les **relations entre objets et classes**.
```
print(isinstance(student, Student))  # True
print(isinstance(student, Person))   # True
print(issubclass(Student, Person))   # True
```
#### 4️⃣ Surcharge de méthodes

**Redéfinir une méthode héritée** pour modifier son comportement.
```
class Cat(Animal):
    def speak(self):
        return "Meow !"

animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())  # Output: Woof ! Meow !
```
### 5️⃣ Classes de base et organisation du code

Créer des **hiérarchies de classes** pour structurer de gros projets.
```
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(4, 5)
print(rect.area())  # Output: 20
```
## 🌞 Conclusion

Ce projet me permet de passer un cap en **POO** :

Je comprends comment **hériter** du travail déjà fait dans une classe parente.

J’apprends à utiliser **super()** intelligemment pour éviter la duplication.

Je découvre comment Python me donne des outils comme **isinstance()** et **issubclass()** pour analyser mes objets.
