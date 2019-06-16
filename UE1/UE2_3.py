class Stack:

    def __init__(self):
        self.value = None
        self.next = None

    def push(self, value):

        # neuer Stack wird initialisiert
        newStack = Stack()
        newStack.next = self
        newStack.value = value
        return newStack

    def pop(self):

        # dieser Fall bleibt bestehen
        if self.is_empty():
            raise KeyError("pop from empty stack")

        # hier wird wiederum ein neuer Stack initialisiert und ausgegeben
        else:
            newStack = Stack()
            newStack.value = self.next.value
            newStack.next = self.next.next

            # der erste Wert kann nicht mehr zurückgegeben werden
            return newStack

    def top(self):

        # Rückgabe des obersten Wertes
        return self.value

    def is_empty(self):
        return self.next == None

    def to_list(self):
        if self.next == None:
            return []
        else:
            return [self.value] + self.next.to_list()

    def __str__(self):
        elements = [str(s) for s in self.to_list()]
        return ", ".join(elements)


s1 = Stack()
s2 = s1.push(5)
s3 = s2.push(6)
print(s3.top())  # 6
s4 = s3.pop()
s5 = s4.push(9)

print(s5)  # 9, 5
