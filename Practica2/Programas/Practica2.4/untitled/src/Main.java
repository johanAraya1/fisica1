public class Main {
    public static void main(String[] args) {
        // Parámetros iniciales
        double d0 = 10.0; // Separación inicial en metros
        double a1 = 2.0;  // Aceleración del carrito 1 en m/s²
        double a2 = 1.0;  // Aceleración del carrito 2 en m/s²
        double t = 3.0;   // Tiempo en segundos

        // Inciso a: Separación después del tiempo colocado en la variable t en segundos
        double d1 = 0.5 * a1 * t * t;
        double d2 = 0.5 * a2 * t * t;
        double separacion = d0 + d1 + d2;
        System.out.println("Separación después de "+t+" s es de " + separacion + " m");

        // Inciso b: Tiempo para encontrarse
        double tiempoEncuentro = Math.sqrt((2 * d0) / (a1 + a2));
        System.out.println("Tiempo para toparse: " + tiempoEncuentro + " s");

    }
}