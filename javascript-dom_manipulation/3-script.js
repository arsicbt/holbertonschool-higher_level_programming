#!/usr/bin/node

// Chargement du DOM
document.addEventListener('DOMContentLoaded', function () {
  const toggleDiv = document.querySelector('#toggle_header'); // Je recupere l'element cliquable
  const header = document.querySelector('header'); // Et l'element que je veux modifier

  toggleDiv.addEventListener('click', function () { // Ecoute du clic
    if (header.classList.contains('red')) { // Passer du rouge au vert
      header.classList.remove('red');
      header.classList.add('green');
    } else if (header.classList.countains('green')) { // Passer du vert au rouge (reverse)
      header.classList.remove('green');
      header.classList('red');
    } else { // Cas vide, passage au rouge
      header.classList.add('red');
    }
  });
});
