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
        if size(left(tree)) >= size(right()):
            return 1 + height(left(tree))
        else:
            return 1 + height(right(tree))

# Erstellt einen vollständigen Baum mit der Höhe depth und gibt diesen zurück.
def full_bintree(depth):

    # Hilfsfunktion
    def full_bintree_helper(index, tree):
        if index == 0:
            return tree
        else:
            return full_bintree_helper(index-1,node(tree, tree))

    tree = empty_tree()

    return full_bintree_helper(depth, tree)


# Erstellt einen ausgeglichenen Baum mit Höhe depth und gibt diesen zurück.
def balanced_bintree(size):



def cut_bintree(tree, depth):