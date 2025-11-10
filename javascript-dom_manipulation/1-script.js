#!/usr/bin/node

// Chargement du DOM
document.querySelector("red_header").addEventListener("click", function () {
  // Je recupere l'element avec son ID
  const redHeaderDiv = document.querySelector('#red_header');

  // Est ce que l'element existe ?
  if (redHeaderDiv) {
    redHeaderDiv.addEventListener("click", function () {
      // Changement de la couleur en rouge
      const header = document.querySelector('header');
      if (header) {
        header.style.color = '#FF0000'
      }
   });
}});
