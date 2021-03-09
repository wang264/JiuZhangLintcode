# 使用java版本的解法，使用hash table以及doubly linked list，然後雙向鏈表的頭尾都是dummy node
# 好處是可以縮短兩個子函數,_remove_node(node), _move_to_tail(node)的程式碼，
# 假設self.tail不使用dummy node的話，使用的是self.tail = self.head這樣的方式
# 在_remove_node(node)以及_move_to_tail(node)這兩個函式中，就需要判別移除的node是否為tail，然後分別處理
# 若是移除的node在tail的話，則不用移除以及移動，若不是在tail，則需要移除以及移動


class DoublyLinkedListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        if self is None:
            return "EmptyNode"

        if self.prev:
            prev = self.prev.key
        else:
            prev = 'None'
        if self.next:
            ne_xt = self.next.key
        else:
            ne_xt = 'None'

        return f"[key:{self.key} prev:{prev} next:{ne_xt}"


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = dict()
        self.head = DoublyLinkedListNode(0, 0)  # dummy node
        self.tail = DoublyLinkedListNode(0, 0)  # dummy node
        self.tail.prev = self.head
        self.head.next = self.tail

    def get(self, key):
        if key not in self.hash:
            return - 1

        node = self.hash[key]
        self._remove_node(node)
        self._move_to_tail(node)

        return node.value

    def set(self, key, value):
        if key in self.hash:
            self.hash[key].value = value  # uddate value if value is changed
            node = self.hash[key]
            self._remove_node(node)
        else:
            if len(self.hash) == self.capacity:
                del self.hash[self.head.next.key]
                self.head.next = self.head.next.next
                self.head.next.prev = self.head

            node = DoublyLinkedListNode(key, value)
            self.hash[key] = node

        self._move_to_tail(node)

    def _move_to_tail(self, node):
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        node.next = self.tail

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


class SinglyLinkedListNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache2:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.key_to_prev = {} # dictionary that map key to the repected node's previous node.
        self.dummy = SinglyLinkedListNode("dummy")
        self.tail = self.dummy # point to the last node the linked list
        self.capacity = capacity # capacity of the cache

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # if we never cache that, return -1
        if key not in self.key_to_prev.keys():
            return -1

        prev_node = self.key_to_prev[key]
        curr_node = prev_node.next
        # giving the previous node, move the next node of the previous node to the tail of the linked list.
        self.kick(prev_node)

        return curr_node.value
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # if we have never seen it before
        if key not in self.key_to_prev.keys():
            # create node and add to the end of linked list
            new_node = SinglyLinkedListNode(key=key, value=value)
            self.push_back(new_node)
            # if exceed capacity, we pop the first node.
            if len(self.key_to_prev) > self.capacity:
                self.pop_front()

        # if we seen this node before
        else:
            # using the 'kick' function to kick this node to the tail of the list
            prev_node = self.key_to_prev[key]
            self.kick(prev_node)
            self.key_to_prev[key].next.value = value

    # providing the 'prev'.....'kick' the current 'node' to the tail.

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

    # insert to tail
    def push_back(self, node):
        self.tail.next = node
        self.key_to_prev[node.key] = self.tail
        self.tail = node

    # delete the first node.
    def pop_front(self):
        head_node = self.dummy.next
        del self.key_to_prev[head_node.key]
        self.dummy.next = head_node.next
        self.key_to_prev[head_node.next.key] = self.dummy


