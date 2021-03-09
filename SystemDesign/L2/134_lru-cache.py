class SinglyLinkedListNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.key_to_prev = {}
        self.dummy = SinglyLinkedListNode("dummy")
        self.tail = self.dummy
        self.capacity = capacity

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if key not in self.key_to_prev.keys():
            return -1

        prev_node = self.key_to_prev[key]
        curr_node = prev_node.next
        self.kick(prev_node)
        return curr_node.value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        if key not in self.key_to_prev.keys():
            new_node = SinglyLinkedListNode(key=key, value=value)
            self.push_back(new_node)
            if len(self.key_to_prev) > self.capacity:
                self.pop_front()
        else:

            prev_node = self.key_to_prev[key]
            self.kick(prev_node)
            self.key_to_prev[key].next.value = value

    # prev --> node --> next .....--->tail
    # prev --> next --->.... -->tail --> node
    def kick(self, prev_node):
        curr_node = prev_node.next
        next_node = curr_node.next
        if curr_node == self.tail:
            return
        prev_node.next = curr_node.next
        self.key_to_prev[next_node.key] = prev_node
        curr_node.next = None
        self.push_back(curr_node)

    def push_back(self, node):
        self.tail.next = node
        self.key_to_prev[node.key] = self.tail
        self.tail = node

    def pop_front(self):
        head_node = self.dummy.next
        del self.key_to_prev[head_node.key]
        self.dummy.next = head_node.next
        self.key_to_prev[head_node.next.key] = self.dummy



