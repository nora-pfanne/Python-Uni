# Smartkonstruktoren für binäre Bäume
# Verstecken die Implementierung der Bäume als Arrays

def node(l, v, r):
    return [l,v,r]

def empty() :
    return []

def left(list) :
    return list[0]

def right(list) :
    return list[2]

def value(list) :
    return list[1]

def is_empty(tree):
    return tree == []

def empty_to_value(tree ,v):
    if tree == [] :
        tree.extend([empty() ,v ,empty()])

def value_to_empty(tree):
    if tree != []:
        return []

# ----Funktionen auf Suchbäumen----

def empty_st() :
    return empty()

def lookup(v ,tree) :
    if is_empty(tree) :
        return False
    if v < value(tree) :
        return lookup(v ,left(tree))
    elif v > value(tree) :
        return lookup(v ,right(tree))
    else :
        return v == value(tree)

def insert(v, tree) :
    if is_empty(tree) :
        empty_to_value(tree ,v)
        return True
    if v < value(tree) :
        return insert(v ,left(tree))
    elif v > value(tree) :
        return insert(v ,right(tree))
    else :
        return False

# Hausübung

def list_to_search_tree(l):

    # nehmen die mittlere Zahl als Wurzel unseres Baumes, da die Liste ja sortiert ist.
    wurzel = l[len(l )//2]

    # Erstellung des Baumes nur mit der Wurzel
    tree = node(empty() ,wurzel ,empty())

    # Einfügen der restlichen Elemente mit insert
    for i in range(len(l)):
        insert(l[i], tree)

    return tree

def search_tree_to_list(tree):



    if is_empty(left(tree)) == False and is_empty(right(tree)) == False:

        liste = search_tree_to_list(left(tree)) + [value(tree)] + search_tree_to_list(right(tree))

    elif is_empty(left(tree)) == False and is_empty(right(tree)) == True:

        liste = search_tree_to_list(left(tree)) + [value(tree)]

    elif is_empty(left(tree)) == True and is_empty(right(tree)) == False:

        liste = [value(tree)] + search_tree_to_list(right(tree))

    else:

        liste = [value(tree)]

    return liste


# Definition der Funktion Sort, welche eine Liste sortiert
def sort(list) :

    if len(list) != 0:

        # Für die Sortierung wird ein Quicksort verwendet
        return quicksort(list, 0, len(list)-1)

# Sortierung eines Baumes wird auf die Liste zurückgeführt
def sort(tree) :

    list_to_search_tree(sort(search_tree_to_list(tree)))

def quicksort(list, start, end):

    if len(list) > 1:

        # Da immer die ganze Liste sortiert wird, werden die Grenzen auf das erste und das letzte Element gesetzt
        pivot = list[start]
        left = start
        right = end

        while left <= right:

            # alle Elemente links vom betrachteten Wert sind bereits kleiner
            while list[left] < pivot:
                left += 1

                # alle Elemente rechts vom betrachteten Wert sind bereits größer
                while list[right] > pivot:
                    right -= 1

                if left <= right:

                    if left < right:
                        temp = list[left]
                        list[left] = list[right]
                        list[right] = temp

                    left += 1
                    right -= 1

                    if right < 0:
                        right = 0

            # rekursiver Aufruf für die unsortierten Teile der Liste
            if start < right:
                list = quicksort(list, start, right)
            if left < end:
                list = quicksort(list, left, end)

    return list


# Hauptprogramm:

tree = list_to_search_tree([1 ,2 ,3 ,4 ,5 ,6])

print(tree)

tree1 = [[[], 1, [[], 2, [[], 3, []]]], 4, [[], 5, [[], 6, []]]]

print(search_tree_to_list(tree1))