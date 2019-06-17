'''
Gesetze:

is_empty(empty_tree()) => True

is_empty(node(left_tree, right_tree)) => False

left(node(left_tree, right_tree)) => left_tree

right(node(left_tree, right_tree)) => right_tree

left(empty_tree) => None
'''
# ------------------------Präsenzübung---------------------------
def empty_tree():
    # Ein einzelnes, leeres Blatt oder die Wurzel eines Baumes.
    return {}


def is_empty_tree(tree):
    return tree == {}


def node(left_tree, right_tree):
    return {"left": left_tree,
            "right": right_tree}


def left(tree):
    if is_empty_tree(tree):
        return None
    else:
        return tree["left"]


def right(tree):
    if is_empty_tree(tree):
        return None
    else:
        return tree["right"]
'''
Gesetze:

height(empty_tree) => 0

size(empty_tree) => 0

height(full_bintree(depth)) => depth

height(cut_bintree(tree, depth)) => depth

height(balanced_bintree(size)) <= log2(size)
'''
#------------------------------Übung-------------------------------
# Gibt die Anzahl der Elemente eines Binärbaumes zurück.
def size(tree):
    if is_empty_tree(tree):
        return 0
    else:
        return 1 + size(left(tree)) + size(right(tree))

# Gibt die Höhe eines Binärbaumes zurück.
def height(tree):
    if is_empty_tree(tree):
        return 0
    else:
        if size(left(tree)) >= size(right(tree)):
            return 1 + height(left(tree))
        else:
            return 1 + height(right(tree))
def height(tree):
    stack = [[tree,0]]
    max_height = 0

    while len(stack) > 0:
        tree1 = stack[-1][0]
        height_left = stack[-1][1]

        while not is_empty_tree(tree1):
            height_left = height_left + 1
            stack.append([right(tree1), height_left])
            tree1 = left(tree1)
        if height_left > max_height:
            max_height = height_left



# Erstellt einen vollständigen Baum mit der Höhe depth und gibt diesen zurück.
def full_bintree(depth):
    if depth == 0:
        return {}
    else:
        return node(full_bintree(depth-1), full_bintree(depth-1))


# Erstellt einen ausgeglichenen Baum mit Höhe depth und gibt diesen zurück.
def balanced_bintree(size):
    if size == 0:
        return {}
    else:
        left_elems = size / 2
        right_elems = size - left_elems
        return node(balanced_bintree(left_elems), balanced_bintree(right_elems))

# Schneidet einen Binärbaum auf der Höhe depth an.
def cut_bintree(tree, depth):
    if depth == 0:
        return {}, [left(tree), right(tree)]
    else:
        new_left, list_left = cut_bintree(left(tree), depth-1)
        new_right, list_right = cut_bintree(right(tree), depth-1)
        return node(new_left, new_right), list_left + list_right


# -------------------------------------Testprogramm--------------------------------------------

empty_tree = {}
bintree = full_bintree(5)

print(height(empty_tree))                   #0
print(size(empty_tree))                     #0
print(height(full_bintree(3)))              #3
print(height(cut_bintree(bintree, 4)[0]))   #4
