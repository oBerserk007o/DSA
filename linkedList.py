class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None


    def insert(self, data, index=0):
        if index == 0:
            node = Node(data, self.head)
            self.head = node
            return

        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        i = 0
        while itr.next:
            if i == index:
                self.head = Node(data, itr.next)
                itr.next = self.head
            else:
                i += 1
            itr = itr.next
        raise IndexError("Index out of range")


    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        msg = ""
        while itr:
            msg += str(itr.data) + (" --> " if itr.next else "")
            itr = itr.next
        print(msg)


    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)


    def insertList(self, dataList, index=None, indexList=None):
        if index is not None:
            for data in dataList:
                self.insert(data, index)
        if indexList is not None:
            if len(indexList) != len(dataList):
                raise IndexError("Index list length does not match data list length")
            for i, data in enumerate(dataList):
                self.insert(data, indexList[i])

        for data in dataList:
            self.append(data)


    def __len__(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        i = 0
        while itr:
            itr = itr.next
            i += 1
        return i


    def pop(self, index=None):
        if index is None:
            index = len(self) - 1
        index = index % len(self)
        if index == 0:
            ...

    def clear(self):
        for _ in range(len(self)):
            self.pop()


if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.insert("WOOO yeah baby")
    linkedList.insert("Ho Ho Ho", 0)
    linkedList.append("Caramba")
    linkedList.insertList([1, 2, 3, 4, 5])
    linkedList.print()

