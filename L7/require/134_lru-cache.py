# 使用java版本的解法，使用hash table以及doubly linked list，然後雙向鏈表的頭尾都是dummy node
# 好處是可以縮短兩個子函數,_remove_node(node), _move_to_tail(node)的程式碼，
# 假設self.tail不使用dummy node的話，使用的是self.tail = self.head這樣的方式
# 在_remove_node(node)以及_move_to_tail(node)這兩個函式中，就需要判別移除的node是否為tail，然後分別處理
# 若是移除的node在tail的話，則不用移除以及移動，若不是在tail，則需要移除以及移動


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = dict()
        self.head = Node(0, 0)  # dummy node
        self.tail = Node(0, 0)  # dummy node
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

            node = Node(key, value)
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