#!/usr/bin/node

document.addEventListener('DOMContentLoaded', async function () {
  const listMovie = document.querySelector('#list_movies');
  if (!listMovie) return;

  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Création d'une liste des titres de film dans 'ul'
    const data = await response.json();
    data.results.forEach(film => {
      const li = document.createElement('li');
      li.textContent = film.title;
      listMovie.appendChild(li);
    });
  } catch (error) {
    console.error('Erreur lors de la récupération des films :', error);
  }
});
