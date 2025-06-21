  
  (function () {
  'use strict'
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl)
  })
})()

  function cargarContenido(url) {
    fetch(url)
      .then(response => response.text())
      .then(html => {
        document.getElementById("contenido-dinamico").innerHTML = html;
      });

    // Quitar clase 'active' de todos los enlaces
    document.querySelectorAll('.nav-link').forEach(link => {
      link.classList.remove('active');
    });

    // Añadir clase 'active' al enlace que fue clicado
    event.target.closest('.nav-link').classList.add('active');
  }

 