#!/usr/bin/node

// Chargement du DOM
document.addEventListener('DOMContentLoaded', async function () { // async permet l'utilisation de await
  const nameChar = document.querySelector('#character'); // Je recupere l'element via son ID

  if (!nameChar) return;

  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  try { // leve une erreur si HTTP non ok
    const response = await fetch(url); // Requete HTTP GET URL
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json(); // convertion du flux en objet JS
    nameChar.textContent = result.name; // affichage du nom
  } catch (error) { // edge case, requete echoue
    console.error(error.message);
  }
});
