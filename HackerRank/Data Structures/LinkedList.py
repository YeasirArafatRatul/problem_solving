class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        # head node will never contain any actual data and it's not going to be indexable;
        self.head = node()
        # User isn't going to be able to access this head node

    # append fuction(to insert data)
    def append(self, data):
        # new node of class node and passig the data that user has entered
        new_node = node(data)
        current_node = self.head  # because we are starting with head or first node
        while current_node.next != None:  # when "next" of a node is "None" then it will be the last node
            # changing the current node to that node which is indicated by the "next" of the current node
            current_node = current_node.next
        # if we are at the last element of the list then our new_node will be the vlaue indicated by current_node's "next"
        current_node.next = new_node

    def length(self):
        current_node = self.head
        total = 0
        while current_node.next != None:
            total += 1
            current_node = current_node.next
        return total

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    def get(self, index):
        # check the index number is present in the linked list
        if index >= self.length():
            print("Error: 'index is out of length'")
            return None
        current_index = 0
        current_node = self.head
        # begin the iteration for searching the index(users input) through the linkedlist's indexes.
        while True:
            current_node = current_node.next
            if current_index == index:  # 'index' user's input
                                # if the index(users input) is present in the linkedlist's index then pass the data of that index
                return current_node.data
            current_index += 1

    def delete(self, index):
        if index >= self.length():
            print("Error : Index doesn't present ")

        current_index = 0
        current_node = self.head
        # begin the iteration for searching the index(users input) through the linkedlist's indexes.
        while True:
            last_node = current_node
            current_node = current_node.next
            # if the user provided index no is equal to the current_node's index then
            if current_index == index:
                                # last_node's 'next' will be the value of current_node's 'next' i.e the loop will stop going further

                last_node.next = current_node.next
                return
            current_index += 1


my_list = linkedList()  # object of the class

my_list.append(1)  # object inheriting the properties of the class

my_list.append(4)

my_list.append(3)
my_list.append(6)

print(my_list.length())
print(my_list.get(2))

my_list.display()

print(my_list.delete(2))
my_list.display()
