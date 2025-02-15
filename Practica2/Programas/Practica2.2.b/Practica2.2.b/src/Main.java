public class Main {
    public static void main(String[] args) {

        // Declaración de constantes
        final double VELOCIDAD_CRECIMIENTO = 2.0; // cm/mes

        // Definir valores manualmente
        double longitudInicial = 1.5; // Longitud inicial del cabello en cm
        double longitudFinal = 3.5; // Longitud final deseada en cm
        int opcion = 1; // Unidad de tiempo (1: meses, 2: días, 3: semanas)

        // Calcular el tiempo necesario
        double tiempoMeses = (longitudFinal - longitudInicial) / VELOCIDAD_CRECIMIENTO;

        // Convertir el tiempo según la opción seleccionada
        switch (opcion) {
            case 1: // Meses
                System.out.print("El estudiante deberá esperar " +tiempoMeses+" mes o meses, para su siguiente visita al peluquero");
                break;
            case 2: // Días (aproximadamente 30 días por mes)
                System.out.print("El estudiante deberá esperar " +tiempoMeses*30+" mes o meses, para su siguiente visita al peluquero");
                break;
            case 3: // Semanas (aproximadamente 4.3 semanas por mes)
                System.out.print("El estudiante deberá esperar " +tiempoMeses*4.3+" mes o meses, para su siguiente visita al peluquero");
                break;
            default:
                System.out.println("Opción no válida. Mostrando en meses por defecto.");
                System.out.print("El estudiante deberá esperar " +tiempoMeses+" mes o meses, para su siguiente visita al peluquero");
        }
    }
}