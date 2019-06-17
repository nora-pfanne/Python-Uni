# Klasse "Token"
class Token:

    # Konstruktor
    # Legt einen Token mit einem Eintrag an, der auf sich selbst zeigt.
    def __init__(self, value):
        self.value = value
        self.next_element = self

    # Liefert das nächste Token zum aktuellen Token
    def next(self):
        return self.next_element

    # Fügt ein Elemnt zum Tokenring hinzu, welches direkt hinter dem aktuellen liegt.
    def add_next(self, value):
        temp = self.next_element
        new_token = Token(value)
        self.next_element = new_token
        new_token.next_element = temp

    # Löst das aktuelle Element aus dem Tokenring heraus, wobei dies nur möglich sein soll, wenn noch weitere Elemente in dem Tokenring enthalten sind.
    def detach(self):
        if self.next_element != self:
            temp = self.next_element
            current_position = self
            while self != current_position.next_element:
                current_position = current_position.next_element
            current_position.next_element = temp
        else:
            return None

    # Wandelt einen Tokenring in die Liste der Elemente um.
    def to_list(self):
        position = self
        token_list= []
        token_list.append(position.value)
        while position.next != self:
            position = position.next
            token_list.append(position.value)
        return token_list

#-----------------------------------Testprogramm----------------------------------------------------

test_token = Token(42)
test_token.add_next(73)
print(test_token.next().value)      #73
print(test_token.value)             #42
test_token.detach()
print(test_token.next().value)      #73