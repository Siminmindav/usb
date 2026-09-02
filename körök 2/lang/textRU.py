import math
caption = "Бесконечная спираль"
fps = f"Кадры в секунду: "

instructions = [
    "---Навигация---",
    "пробел:                           Добавляет новый квадрат.",
    "левая кнопка мыши:       Перетаскивает средний квадрат.",
    "колёсико мыши:              Изменяет изменяемую переменную.",
    "прокрутить вверх:           Увеличивает выбранную переменную.",
    "прокрутить вниз:            Уменьшает выбранную переменную.",
    "правая кнопка мыши:     Удаляет последний добавленный квадрат.",
    "OK"
    ]

variables = [
    "Скорость: ",
    " градус/кадр",
    "Размер: ",
    " px^2",
    "Радиус: ",
    " px",
    "Красный: ",
    " цвет",
    "Зелёный: ",
    " цвет",
    "Синий: ",
    " цвет",
    "Ничего",
    "opacity: ",
    " 1bit value",
    "négyzet: ",
    " bináris",
    "kör: ",
    " bináris",
    "vonal: ",
    " bináris",
    "háttér átettszése: ",
    " 1bites érték",
    "szög: ",
    " fok",
    "Semmi",
]

developer = [
    "Készítette: Siminmin",
    "GitHub link:",
    "https://github.com/Siminmindav/spinner",
    "",
    "Zene:",
    "szerő - dal",
    "szerő2 - dal2",
    "",
    "Köszönöm, hogy játszottál!",
]

savings = [
    "Kiválasztott fájl:",
    "Nevezd el a fájlt!",
]

trashing = [
    "Mindent kitörölsz?",
]
leaving = [
    "Elhagyod a játékot?",
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
    ]

textlist = [
    ["Choose window size", (115, 20), 0],
    ["A few sizes:", (13, 70), 0],
    ["800x800", (20, 120), (13, 114, 90, 35)],
    ["700x700", (20, 170), (13, 164, 90, 35)],
    ["fullscreen", (20, 220), (13, 214, 99, 35)],
    ["Type size here:", (220, 70), 0],
    ["X                  px", (220,120), (243, 114, 90, 35)],
    ["", (250,120), 0],
    ["Y                  px", (220,170), (243, 164, 90, 35)],
    ["", (250,170), 0],
]