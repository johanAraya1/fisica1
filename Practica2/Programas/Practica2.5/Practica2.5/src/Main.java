public class Main {
    public static void main(String[] args) {

        // Parámetros iniciales
        double velocidadInicial = 72 * 1000 / 3600; // 72 km/h a m/s
        double desaceleracion = -1.0; // m/s^2
        double aceleracion = 0.5; // m/s^2
        double tiempoParada = 2.0 * 60; // 2 minutos convertidos a segundos

        // Variables del ciclo de simulación
        double tiempo = 0;
        double posicion = 0;
        double velocidad = velocidadInicial;

        // Tamaño de la matriz (20 filas para el tiempo, 50 columnas para la pista)
        int filas = 20; // El número de filas para mostrar el tiempo
        int columnas = 50; // El número de columnas para la pista

        // Mostrar la simulación de la desaceleración
        System.out.println("Iniciando simulación de desaceleración hasta la parada...");
        while (velocidad > 0) {
            // Actualizamos el tiempo y la posición
            tiempo += 1; // Intervalo de 1 segundo
            velocidad += desaceleracion; // Actualizamos velocidad
            if (velocidad < 0) velocidad = 0; // La velocidad no puede ser negativa
            posicion += velocidad; // Actualizamos posición

            // Dibujamos la simulación en la matriz
            dibujarMatriz(posicion, filas, columnas, false);
            System.out.println("Tiempo: " + tiempo + "s, Velocidad: " + velocidad + " m/s, Posición: " + posicion + " m\n");
        }

        // El tren se detuvo, ahora simulamos la parada de 2 minutos
        System.out.println("\nEl tren se detuvo, simulando la parada de 2 minutos...");
        for (int i = 0; i < tiempoParada; i++) {
            tiempo++;
            // Dibujamos la parada (el tren está detenido)
            dibujarMatriz(posicion, filas, columnas, true);
            System.out.println("Tiempo: " + tiempo + "s, El tren está detenido en la estación.\n");
        }

        // Ahora simulamos la aceleración después de la parada
        System.out.println("\nIniciando simulación de aceleración después de la parada...");
        while (velocidad < velocidadInicial) {
            tiempo++;
            velocidad += aceleracion; // Aceleración positiva
            if (velocidad > velocidadInicial) velocidad = velocidadInicial; // Alcanza su velocidad inicial
            posicion += velocidad; // Actualizamos posición

            // Dibujamos la simulación en la matriz
            dibujarMatriz(posicion, filas, columnas, false);
            System.out.println("Tiempo: " + tiempo + "s, Velocidad: " + velocidad + " m/s, Posición: " + posicion + " m\n");
        }

        // Al final de la simulación mostramos la distancia recorrida
        System.out.println("\nSimulación completa. El tren ha alcanzado su velocidad inicial nuevamente.");
        System.out.println("Distancia total recorrida durante la simulación: " + posicion + " metros.");
    }

    // Método para dibujar la simulación en una matriz
    private static void dibujarMatriz(double posicion, int filas, int columnas, boolean enParada) {
        // Convertimos la posición a una posición dentro de las columnas
        int posicionEnPista = (int)(posicion / 10); // Escalamos la distancia (10 metros por columna)
        if (posicionEnPista > columnas - 1) posicionEnPista = columnas - 1; // Aseguramos que no sobrepase el límite de la pista

        // Limpiamos la consola antes de dibujar (para una mejor visualización)
        System.out.print("\033[H\033[2J");
        System.out.flush();

        // Recorremos las filas para dibujar la simulación
        for (int i = 0; i < filas; i++) {
            StringBuilder fila = new StringBuilder();

            // Si estamos en la parada, mostramos un mensaje claro en la fila central
            if (enParada && i == filas / 2) {
                // Fila central con mensaje de parada
                fila.append("[                    P                                      ]");
            } else {
                // Añadimos espacio vacío antes del tren (es decir, la pista)
                for (int j = 0; j < columnas; j++) {
                    if (j == posicionEnPista) {
                        fila.append('T'); // El tren se representa por 'T'
                    } else {
                        fila.append(' '); // Vacío para la pista
                    }
                }
            }

            // Imprimimos la fila
            System.out.println(fila.toString());
        }
    }
}