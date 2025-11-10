#!/usr/bin/node

// Je recupere l'element avec son ID, addEventListener ecoute le clic de l'user
document.querySelector('#red_header').addEventListener('click', function () {
  // Changement de la couleur en rouge
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
});
