class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Display(self):
        present = self.head
        while present:
            print(present.data)
            present = present.link
        print('')

    def InsertStart(self, data):
        new = Node(data)
        new.link = self.head
        self.head = new

    def InsertIndex(self, index, data):
        if index == 0:
            self.InsertStart(data)
        else:
            present, previous = self.head, None
            for i in range(index):
                previous = present
                if present.link:
                    present = present.link
                else:
                    self.InsertEnd(data)
                    return
            new = Node(data)
            previous.link = new
            new.link = present

    def InsertEnd(self, data):
        if self.head:
            present = self.head
            while present.link:
                present = present.link
            present.link = Node(data)
        else:
            self.head = Node(data)

    def DeleteEnd(self):
        if self.head:
            present = self.head
            while present.link:
                previous = present
                present = present.link
            previous.link = None

    def DeleteStart(self):
        new = self.head.link
        self.head = None
        self.head = new

    def DeleteIndex(self, index):
        present = self.head
        for i in range(index):
            previous = present
            present = present.link
        previous.link = present.link

    def DeleteFound(self, data):
        present = self.head
        while present:
            if not present.link:
                return None
            if present.data == data:
                break
            previous = present
            present = present.link
        previous.link = present.link

    def DeleteList(self):
        self.head = None

    def ListLengthI(self):
        present = self.head
        count = 0
        while present:
            present = present.link
            count += 1
        return count

    def ListLengthR(self, point):
        if point:
            return 1 + self.ListLengthR(point.link)
        return 0

    def SearchI(self, data):
        present = self.head
        while present:
            if present.data == data:
                return True
            present = present.link
        return False

    def SearchR(self, point, data):
        if point:
            if point.data == data:
                return True
            else:
                return self.SearchR(point.link, data)
        return False

    def ReturnIndexI(self, index):
        present = self.head
        for i in range(index):
            present = present.link
        print(present.data)

    def ReturnIndexR(self, point, index):
        count = 0
        if point:
            if count == index:
                print(point.data)
            else:
                self.ReturnIndexR(point.link, index-1)
        else:
            print("doesn't exist")
