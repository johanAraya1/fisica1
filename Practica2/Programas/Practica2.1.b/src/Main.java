public class Main {
    public static void main(String[] args) {

        // Velocidad
        final double VELOCIDAD_IMPULSO = 100.0; // en metros por segundo (m/s)

        // Estimar la distancia en metros
        double distancia = 1.5; // Por ejemplo, 1.5 metros

        // Calcular la fórmula del MRU: t = d / v
        double tiempo = distancia / VELOCIDAD_IMPULSO;

        // Convertir el tiempo a milisegundos
        double tiempoMilisegundos = tiempo * 1000;

        // Mostrar el resultado en milisegundos
        System.out.print("El tiempo que tarda el impulso nervioso en llegar " +
                "al cerebro es de "+tiempoMilisegundos+" milisegundos. " +
                "Estimando una distancia de "+distancia+" metros");
    }
}