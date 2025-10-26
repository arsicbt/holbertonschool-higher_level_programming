# 🌟 SQL – More Queries

Projet Holberton School\
Auteure : Arsinoé\
📅 Semaine : 20/10 au 24/10

## 🎯 Objectif du projet

Ce projet **approfondit mes connaissances en SQL**.
Après avoir appris à manipuler des tables simples, je vais maintenant découvrir comment **relier des données**, gérer les **droits utilisateurs**, et faire des **requêtes plus complexes**.


## 🧩 Concepts clés
```
Thème	                    | Description rapide
RELATIONS entre tables	    | Lien logique via les clés étrangères
JOINS	                    | Combiner des données venant de plusieurs tables
CONTRAINTES                 | Règles qui garantissent l’intégrité des données
VUES (VIEWS)	            | Requêtes sauvegardées comme des “tables virtuelles” 
DROITS & UTILISATEURS	    | Contrôle d’accès à la base
Sous-requêtes (subqueries)  | Requête à l’intérieur d’une autre requête
```
## 🧠 Notes essentielles
🔹 Créer un utilisateur et lui donner des droits
```
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'project_pass';
GRANT ALL PRIVILEGES ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
```

*Astuce : Toujours utiliser FLUSH PRIVILEGES; après avoir changé les permissions.*

🔹 Créer une table avec contrainte de clé étrangère
```
CREATE TABLE cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE people (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    city_id INT,
    FOREIGN KEY (city_id) REFERENCES cities(id)
);
```

*Ici, city_id je relis chaque personne à une ville dans la table cities.*

🔹 JOINS – Relier les tables entre elles
```
INNER JOIN

SELECT people.name, cities.name AS city
FROM people
JOIN cities ON people.city_id = cities.id;


LEFT JOIN

SELECT people.name, cities.name AS city
FROM people
LEFT JOIN cities ON people.city_id = cities.id;
```

*Rappel :*

* *INNER JOIN → affiche seulement les correspondances*
* *LEFT JOIN → garde toutes les personnes même sans ville associée*

🔹 Contraintes de données
```
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10,2) CHECK (salary > 0)
);
```

*Astuce: Les contraintes t’évitent bien des bugs plus tard !*

🔹 Utiliser des vues (views)
```
CREATE VIEW top_students AS
SELECT name, grade
FROM students
WHERE grade >= 90;
```

Ensuite tu peux faire :
```
SELECT * FROM top_students;
```

*Les vues rendent tes requêtes longues plus faciles à relire et à maintenir.*

🔹 Sous-requêtes (subqueries)
```
SELECT name
FROM students
WHERE grade = (SELECT MAX(grade) FROM students);
```

*Ici, la sous-requête récupère la meilleure note, et la requête principale trouve l’étudiant correspondant.*

🔹 Grouper et filtrer les résultats
```
SELECT city_id, AVG(age) AS average_age
FROM people
GROUP BY city_id
HAVING AVG(age) > 25;
```


#### Merci d'avoir lu ! n'hésites pas si tu as des conseils ou bien des améliorations à proposer 🌺
