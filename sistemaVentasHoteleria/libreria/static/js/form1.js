  document.getElementById('btn-habilitar-panel').addEventListener('click', function () {
    const inputs = document.querySelectorAll('#form-panel-1 input');
    const btnGuardar = document.getElementById('btn-guardar');

    inputs.forEach(input => input.removeAttribute('disabled'));
    btnGuardar.removeAttribute('disabled');
  });