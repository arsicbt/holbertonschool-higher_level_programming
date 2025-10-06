# ☁️ Projet API REST Holberton School

**Hello à tous !**  \
Mon évolution en Python continue et cette semaine commence ma découverte des **API REST** ⭐

## ✨ Objectif

L’objectif de ce projet est de maîtriser les bases de la **consommation** d’une **API REST** et de l’**utilisation de requêtes HTTP** en Python.

#### Ce que je vais apprendre : 

* Faire des **requêtes GET** et **POST**.
* **Manipuler** des **réponses JSON**.
* Utiliser des **modules Python adaptés** (*requests*).
* Comprendre les **en-têtes HTTP** et le **statut des réponses**.


## 🌐 Utilisation de base
#### 1. Récupérer des données (GET) 🪝

*Exemple avec JSONPlaceholder :*
````
import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Récupère le JSON
    print(data[0])          # Affiche le premier post
````

#### 2. Envoyer des données (POST) ✈️
````
import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {"title": "foo", "body": "bar", "userId": 1}

response = requests.post(url, json=payload)

if response.status_code == 201:
    print(response.json())  # Nouveau post créé
````

## 🗒️ Points clés

**GET :** récupérer des informations.

**POST :** envoyer des données à l’API.

**JSON :** format standard pour communiquer avec l’API.

**En-têtes HTTP :** permettent de contrôler la réponse et gérer l’authentification, le cache, etc.

*+ Toujours vérifier le status code (200 OK, 201 Created, 404 Not Found, etc.).*

