# 🌟 SQL – Introduction

Projet Holberton School\
Auteure :  Arsinoé\
📅 Semaine : 20/10 au 24/10
## 🎯 Objectif du projet

Ce projet introduit les **bases de SQL** (Structured Query Language), un langage indispensable pour **interagir avec des bases de données** relationnelles.
L’objectif est de comprendre comment **stocker, interroger, mettre à jour et supprimer** des **données** efficacement.

## 🧩 Concepts clés à retenir
```
Thème                      | Description rapide
Base de données            | Ensemble organisé de données
Table	                   | Conteneur pour les données (colonnes = attributs, lignes = enregistrements)
SQL                        | Langage pour communiquer avec la base
Clé primaire (PRIMARY KEY) | Identifie de manière unique chaque ligne
Clé étrangère (FOREIGN KEY)| Relie deux tables entre elles
Requête	                   | Instruction SQL pour demander une action à la base
```
## 🧠 Notes essentielles
🔹 Créer une base de données
```
CREATE DATABASE holberton_school;
```

🔹 Créer une table
```
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    grade FLOAT
);
```

🔹 Insérer des données
```
INSERT INTO students (name, age, grade)
VALUES ('Awa', 22, 92.5),
       ('Sofia', 24, 88.0),
       ('Léa', 23, 95.2);
```
🔹 Lire les données
```
SELECT * FROM students;
SELECT name, grade FROM students WHERE grade > 90;
```
🔹 Mettre à jour des données
```
UPDATE students
SET grade = 96.0
WHERE name = 'Léa';
```
🔹 Supprimer des données
```
DELETE FROM students WHERE name = 'Sofia';
```
🔹 Supprimer une table
```
DROP TABLE students;
```

#### Merci d'avoir lu ! n'hésites pas si tu as des conseils ou bien des améliorations à proposer 🌺
