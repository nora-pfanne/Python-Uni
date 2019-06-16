# Klasse "Token"
class Token:

    # Konstruktor
    # Legt einen Token mit einem Eintrag an, der auf sich selbst zeigt.
    def __init__(self, value):
        self.value = value
        self.next = self

    # Liefert das nächste Token zum aktuellen Token
    def next(self):
        return self.next

    # Fügt ein Elemnt zum Tokenring hinzu, welches direkt hinter dem aktuellen liegt.
    def add_next(self, value):
        temp = self.next
        new_token = Token(value)
        self.next = new_token
        new_token.next = temp

    # Löst das aktuelle Element aus dem Tokenring heraus, wobei dies nur möglich sein soll, wenn noch weitere Elemente in dem Tokenring enthalten sind.
    def detach(self):
        if self.next != self:
            temp = self.next
            current_position = self
            while self != current_position.next:
                current_position = current_position.next
            current_position.next = temp
        else:
            return None

    # Wandelt einen Tokenring in die Liste der Elemente um.
    def to_list(self):
        position = self
        list = []
        list.append(position.value)
        while position.next != self:
            position = position.next
            list.append(position.value)
