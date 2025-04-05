// Declaración de variables globales para canvas y contexto de dibujo
let canvas, ctx;

// Variables físicas
let v0, angle, g, t; // velocidad inicial, ángulo, gravedad, tiempo
let x, y;            // posición del proyectil
let vx, vy;          // componentes de velocidad horizontal y vertical

let scale = 10; // Escala visual: 1 metro = 10 píxeles
let floorHeight = 20; // Altura del suelo en píxeles

// Imagen de fondo del canvas
let backgroundImg = new Image();
backgroundImg.src = "fondo1.jpg"; // Ruta de la imagen de fondo

// Dimensiones del canvas
let width = 1300;
let height = 600;

// Radio del proyectil (bola)
let proyectilRadio = 6;

// Control de rebotes
let reboteRegistrado = false; // indica si ya se mostró la info del primer rebote
let rebotes = 0;              // contador de rebotes

let animationId = null; // Guarda el ID del requestAnimationFrame para poder detenerlo

// Función que configura el canvas al cargar la página
function setupCanvas() {
    canvas = document.getElementById("canvas"); // Obtener referencia al canvas
    canvas.width = width;    // Asignar ancho
    canvas.height = height;  // Asignar alto
    ctx = canvas.getContext("2d"); // Obtener el contexto 2D para dibujar

    drawBackground(); // Dibujar fondo al inicio
}

// Dibuja el fondo y el suelo
function drawBackground() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Limpiar todo el canvas
    ctx.drawImage(backgroundImg, 0, 0, canvas.width, canvas.height); // Imagen de fondo
    ctx.fillStyle = "black"; // Color del suelo
    ctx.fillRect(0, canvas.height - floorHeight, canvas.width, floorHeight); // Dibujo del suelo
}

// Función que se ejecuta al presionar "Iniciar"
function iniciarSimulacion() {
    // Detener cualquier animación previa
    if (animationId) {
        cancelAnimationFrame(animationId);
        animationId = null;
    }

    // Obtener valores desde los inputs HTML
    v0 = parseFloat(document.getElementById("velocidad").value);
    angle = parseFloat(document.getElementById("angulo").value);

    // Validación de entradas
    if (isNaN(v0) || isNaN(angle) || angle < 0 || angle > 90 || v0 <= 0) {
        alert("Ingrese valores válidos: velocidad > 0 y ángulo entre 0° y 90°");
        return;
    }

    // Limpiar info previa en pantalla
    document.getElementById("info").innerHTML = "";
    document.getElementById("estado").innerHTML = "";

    // Reiniciar estado
    reboteRegistrado = false;
    rebotes = 0;
    g = 9.81; // gravedad

    // Convertir ángulo a radianes
    let radians = angle * Math.PI / 180;

    // Calcular componentes iniciales de velocidad (escalados)
    vx = v0 * Math.cos(radians) * scale;
    vy = v0 * Math.sin(radians) * scale;

    // Posición inicial del proyectil (esquina superior izquierda)
    x = proyectilRadio;
    y = proyectilRadio;
    t = 0;

    // Iniciar animación
    animationId = requestAnimationFrame(simular);
}

// Función principal de animación que corre a ~60 FPS
function simular() {
    drawBackground(); // Dibujar fondo

    // Actualizar posición
    x += vx * 0.016;               // desplazamiento horizontal
    vy += g * scale * 0.016;       // aplicar gravedad
    y += vy * 0.016;               // desplazamiento vertical

    // Detectar colisión con el suelo
    if (y + proyectilRadio >= canvas.height - floorHeight) {
        rebotes++; // Aumentar el número de rebotes

        // Primer rebote
        if (rebotes === 1) {
            vy = -vy; // invertir dirección de la velocidad vertical (rebote)
            y = canvas.height - floorHeight - proyectilRadio; // ajustar posición justo encima del suelo

            // Mostrar info del rebote solo una vez
            if (!reboteRegistrado) {
                let vx_final = vx / scale; // quitar escala
                let vy_final = vy / scale;
                let v_total = Math.sqrt(vx_final ** 2 + vy_final ** 2); // velocidad total
                let angle_rebote = Math.atan2(vy_final, vx_final) * (180 / Math.PI); // ángulo final

                // Mostrar datos en el cuadro "info"
                document.getElementById("info").innerHTML = `
                    <strong>Después del primer rebote:</strong><br>
                    Vx = ${vx_final.toFixed(2)} m/s<br>
                    Vy = ${vy_final.toFixed(2)} m/s<br>
                    V = ${v_total.toFixed(2)} m/s<br>
                    θ = ${angle_rebote.toFixed(2)}°
                `;
                reboteRegistrado = true; // evitar que se muestre de nuevo
            }

        } else if (rebotes === 2) {
            // Si ya rebotó dos veces, detener animación
            cancelAnimationFrame(animationId);
            animationId = null;
            return;
        }
    }

    // Dibujar el proyectil
    ctx.fillStyle = "red";
    ctx.beginPath();
    ctx.arc(x, y, proyectilRadio, 0, Math.PI * 2); // dibujar círculo
    ctx.fill();

    // Actualizar el tiempo
    t += 0.016; // 60 fps → cada frame = 1/60 segundos

    // Mostrar información en tiempo real en el cuadro "estado"
    document.getElementById("estado").innerHTML = `
        <strong>Tiempo:</strong> ${t.toFixed(2)} s<br>
        <strong>Posición X:</strong> ${(x / scale).toFixed(2)} m<br>
        <strong>Posición Y:</strong> ${(y / scale).toFixed(2)} m<br>
        <strong>Velocidad X:</strong> ${(vx / scale).toFixed(2)} m/s<br>
        <strong>Velocidad Y:</strong> ${(vy / scale).toFixed(2)} m/s
    `;

    // Solicita el siguiente cuadro de animación
    animationId = requestAnimationFrame(simular);
}

// Ejecutar setupCanvas() cuando la página termine de cargar
window.onload = setupCanvas;
