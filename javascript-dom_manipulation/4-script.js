#!/usr/bin/node

// Chargement du DOM
document.addEventListener('DMContentLoaded', function () {
  const addButton = document.querySelector('#add_item'); // Je recupere le buton
  const myList = document.querySelector('.my_list'); // Et la liste

  if (addButton && myList) {
    addButton.addEventListener('click', function () {
      const LiElement = document.createElement('li'); // Création de l'element 'li'
      LiElement.textContent = 'Item'; // Definition de sa valeur
      myList.appendChild(LiElement); // Ajout dans ma liste
    });
  }
});
