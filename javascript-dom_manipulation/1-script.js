#!/usr/bin/node

// Je recupere l'element avec son ID, add
document.querySelector("#red_header").addEventListener("click", function () {
  // Changement de la couleur en rouge
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
});
