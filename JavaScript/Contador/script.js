// Script para la cuenta atrás
let numero = 10; // Valor inicial de la cuenta atrás
const contadorElemento = document.getElementById('contador');

const intervalo = setInterval(() => {
  contadorElemento.textContent = numero; // Actualiza el contenido del DIV
  numero--; // Decrementa el número

  if (numero < 0) {
    clearInterval(intervalo); // Detiene el intervalo cuando llega a 0
    contadorElemento.textContent = "¡Cuenta atrás finalizada!"; // Mensaje final
  }
}, 1000); // Intervalo de 1 segundo (1000 ms)