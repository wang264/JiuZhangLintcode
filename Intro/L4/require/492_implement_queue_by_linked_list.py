# 492. Implement Queue by Linked List
# 中文English
# Implement a Queue by linked list. Support the following basic methods:
#
# 1.enqueue(item). Put a new item in the queue.
# 2. dequeue(). Move the first item out of the queue, return it.
#
# Example
# Example 1:
#
# Input:
# enqueue(1)
# enqueue(2)
# enqueue(3)
# dequeue() // return 1
# enqueue(4)
# dequeue() // return 2
# Example 2:
#
# Input:
# enqueue(10)
# dequeue()// return 10

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        node = ListNode("dummy")
        self.head = node
        self.tail = node
        self.length = 0

    def append_at_end(self, x):
        new_node = ListNode(x)
        self.tail.next = new_node
        self.tail = new_node

        self.length += 1

    def delete_at_front_and_return_val(self):
        if self.length == 0:
            return

        if self.length == 1:
            return_val = self.head.next.val
            self.head.next = None
            self.tail = self.head
            self.length -= 1
            return return_val

        return_val = self.head.next.val

        curr_node = self.head.next
        next_node = curr_node.next

        curr_node.next = None
        del curr_node
        self.head.next = next_node
        self.length -= 1

        return return_val


class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """

    def __init__(self):
        self.linked_list = LinkedList()

    def enqueue(self, item):
        # write your code here
        self.linked_list.append_at_end(x=item)

    """
    @return: An integer
    """

    def dequeue(self):
        # write your code here
        return self.linked_list.delete_at_front_and_return_val()

    def is_empty(self):
        return self.linked_list.length == 0


q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()  # // return 1
q.enqueue(4)
q.dequeue()  # // return 2

q = MyQueue()
q.enqueue(438)
q.dequeue()
q.enqueue(452)
q.enqueue(379)
q.enqueue(884)
q.enqueue(332)
q.enqueue(55)
q.dequeue()
q.enqueue(825)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(983)
q.dequeue()
q.dequeue()
q.enqueue(616)
q.enqueue(66)
