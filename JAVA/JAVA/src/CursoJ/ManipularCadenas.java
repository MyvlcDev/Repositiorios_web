package CursoJ;


public class ManipularCadenas {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String nombre="Cruso de Java";
		
		System.out.println("la pirmera letra de "+ nombre+ "es la letra "+ nombre.charAt(0));
		
		String frase2="Hoy es un excelente d�a para estudiar el Curso de Java";
		
		int ultimaletra=frase2.length();
		
		System.out.println("La �ltima letra de " + frase2 + " es la letra "+ frase2.charAt(ultimaletra-1));
		
		
		String frase3="No hay nada mejor que levantarse un domingo para estudiar Java";
		
		System.out.println(frase3.substring(22, 43));
		
		String palabra1="Casa";
		String palabra2="casa";
		String palabra3="casa";

		
		System.out.println(palabra1.equals(palabra2));
		
		System.out.println(palabra1.equalsIgnoreCase(palabra3));

	}

}
