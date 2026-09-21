import math
caption = "Espiral infinita"
fps = f"Fotogramas por segundo: "

captions = [
    "Videojuego",
    "¡Algo está escondido en este juego, encuéntralo!",
    "¡Cierra los ojos y juega un juego! ...o no cierres los ojos y juega un juego!",
    "'¡Pygame no apesta, tú sí!' El arte de la guerra - Sun Tzu",
    "Puedes hacer cualquier cosa aquí. (teóricamente)",
    "Este juego no tiene un objetivo, pero si quieres, puedes encontrar uno.",
    "¯\\_(ツ)_/¯",
    "¡Todo es increíble!",
    ":/",
    "♥♥♥",
    "Hamsteres humedos",
    "Siminmindav Infók és weboldalak (Tengo mi propio sitio web :D)",
]

instructions = [
    "                                  --- Controles ---",
    "Espacio:                               Crea un nuevo cuadrado.",
    "Botón izquierdo del ratón:       Arrastra el cuadrado del medio.",
    "Botón central del ratón:          Cambia la variable modificable.",
    "Rueda del ratón hacia arriba:   Aumenta la variable seleccionada.",
    "Rueda del ratón hacia abajo:   Disminuye la variable seleccionada.",
    "Botón derecho del ratón:        Elimina el último cuadrado invocado.",
    ]
variables = [
    "Velocidad: ",
    " grado/por fotograma",
    "Tamaño: ",
    " px^2",
    "Radio: ",
    " px",
    "Rojo: ",
    " valor de color",
    "Verde: ",
    " valor de color",
    "Azul: ",
    " valor de color",
    "Opacidad: ",
    " valor 0-1",
    "rectángulo: ",
    " bool",
    "círculo: ",
    " bool",
    "línea: ",
    " bool",
    "Opacidad de fondo: ",
    " valor 0-1",
    "ángulo: ",
    " grados",
    "nada",
    ]

developer = [
    "Desarrollado por: Siminmin",
    "GitHub link:",
    "https://github.com/Siminmindav/spinner",
    "",
    "Música:",
    "szerő - dal",
    "szerő2 - dal2",
    "",
    "¡Gracias por jugar!",
]

savings = [
    "Archivo seleccionado",
    "Nombre del archivo",
]

trashing = [
    "¿Borrar todo?",
]
leaving = [
    "¿Abandonar el juego?",
]

def textgenforaction(base,opacity):
    return [
    f"{variables[0]}{math.floor(base.omega*10)/10}{variables[1]}",
    f"{variables[2]}{math.floor(base.w*10)/10}{variables[3]}",
    f"{variables[4]}{base.r}{variables[5]}",
    f"{variables[6]}{base.color.r}{variables[7]}",
    f"{variables[8]}{base.color.g}{variables[9]}",
    f"{variables[10]}{base.color.b}{variables[11]}",
    f"{variables[12]}{base.color.opacity}{variables[13]}",
    f"{variables[14]}{base.shapes[0]}{variables[15]}",
    f"{variables[16]}{base.shapes[1]}{variables[17]}",
    f"{variables[18]}{base.shapes[2]}{variables[19]}",
    f"{variables[20]}{opacity}{variables[21]}",
    f"{variables[22]}{base.angle}{variables[23]}",
    f"{variables[24]}"
    ]

textlist = [
    ["Elija tamaño de ventana", (100, 20), 0],
    ["Algunos tamaños:", (13, 70), 0],
    ["800x800", (20, 120), (13, 114, 90, 35)],
    ["700x700", (20, 170), (13, 164, 90, 35)],
    ["pantalla completa", (20, 220), (13, 214, 170, 35)],
    ["Escriba tamaño aquí:", (200, 70), 0],
    ["X                 px", (220,120), (243, 114, 90, 35)],
    ["", (250,120), 0],
    ["Y                  px", (220,170), (243, 164, 90, 35)],
    ["", (250,170), 0],
]