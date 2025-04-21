package web;
import java.io.IOException;


public class contador {

	public static void main(String[] args) throws InterruptedException, IOException {
		// TODO Auto-generated method stub

		
		  // Iniciamos el contador en 0
        int contador = 0;

        // Bucle para incrementar el contador hasta 10
        while (contador <= 10) {
            // Mostramos el valor actual del contador
            System.out.println("Contador: " + contador);
            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();

            // Incrementamos el contador
            contador++;

            // Pausamos el programa por 1 segundo (1000 milisegundos)
            try {
                Thread.sleep(1000); // Pausa de 1 segundo
            } catch (InterruptedException e) {
                // Manejo de excepción por si ocurre un error en el sleep
                System.err.println("Error al pausar el hilo: " + e.getMessage());
            }
		
            System.out.println();
        }
		
	}

}
