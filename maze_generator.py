import random
from PIL import Image, ImageDraw, ImageFont
from models.cell import Cell


def generate(x=20, y=20, cell_size=20, text="", time="morning"):
    if x > 400:
        x = 400
    if x < 2:
        x = 2
    if y > 400:
        y = 400
    if y < 2:
        y = 2
    print(f"Generando laberinto de {x} x {y}...")

    # random.seed(4)

    grid = [[Cell() for _ in range(x)] for _ in range(y)]

    current_row = random.randrange(0, y)
    current_cell = random.randrange(0, x)
    cell = grid[current_row][current_cell]
    cell.visited = True
    visited_cells = [[current_row, current_cell]]
    intento_arriba = False
    intento_derecha = False
    intento_abajo = False
    intento_izquierda = False
    while len(visited_cells) > 0:
        direction = random.randint(1, 4)
        valid = False
        if direction == 1 and current_row > 0:  # arriba
            current_row -= 1
            next_cell = grid[current_row][current_cell]
            if not next_cell.visited:
                valid = True
                cell.muro_arriba = False
                next_cell.muro_abajo = False
                cell = next_cell
            else:
                current_row += 1
        elif direction == 2 and current_cell < x - 1:  # derecha
            current_cell += 1
            next_cell = grid[current_row][current_cell]
            if not next_cell.visited:
                valid = True
                cell.muro_derecha = False
                next_cell.muro_izquierda = False
                cell = next_cell
            else:
                current_cell -= 1
        elif direction == 3 and current_row < y - 1:  # abajo
            current_row += 1
            next_cell = grid[current_row][current_cell]
            if not next_cell.visited:
                valid = True
                cell.muro_abajo = False
                next_cell.muro_arriba = False
                cell = next_cell
            else:
                current_row -= 1
        elif direction == 4 and current_cell > 0:  # izquierda
            current_cell -= 1
            next_cell = grid[current_row][current_cell]
            if not next_cell.visited:
                valid = True
                cell.muro_izquierda = False
                next_cell.muro_derecha = False
                cell = next_cell
            else:
                current_cell += 1

        if valid:
            cell.visited = True
            visited_cells.append([current_row, current_cell])
        else:
            if direction == 1:
                intento_arriba = True
            if direction == 2:
                intento_derecha = True
            if direction == 3:
                intento_abajo = True
            if direction == 4:
                intento_izquierda = True
            if intento_arriba and intento_derecha and intento_abajo and intento_izquierda and len(visited_cells) > 0:
                intento_arriba = False
                intento_derecha = False
                intento_abajo = False
                intento_izquierda = False
                coords_prev_cell = visited_cells.pop()
                current_row = coords_prev_cell[0]
                current_cell = coords_prev_cell[1]
                cell = grid[current_row][current_cell]

    entrada = [random.randrange(0, y), 0]
    salida = [random.randrange(0, y), x - 1]
    grid[entrada[0]][entrada[1]].is_entrance = True
    grid[salida[0]][salida[1]].is_exit = True

    image = Image.new("RGB", (x * cell_size, y * cell_size), color="white")
    draw = ImageDraw.Draw(image)

    x_entrance = 0
    y_entrance = 0
    x_exit = 0
    y_exit = 0

    for ifila, fila in enumerate(grid):
        for icelda, celda in enumerate(fila):
            x_start = cell_size * icelda
            y_start = cell_size * ifila
            if celda.muro_derecha:
                if x_start == image.width - cell_size:
                    x_start -= 1
                line = ((x_start + cell_size, y_start), (x_start + cell_size, y_start + cell_size))
                if celda.is_exit:
                    x_exit = x_start
                    y_exit = y_start
                else:
                    draw.line(line, fill="black")
            x_start = cell_size * icelda
            if celda.muro_izquierda:
                line = ((x_start, y_start), (x_start, y_start + cell_size))
                if celda.is_entrance:
                    x_entrance = x_start
                    y_entrance = y_start
                else:
                    draw.line(line, fill="black")
            if celda.muro_abajo:
                if y_start == image.height - cell_size:
                    y_start -= 1
                line = ((x_start, y_start + cell_size), (x_start + cell_size, y_start + cell_size))
                draw.line(line, fill="black")
            y_start = cell_size * ifila
            if celda.muro_arriba:
                line = ((x_start, y_start), (x_start + cell_size, y_start))
                draw.line(line, fill="black")

    del draw
    maze = Image.new(image.mode, (image.width + (cell_size * 6), image.height + (cell_size * 6)), "white")
    maze.paste(image, (int(cell_size * 3), int(cell_size * 3)))

    draw = ImageDraw.Draw(maze)
    # Write text
    if len(text) > 0:
        font = ImageFont.truetype("arial.ttf", cell_size)
        draw.text((maze.width - cell_size * len(text), maze.height - (cell_size * 2.5)), text, "black", font=font)

    # Put the entrance and exit images
    entrance_img = Image.open(f"assets/start.png").resize((cell_size * 3, cell_size * 3), Image.ANTIALIAS)
    entrance_img_mask = Image.open(f"assets/start.png").resize((cell_size * 3, cell_size * 3), Image.ANTIALIAS)
    maze.paste(entrance_img, (x_entrance, y_entrance + (cell_size * 2)), entrance_img_mask)

    exit_img = Image.open(f"assets/end_{time}.png").resize((cell_size * 3, cell_size * 3), Image.ANTIALIAS)
    exit_img_mask = Image.open(f"assets/end_{time}.png").resize((cell_size * 3, cell_size * 3), Image.ANTIALIAS)
    maze.paste(exit_img, (x_exit + (cell_size * 4), y_exit + cell_size + cell_size), exit_img_mask)

    del draw

    maze.save("maze.png")
    return maze
