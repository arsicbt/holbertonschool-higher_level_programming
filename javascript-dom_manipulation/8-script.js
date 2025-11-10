#!/usr/bin/node

// Chargement du DOM
document.addEventListener('DOMContentLoaded', async function () {
  const helloElmt = document.querySelector('#hello');
  if (!helloElmt) return;

  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    helloElmt.textContent = data.hello;
  } catch (error) {
    console.error('Erreur lors du fetch :', error);
  }
});
