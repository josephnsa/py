  
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

 const ctx1 = document.getElementById('graficoIngresos').getContext('2d');
  const ingresosChart = new Chart(ctx1, {
    type: 'bar',
    data: {
      labels: ['Lun', 'Mar', 'Mié', 'Jue', 'Vie'],
      datasets: [{
        label: 'Ingresos (S/.)',
        data: [1200, 1900, 3000, 2500, 2200],
        backgroundColor: 'rgba(54, 162, 235, 0.6)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          labels: {
            color: 'white'
          }
        }
      },
      scales: {
        x: {
          ticks: { color: 'white' },
          grid: { color: '#444' }
        },
        y: {
          ticks: { color: 'white' },
          grid: { color: '#444' },
          beginAtZero: true
        }
      }
    }
  });

  const ctx2 = document.getElementById('graficoProductos').getContext('2d');
  const productosChart = new Chart(ctx2, {
    type: 'doughnut',
    data: {
      labels: ['Agua', 'Snacks', 'Cerveza', 'Galletas'],
      datasets: [{
        label: 'Ventas',
        data: [50, 30, 70, 40],
        backgroundColor: ['#0d6efd', '#198754', '#ffc107', '#dc3545']
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          labels: {
            color: 'white'
          }
        }
      }
    }
  });