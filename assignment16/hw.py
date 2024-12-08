from typing import List, Any, Dict, Set, Generator

class StaticArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * capacity

    def set(self, index: int, value: int) -> None:
        self.array[index] = value

    def get(self, index: int) -> int:
        return self.array[index]

class DynamicArray:
    def __init__(self):
        self.array = []

    def append(self, value: int) -> None:
        self.array.append(value)

    def insert(self, index: int, value: int) -> None:
        self.array.insert(index, value)

    def delete(self, index: int) -> None:
        self.array.pop(index)

    def get(self, index: int) -> int:
        return self.array[index]

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None



class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size_ = 0

    def append(self, value: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size_ += 1

    def insert(self, position: int, value: int) -> None:
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if self.size_ == 0:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node
        self.size_ += 1

    def delete(self, value: int) -> None:
        current = self.head
        if current and current.value == value:
            self.head = current.next
            if self.head is None:
                self.tail = None
            self.size_ -= 1
            return

        prev = None
        while current and current.value != value:
            prev = current
            current = current.next
        if current:
            prev.next = current.next
            if current.next is None:
                self.tail = prev
            self.size_ -= 1

    def find(self, value: int) -> Node:
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        return self.size_

    def is_empty(self) -> bool:
        return self.size_ == 0

    def reverse(self) -> None:
        prev = None
        current = self.head
        self.tail = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def get_head(self) -> Node:
        return self.head

    def get_tail(self) -> Node:
        return self.tail

class DoubleNode:
    def __init__(self, value: int, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def append(self, value: int) -> None:
        new_node = DoubleNode(value)
        self.size = self.size + 1

    def insert(self, position: int, value: int) -> None:
            if not node:
                return TreeNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

            self = _insert(self, value)

    def delete(self, value: int) -> None:
        temp = self.head
        if(temp.next != None):
            if(temp == value):
                temp.next.prev = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while(temp.next != None):
                    if(temp == value):
                        break
                    temp = temp.next
                if(temp.next):
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    temp.next = None
                    temp.prev = None
                else:
                    temp.prev.next = None
                    temp.prev = None
                return

        if (temp == None):
            return

    def find(self, value: int) -> DoubleNode:
        curr = head
        pos = 0
        while curr is not None and curr.data != x:
            pos += 1
            curr = curr.next
        if curr is None or curr.data != x:
            return -1
        return pos + 1

    def size(self) -> int:
        self.length = 0
        return self.length


    def is_empty(self) -> bool:
        return len(self) == True

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")
    
    def reverse(self) -> None:
        if curr is None:
            return None
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        if curr.prev is None:
            return curr
        return reverse(curr.prev)
    
    def get_head(self) -> DoubleNode:
        self.headNode = 000
        while True:
            try:
                lastNode = Task.objects.get(next=self.headNode)
                self.headNode = lastNode.id
            except Task.DoesNotExist:
                break
    def get_tail(self) -> DoubleNode:
        if head is None:
            return None
        current = head
        while current.next is not None:
            current = current.next
            return current

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value: int):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0
class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node: TreeNode, value: int) -> None:
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def inorder_traversal(self) -> List[int]:
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: TreeNode, result: List[int]) -> None:
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)


def quick_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor
    return elements

def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1,size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left, right)

def merge_two_sorted_lists(a,b):
    sorted_list = []

    len_a = len(a)
    len_b = len(b)

    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1

    while i < len_a:
        sorted_list.append(a[i])
        i+=1

    while j < len_b:
        sorted_list.append(b[j])
        j+=1

    return sorted_list

def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break
    return elements

def shell_sort(arr):
    size = len(arr)
    gap = size//2

    while gap > 0:
        for i in range(gap,size):
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap]>anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2
    return arr