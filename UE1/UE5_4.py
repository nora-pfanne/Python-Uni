'''-------------- Konstruktor ------------------------
empty_key

------------ Selektoren/Tests -------------------
is_value(v, x, k)	gibt an, ob ein Wert unter diesem Schlüssel gespeichert wurde
value(x, k)			gibt den Wert unter dem Schlüssel x an
------------ weitere Operationen ----------------
insert(v, x, k)	ein Wert wird unter einem Schlüssel gespeichert
delete(x,k)	der Wert unter dem Schlüssel wird gelöscht


Gesetze

(1) value(x, delete(x, k) = None
(2) value(x, insert(v, x, k)) = v
(3) is_value(v, x, empty_key()) = False
(4) value(x, empty_key()) = None
(5) is_value(v, x, insert(v, x, k)) = True '''


def empty_key():
    return lambda x: None

def is_empty(k):
    return empty_key() == k

def is_value(x, v, k):
    return k(x) == v

def value(x, k):
    return k(x)

def insert(v, x, k):
    return lambda y: v if x == y else k(y)

def delete(v, k):
    return lambda x: None if k(x) == v else k(x)

#---------------------Testprogramm---------------------

key = empty_key()

# der Wert 6 wird unter dem Schlüssel 3 gespeichert
insert(6, 3, key)

# Prüfen von Gesetz (1)
print(value(3, delete(3, key))) # None

# Prüfen von Gesetz (2)
print(value(2, insert(6, 2, key))) # 6

# Prüfen von Gesetz (3)
print(is_value(5, 2, empty_key())) # False

# Prüfen von Gesetz (4)
print(value(5, empty_key())) # None

# Prüfen von Gesetz (5)
print(is_value(3, 3, insert(3, 3, key))) # True
