# Smartkonstruktoren
def empty_deque():
    hole = {}
    return [hole, hole]

def is_empty(q) :

    q_empty = empty_deque()

    if q == empty_deque():
        return True
    else:
        return False


# Prozedur aus der Vorlesung
def enqueue_back(v, q):
    new_hole = {}
    hole = q[1]
    hole['value'] = v
    hole['next'] = new_hole
    q[1] = new_hole

# Variante von enqueue(v, q)
def enqueue_front(v, q):

    # Ursprüngliche Werte speichern
    old_deque_value = q[0]['value']
    old_deque_next = q[0]['next']

    # Pointer
    noch_ein_hole = {}

    # alte Werte an den hinteren Teil der Deque ablegen
    noch_ein_hole['value'] = old_deque_value
    noch_ein_hole['next'] = old_deque_next

    # neue Werte vorne anfügen
    new_hole = {}
    hole = q[0]
    hole['value'] = v
    hole['next'] = noch_ein_hole
    q[1] = new_hole

def dequeue_back(q1):

    temp_deque = empty_deque()

    if is_empty(q):
        value = q[0]['value']
        q[0] = q[0]['next']
    else:
        enqueue_back(dequeue_front(q), temp_deque)
        value = dequeue_back(q)


    return value

# Prozedur aus der Vorlesung
def dequeue_front(q):
    value = q[0]['value']
    q[0] = q[0]['next']
    return value


#Hauptprogramm

# Initialisierung einer Test-Deque
q = empty_deque()
print(q)

# Test der neuen Prozeduren
enqueue_back(2,q)
enqueue_back(3,q)
enqueue_back(4,q)

# Ergebnisausgabe
print(q)
print(dequeue_back(q))
print(q)

