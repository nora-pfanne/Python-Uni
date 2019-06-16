class Linked:

    # Konstruktor
    def __init__(self):
        self.value = None
        self.next = None

    def is_empty(self):
        return (self.value == None and self.next == None)

    # Text an richtiger Stelle einfügen
    def add(self, text):

        def add_helper(ll, text, parent):
            if ll.is_empty():
                ll.value = text
                ll.next = Linked()

            elif text < ll.value:
                if parent== None:
                    copy_list = ll
                    ll.value = text
                    ll.next = copy_list
                else:
                    new_list = Linked
                    new_list.value = text
                    new_list.next = ll
                    parent.next = new_list
            else:
                add_helper(ll.next, text, ll)

        add_helper(self, text, None)

    # Text löschen
    def delete(self, text):

        def delete_helper(ll, text, parent):
            if ll.is_empty():
                return False
            elif text == ll.value:
                if parent == None:
                    ll.value = ll.next.value
                    ll.next = ll.next.next
                else:
                    parent.next = ll.next
                return True
            else:
                return delete_helper(ll, text, ll.next)

        return delete_helper(self, text, None)

    # Print
    def print__(self):
        ll = self

        while not ll.is_empty():
            print(ll.value)
            ll = ll.next


# Hauptprogramm
l = Linked()


l.add("a: erstes Element")
print(l)
l.add("x: ganz am Ende")
l.add("q: kurz vor'm Ende")
l.add("c: an dritter Position")
l.add("c: an dritter Position") # doppelt einfügen testen
print(l)

print(" +++++ +++++ +++++ ")

print(l.delete("a: erstes Element")) # erstes Element löschen
print(l.delete("x: ganz am Ende")) # letztes Element löschen
print(l.delete("c: an dritter Position")) # mittendrin löschen
print(l.delete("?: mich gibt es nicht in der Liste")) # mittendrin löschen

print(l)
l.delete("c: an dritter Position")
l.delete("q: kurz vor'm Ende")
l.delete("b: zweites Element")

print(l)