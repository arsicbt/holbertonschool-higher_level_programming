#!/usr/bin/node

// Chargement du DOM
document.addEventListener('DOMContentLoaded', function () {
  const redHeaderDiv = document.querySelector('#red_header'); // Je recupere l'element via son ID
  const header = document.querySelector('header'); // Je recupere l'element header (à modifier)

  if (redHeaderDiv && header) { // Verification de l'existence des champs
    redHeaderDiv.addEventListener('click', function () { // Ecoute du clic...
      header.classList.add('red'); // Ajout de la classe red
    });
  }
});
