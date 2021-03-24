# 493. Implement Queue by Linked List II
# 中文English
# Implement a Queue by linked list. Provide the following basic methods:
#
# push_front(item). Add a new item to the front of queue.
# push_back(item). Add a new item to the back of the queue.
# pop_front(). Move the first item out of the queue, return it.
# pop_back(). Move the last item out of the queue, return it.
# Example
# Example 1：
#
# Input：
# push_front(1)
# push_back(2)
# pop_back() // return 2
# pop_back() // return 1
# push_back(3)
# push_back(4)
# pop_front() // return 3
# pop_front() // return 4
# Example 2：
#
# Input:
# push_front(1)
# pop_front()// return 1

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

    def append_at_front(self, x):
        new_node = ListNode(x)
        new_node.next = self.head.next

        self.head.next = new_node
        self.length += 1
        if self.length == 1:
            self.tail = new_node

    def delete_at_end_and_return_val(self):
        if self.length == 0:
            return
        if self.length == 1:
            return_val = self.head.next.val
            self.head.next = None
            self.tail = self.head
            self.length -= 1
            return return_val

        prev = self.head
        while prev.next != self.tail:
            prev = prev.next
        return_val = self.tail.val
        prev.next = None
        self.tail = prev
        self.length -= 1

        return return_val

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


class Dequeue:

    def __init__(self):
        self.linked_list = LinkedList()
        # do intialization if necessary

    """
    @param: item: An integer
    @return: nothing
    """

    def push_front(self, item):
        # write your code here
        self.linked_list.append_at_front(x=item)

    """
    @param: item: An integer
    @return: nothing
    """

    def push_back(self, item):
        # write your code here
        self.linked_list.append_at_end(x=item)

    """
    @return: An integer
    """

    def pop_front(self):
        # write your code here
        return self.linked_list.delete_at_front_and_return_val()

    """
    @return: An integer
    """

    def pop_back(self):
        return self.linked_list.delete_at_end_and_return_val()


deque = Dequeue()

deque.push_front(1)
deque.push_back(2)
deque.pop_back()
deque.pop_back()
deque.push_back(3)
deque.push_back(4)
deque.pop_front()
deque.pop_front()
