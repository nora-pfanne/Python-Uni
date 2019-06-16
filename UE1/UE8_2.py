def can_move(position, path, width, height):

    if position == None:
        return False

    # Liegt position im Spielfeld?
    if position[0] < width and position[1] < height and position[0] >= 0 <= position[1]:


        # Wurde position bereits besucht?
        for i in range(len(path)):
            if path[i][0] == position[0] and path[i][1] == position[1]:

                return False
        return True
    return False


def is_complete(path, width, height):

    # Anzahl der Felder muss mit den Einträgen übereinstimmen
    return len(path) == (width-1)*(height-1)

# index wird zur Überprüfung mit übergeben
def get_next_positions(position, index):

    if position == None:
        return None

    if index == 1:
        # Alle 8 möglichen Züge eines Springers werden mit can_move überprüft
        #if can_move([position[0]-2, position[1]+1], path, width, height):
        return [position[0]-2, position[1]+1]
    elif index == 2:
       # if can_move([position[0]-2, position[1]-1], path, width, height):
        return [position[0]-2, position[1]-1]
    elif index == 3:
        #if can_move([position[0]+2, position[1]+1], path, width, height):
        return [position[0]+2, position[1]+1]
    elif index == 4:
       # if can_move([position[0]+2, position[1]-1], path, width, height):
        return [position[0]+2, position[1]-1]
    elif index == 5:
       # if can_move([position[0] - 1, position[1] + 2], path, width, height):
        return [position[0] - 1, position[1] + 2]
    elif index == 6:
       # if can_move([position[0] - 1, position[1] - 2], path, width, height):
        return [position[0] - 1, position[1] - 2]
    elif index == 7:
       # if can_move([position[0] + 1, position[1] + 2], path, width, height):
        return [position[0] + 1, position[1] + 2]
    elif index == 8:
       # if can_move([position[0] + 1, position[1] - 2], path, width, height):
        return [position[0] + 1, position[1] - 2]
    else:
        return None

def solve(path, width, height):

    position = [0, 0]
    path.append(position)

    while not is_complete(path, width, height):

        i = 1

        while i < 9 and not can_move(get_next_positions(position, i), path, width, height):

            i = i+1

        position = get_next_positions(position, i)
        path.append(position)

    return path

#--------------------------------Testprogramm--------------------------------------

width = 4
height = 5
path = []

print(solve(path, width, height))
# Ausgabe:[[0, 0], [2, 1], [0, 2], [2, 3], [0, 4], [1, 2], [3, 3], [1, 4], [2, 2], [0, 3], [2, 4], [3, 2]]