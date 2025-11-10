#!/usr/bin/node

// Chargement du DOM
document.addEventListener('DOMContentLoaded', function () {
  const updtButton = document.querySelector('#update_header'); // Recuperation le bouton via ID
  const header = document.querySelector('header'); // Recuperation de l'element header (à modifier)

  updtButton.addEventListener('click', function () { // Ecoute du clic sur le bouton
    header.textContent = 'New Header!!!';
  });
});
