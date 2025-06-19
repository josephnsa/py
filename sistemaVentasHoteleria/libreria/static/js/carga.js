  document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/categorias/')
      .then(response => response.json())
      .then(data => {
        const select = document.getElementById('tipoHabitacion');
        data.forEach(cat => {
          const option = document.createElement('option');
          option.value = cat.id;
          option.textContent = cat.nombre;
          select.appendChild(option);
        });
      })
      .catch(error => {
        console.error('Error al cargar categorías:', error);
      });
  });

    document.querySelector('form').addEventListener('submit', function (e) {
    const codigo = document.getElementById('codigo').value.trim();
    const ingreso = document.getElementById('fechaIngreso').value;
    const salida = document.getElementById('fechaSalida').value;
    const tipo = document.getElementById('tipoHabitacion').value;

    if (!codigo && !ingreso && !salida && (tipo === 'Selecciona...' || !tipo)) {
      e.preventDefault();
      alert('Por favor, llena al menos un filtro para buscar.');
    }
  });