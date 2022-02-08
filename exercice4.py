clearConsole = lambda: print('\n' * 10)


def print_table(table):
    # Dimention 1 = ligne (y)
    # Dimention 2 = colone (x)
    clearConsole()
    for i, row in enumerate(table):
        row_str = "{:>2}" * len(row)
        row_str = row_str.format(*row)
        print("{:^20}".format(row_str), '\n')


def init_maze(nb_row, nb_col, player_pos, end_pos, walls):
    maze = [["_" for j in range(nb_col)] for i in range(nb_row)]
    maze[player_pos[0]][player_pos[1]] = "O"
    maze[end_pos[0]][end_pos[1]] = "X"
    for wall in walls:
        maze[wall[0]][wall[1]] = "W"

    return maze


def validate_move(maze, new_player_pos):
    if (0 <= new_player_pos[0] < len(maze) and
            0 <= new_player_pos[1] < len(maze[0]) and
            maze[new_player_pos[0]][new_player_pos[1]] != "W"):
        return True
    else:
        return False


def move(key_pressed, maze, player_pos):
    move_dic = {"w": "up",
                "a": "left",
                "s": "down",
                "d": "right"}

    if key_pressed in move_dic:
        move = move_dic[key_pressed]

        new_player_pos = player_pos.copy()
        if move == "up":
            new_player_pos[0] -= 1

        elif move == "down":
            new_player_pos[0] += 1

        elif move == "left":
            new_player_pos[1] -= 1

        elif move == "right":
            new_player_pos[1] += 1

        var = validate_move(maze, new_player_pos)
        print(var)
        if validate_move(maze, new_player_pos):
            maze[player_pos[0]][player_pos[1]] = "_"
            player_pos = new_player_pos.copy()
            maze[player_pos[0]][player_pos[1]] = "O"

    return maze, player_pos


if __name__ == '__main__':
    nb_row = 4
    nb_col = 7
    player_pos = [0, 0]
    end_pos = [nb_row - 1, nb_col - 1]
    walls = [[0, 1], [1, 1], [1, 2], [1, 3], [1, 5], [2, 1], [2, 5], [3, 3], [3, 5]]
    maze = init_maze(nb_row, nb_col, player_pos, end_pos, walls)

    print_table(maze)

    while player_pos != end_pos:
        key_pressed = input("mouvement : ")
        maze, player_pos = move(key_pressed, maze, player_pos)
        print_table(maze)

    print("Vous avez gagnez !")
