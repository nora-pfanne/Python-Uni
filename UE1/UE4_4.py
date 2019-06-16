# Konstruktor des ADT
def empty_deque():
    return []

# Operationen des ADT
def enqueue_front(v, de):
    return [v]+de

def enqueue_back(v, de):
    return de+[v]

# Selektoren des ADT
def dequeue_front(de):
    if is_empty(de):
        return None
    else:
        return de[1:]

def dequeue_back(de):
    if is_empty(de):
        return None
    else:
        return de[:len(de)-1]

def look_up(de,v):
    for i in range(len(de)):
        if de[i] == v:
            return True
    return False

def is_empty(de):
    return de == []

# Testprogramm
deque0 = empty_deque()
deque1 = enqueue_front(3, deque0)
deque2 = enqueue_front(2, deque1)
deque3 = enqueue_front(1, deque2)
deque4 = enqueue_back(4, deque3)

print(deque4) #[1, 2, 3, 4]

print(look_up(deque4, 5)) # False

deque5 = dequeue_front(deque4)
deque6 = dequeue_back(deque5)

print(deque6) #[2, 3]