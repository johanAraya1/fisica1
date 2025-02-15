public class Main {
    public static void main(String[] args) {

        // Datos iniciales (pueden modificarse manualmente)
        double vi = 2.00e4; // Velocidad inicial en m/s
        double vf = 6.00e6; // Velocidad final en m/s
        double d = 1.50e-2; // Distancia en metros

        // Calcular la aceleración usando la ecuación de Torricelli: vf^2 = vi^2 + 2ad
        double a = (Math.pow(vf, 2) - Math.pow(vi, 2)) / (2 * d);

        // Calcular el tiempo usando la ecuación de velocidad: vf = vi + at
        double t = (vf - vi) / a;

        // Mostrar los resultados en notación científica con 2 decimales
        System.out.printf("Aceleración del electrón: %.2e m/s²\n", a);
        System.out.printf("Intervalo de tiempo transcurrido: %.2e s\n", t);
    }
}