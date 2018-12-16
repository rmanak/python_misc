
class Node:
    """
    Node object for a linked list class
    """
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, next_):
        self.next = next_

    def get_next(self):
        return self.next

    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val = val

class LinkedList:
    """
    A simple implementation of Linked List
    """
    def __init__(self):
        self.head = None

    def add(self, val):
        tmp_ = Node(val)
        tmp_.set_next(self.head)
        self.head = tmp_

    def _get_vals(self):
        curr = self.head
        while curr is not None:
            yield curr.get_val()
            curr = curr.get_next()

    def size(self):
        count = 0
        iterator = self._get_vals()
        for _ in iterator:
            count += 1

        return count

    def __len__(self):
        return self.size()

    def __iter__(self):
        return self._get_vals()

    def search(self, target_val):
        iterator = self._get_vals()
        for val in iterator:
            if val == target_val:
                return True
        return False

    def remove(self, target_val):
        curr = self.head
        previous = None
        while curr is not None:
            curr_val = curr.get_val()
            if curr_val == target_val:
                break
            previous = curr
            curr = curr.get_next()
        if curr is None:
            print("item not found for removal")
            return None

        if previous is None:
            self.head = curr.get_next()
            return None

        previous.set_next(curr.get_next())

mylist = LinkedList()
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(5)
print(mylist.size())
print(mylist.search(5))
print(mylist.search(4))
print(mylist.remove(3))
print(mylist.remove(5))
print(len(mylist))
print(list(mylist))
for x in mylist:
    print(x)


