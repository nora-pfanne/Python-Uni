from copy import deepcopy
class Queue:

    def __init__(self):
        self.value = None
        self.next = None

    def enqueue(self, value):

        newQueue = Queue()
        helperQueue = Queue()
        returnQueue = Queue()

        # neues Element wird hinten an die Queue angefügt
        helperQueue.value = value
        helperQueue.next = newQueue
        returnQueue.value = self
        returnQueue.next = helperQueue

        return returnQueue

    def dequeue(self):

        # dieser Fall bleibt bestehen
        if self.is_empty():
            raise KeyError("dequeue from empty queue")

        # hier wird wiederum eine neue Queue initialisiert und ausgegeben
        else:
            newQueue = Queue()
            newQueue.value = self.next.value
            newQueue.next = self.next.next

            # der erste Wert kann nicht mehr zurückgegeben werden
            return newQueue

    def head(self):

        # Rückgabe des obersten Wertes
        if self.next != None:
            return self
        else:
            return self.next.head()

    def is_empty(self):
        return self.next == None

    def to_list(self):
        if self.value == None:

            if self.next == None:
                return []
            else:
                return self.next.to_list()

        else:
            return [self.value] + self.next.to_list()

    def __str__(self):
        elements = [str(s) for s in self.to_list()]
        return ", ".join(elements)


q1 = Queue()
q2 = q1.enqueue(42)
q3 = q2.enqueue(4)
print(str(q3.head())) # 42
q4 = q3.enqueue(4)
q5 = q4.dequeue()
print(q5)  # 4, 4
