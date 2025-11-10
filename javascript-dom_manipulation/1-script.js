#!/usr/bin/node

// Je recupere l'element avec son ID, 'addEventListener': ecoute le clic
document.querySelector('#red_header').addEventListener('click', function () {
  // Changement de sa couleur en rouge
  document.querySelector('header').style.color = '#FF0000';
});
