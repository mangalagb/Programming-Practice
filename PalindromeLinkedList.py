class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = Node()

    def get_head(self):
        return self.head

    def insert_end(self, data):
        new_node = Node(data, None)

        if self.head.data is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_node

    def insert_begin(self, data):
        new_node = Node(data, None)

        if self.head.data is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data,end="  ")
            current = current.next
        print("\n________________________________________")



def find_if_list_is_palindrome():
    my_list = create_list()
    middle = find_middle_of_list(my_list)
    second_half_list_in_reverse = reverse_second_half_of_list(middle)
    #second_half_list_in_reverse.print_list()

    original_list_current = my_list.get_head()
    reversed_list_current = second_half_list_in_reverse.get_head()

    while reversed_list_current is not None:
        if original_list_current.data != reversed_list_current.data:
            return False
        else:
            original_list_current = original_list_current.next
            reversed_list_current = reversed_list_current.next
    return True




def reverse_second_half_of_list(middle):
    current = middle
    second_half_list = LinkedList()

    while current is not None:
        second_half_list.insert_begin(current.data)
        current = current.next
    return second_half_list

def find_middle_of_list(my_list):
    current = my_list.get_head()
    middle = my_list.get_head()
    counter = 0

    while current.next is not None:
        if counter % 2 == 0:
            middle = middle.next
        current = current.next
        counter += 1
    return middle

def create_list():
    my_list = LinkedList()
    my_list.insert_end(5)
    my_list.insert_end(8)
    my_list.insert_end(8)
    my_list.insert_end(5)
    return my_list

print(find_if_list_is_palindrome())


