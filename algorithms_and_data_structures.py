class queue: 
    def __init__(self): 
        self.values = []
    
    def enqueue(self, n):
        self.values.append(n)
    
    def peek(self): 
        return self.values[0]
    
    def dequeue(self): 
        value = self.values.pop(0)
        return value
    
    def __len__(self): 
        return len(self.values)
    
    def __str__(self): 
        return str(self.values)

class stack: 
    def __init__(self): 
        self.values = []
    
    def push(self, n): 
        self.values.append(n)
        
    def peek(self): 
        return self.values[-1]
    
    def pop(self): 
        value = self.values.pop()
        return value
    
    def __len__(self): 
        return len(self.values)
    
    def __str__(self): 
        return str(self.values)

class node: 
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None
        
    def get_value(self): 
        return self.value

    def get_right(self):
        if self.right: 
            return self.right.value
        else:
            return None
    
    def get_left(self):
        if self.left: 
            return self.left.value
        else:
            return None
    def set_right(self, value): 
        self.right = node(value)

    def set_left(self, value): 
        self.left = node(value)

    def __str__(self): 
        return f"value: {self.value}, left: {self.get_left()}, right: {self.get_right()}"
    
    def __value__(self): 
        return self.value
    
class singly_linked_list: 
    def __init__(self): 
        self.head = None
        self.tail = None
    
    def is_empty(self): 
        return self.head == None
    
    def add(self, value):
        if self.is_empty():
           self.head = node(value)
        else: 
            last_node = self.head
            while last_node.right: 
                last_node = last_node.right
            last_node.right = node(value)
            self.tail = node(value)
            

    def __str__(self): 
        if self.is_empty(): 
            return "List is empty"
        else:
            string = "["
            node = self.head
            while node is not None:
                string += f"{node.get_value()},"
                node = node.right
            return string[:-1] + "]"

class doubly_linked_list: 
    def __init__(self): 
        self.head = None
        self.tail = None
    
    def is_empty(self): 
        return self.head == None and self.tail == None 
    
    def add(self, value):
        if self.is_empty():
           self.head = node(value)
        else: 
            last_node = self.head
            while last_node.right: 
                last_node = last_node.right
            last_node.right = node(value)
            last_node.right.left = last_node
            self.tail = node(value)
            self.tail.left = last_node
            

    def __str__(self): 
        if self.is_empty(): 
            return "List is empty"
        else:
            string = "["
            node = self.head
            while node is not None:
                string += f"{node.get_value()},"
                node = node.right
            return string[:-1] + "]"
                
class tree: 
    def __init__(self, value): 
        self.root = node(value)
        
    def print_tree(self, traversal_type): 
        if traversal_type == "inorder": 
            print(self.inorder_traversal(self.root, []))
        elif traversal_type == "postorder": 
            print(self.postorder_traversal(self.root, []))
        elif traversal_type == "preorder": 
            print(self.preorder_traversal(self.root, []))  
        elif traversal_type == "levelorder" or traversal_type == "level order": 
            print(self.level_order_traversal(self.root))
        elif (traversal_type == "reverse level order" or 
              traversal_type =="reverse levelorder"): 
            print(self.reverse_level_order(self.root))
        else: 
            print('this traversal type is not supported')
         
    def inorder_traversal(self, root, values = []):
        if root is not None: 
            self.inorder_traversal(root.left, values)
            values.append(root.value)
            self.inorder_traversal(root.right, values)
        return values
    
    def postorder_traversal(self, root, values = []): 
        if root is not None: 
            self.postorder_traversal(root.left, values)
            self.postorder_traversal(root.right, values)
            values.append(root.value)
        return values
    
    def preorder_traversal(self, root, values = []): 
        if root is not None: 
            values.append(root.value)
            self.preorder_traversal(root.left, values)
            self.preorder_traversal(root.right, values)
        return values
    
    def level_order_traversal(self, root): 
        QUEUE = queue()
        QUEUE.enqueue(root)
        values = []
        while len(QUEUE) > 0: 
            node = QUEUE.dequeue()
            if node.left is not None: 
                QUEUE.enqueue(node.left)
            if node.right is not None:
                QUEUE.enqueue(node.right)
            values.append(node.value)
        return values
    
    def reverse_level_order(self, root): 
        QUEUE = queue()
        STACK = stack()
        QUEUE.enqueue(root)
        values = []
        while len(QUEUE) > 0: 
            node = QUEUE.dequeue()
            if node.left is not None: 
                QUEUE.enqueue(node.right)
            if node.right is not None:
                QUEUE.enqueue(node.left)
            STACK.push(node.value)
        while len(STACK) > 0: 
            values.append(STACK.pop())
        return values
    
    def bst_adder(self, cur_node, value): 
        if value < cur_node.value:
            if cur_node.left: 
                self.bst_adder(cur_node.left, value)
            else: 
                cur_node.left = node(value)
        else: 
            if cur_node.right: 
                self.bst_adder(cur_node.right, value)
            else: 
                cur_node.right = node(value)
    
    def bst_add(self, value): 
        self.bst_adder(self.root, value)
            
    def height(self, cur_node): 
        if cur_node is None: 
            return -1
        else: 
            return 1 + max(self.height(cur_node.left), self.height(cur_node.right))
        
    def print_height(self): 
        print(f'the height of this tree is {self.height(self.root)}')
        
    def balance(self, cur_node): 
        return self.height(cur_node.left) - self.height(cur_node.right)
    
    def right_rotation(self): 
        ROOT = self.root
        LEFT = self.root.left
        LEFT_RIGHT = self.root.left.right
        self.root = LEFT
        self.root.right = ROOT
        self.root.right.left = LEFT_RIGHT
        
    def left_right_rotation(self): 
        NEW_NODE = self.root.left.right
        self.root.left.left = NEW_NODE
        self.root.left.right = None 
        self.right_rotation()

    def left_rotation(self): 
        ROOT = self.root
        RIGHT = self.root.right
        RIGHT_LEFT = self.root.right.left
        self.root = RIGHT
        self.root.left = ROOT 
        self.root.left.right = RIGHT_LEFT
    
    def right_left_rotation(self): 
        NEW_NODE = self.root.right.left
        self.root.right.right = NEW_NODE
        self.root.right.left = None
        self.left_rotation()
    
    def avl_add(self, value, treshhold = 1): 
        self.bst_add(value)
        self.balance_tree(treshhold)
            
    def balance_tree(self, treshhold): 
        if self.balance(self.root) < -1 * treshhold: 
            if self.root.right.right is not None: 
                self.left_rotation()
            else: 
                self.right_left_rotation()
        elif self.balance(self.root) > treshhold: 
            if self.root.left.left is not None: 
                self.right_rotation()
            else: 
                self.left_right_rotation()

    def search(self, cur_node, value):
        path = ''
        if cur_node.value > value: 
            next_node = cur_node.left
            path += 'left, '
        elif cur_node.value < value: 
            next_node = cur_node.right
            path += 'right, '
        else: 
            return 'this value is the root of the tree'
        while next_node:
            print(next_node)
            if next_node.value > value: 
                next_node = next_node.left
                path += 'left, '
            elif next_node.value < value: 
                next_node = next_node.right
                path += 'right, '
            elif next_node.value == value: 
                return path[:-2]
        return 'value not found in tree'
            
    def print_path(self, value):
        print(f'The path to {value} is: ' + self.search(self.root, value))
    

class sort: 
    import random
    @staticmethod
    def swap(lst, ind1, ind2): 
        val1 = lst[ind1] 
        val2 = lst[ind2]
        lst[ind1] = val2
        lst[ind2] = val1
        return lst
    
    @staticmethod
    def bubble_sort(lst):
        num_swaps = True
        while num_swaps:
            num_swaps = 0
            index = 0
            for i in lst[:-1]:               
                if i > lst[index + 1]:
                    lst = sort.swap(lst, index, index + 1)
                    num_swaps += 1
                index +=1 
            
    @staticmethod
    def quick_sort(lst): 
        LENGTH = len(lst)
        if LENGTH == 0: 
            return []
        elif LENGTH == 1: 
            return lst
        elif LENGTH == 2: 
            if lst[0] <= lst[1]: 
                return lst
            else: 
                return sort.swap(lst, 0, 1)
        PIVOT_IND_INITIAL = sort.random.randint(0,LENGTH - 1)
        pivot = lst[PIVOT_IND_INITIAL]
        lst = sort.swap(lst, 0, PIVOT_IND_INITIAL)
        border_ind = 1
        cur_ind = 2
        while cur_ind < LENGTH: 
            cur_value = lst[cur_ind]
            if cur_value < pivot: 
                lst = sort.swap(lst, cur_ind, border_ind)
                border_ind += 1
            cur_ind += 1
        if lst[border_ind] <= pivot:
            left_partition = lst[1:border_ind + 1]
            right_partition = lst[border_ind + 1:]
        else: 
            left_partition = lst[1:border_ind]
            right_partition = lst[border_ind:]
        return sort.quick_sort(left_partition) + [pivot] + sort.quick_sort(right_partition)

    @staticmethod
    def merge_sort(lst): 
        if len(lst) <= 1: 
            return lst
        MID_IND = int(len(lst) / 2)
        left_half = lst[:MID_IND]
        right_half = lst[MID_IND:]
        sorted_left, sorted_right = sort.merge_sort(left_half), sort.merge_sort(right_half)
        return sort.merge(sorted_left, sorted_right) 

    @staticmethod
    def merge(lst1, lst2):
        if lst1 == []: 
            return lst2
        if lst2 == []: 
            return lst1
        merged_lst = []
        ind1 = 0
        ind2 = 0
        highest_ind1 = len(lst1) - 1
        highest_ind2 = len(lst2) - 1
        while ind1 <= highest_ind1 and ind2 <= highest_ind2:
            if lst1[ind1] < lst2[ind2]:
                merged_lst.append(lst1[ind1])
                ind1 += 1
            else: 
                merged_lst.append(lst2[ind2])
                ind2 += 1 
        while ind2 <= highest_ind2:
                merged_lst.append(lst2[ind2])
                ind2 += 1
        while ind1 <= highest_ind1: 
                merged_lst.append(lst1[ind1])
                ind1 += 1
        return merged_lst
                                     
class graph: 
    def __init__(self):
        self.vertexes = []

    def insert(self, vertex):
        self.vertexes.append(vertex)
    
    def directed_connect(self, vertex1, vertex2, weight):
        '''From vertex 1 to vertex 2'''
        vertex1.connect(vertex2, weight)
        
    def undirected_connect(self, vertex1, vertex2, weight):
        vertex1.connect(vertex2, weight)
        vertex2.connect(vertex1, weight)
        
    def __str__(self):
        string = ''
        for vertex in self.vertexes: 
            string += f'{vertex.ID} with connections {vertex.connected_to} \n'
        return string
    
class vertex: 
    def __init__(self, ID):
        self.ID = ID
        self.connected_to = {}
    
    def connect(self, other, weight):
        if isinstance(other, list):
            SINGLE_DICT = {}
            if len(other) != len(weight):
                raise ValueError('lists should be of same size')
            else: 
                for ID, single_weight in zip(other, weight): 
                    SINGLE_DICT[ID] = single_weight 
        else: 
            SINGLE_DICT = {other:weight}
        self.connected_to.update(SINGLE_DICT)
        
    def __str__(self): 
        return str(self.ID)
    
    def __repr__(self): 
        return self.__str__()

    
if __name__ == '__main__':
	#experiment here
	#example:
	vertex1 = vertex(1)
	vertex2 = vertex(2)
	vertex3 = vertex(3)
	vertex4 = vertex(4)
	graph = graph()
	graph.insert(vertex1)
	graph.insert(vertex2)
	graph.insert(vertex3)
	graph.insert(vertex4)
	graph.directed_connect(vertex1, vertex2, 1)
	graph.directed_connect(vertex2, vertex3, 1)
	graph.directed_connect(vertex3, vertex4, 1)
	graph.directed_connect(vertex4, vertex1, 1)
	graph.undirected_connect(vertex1, vertex3, 5)
	print(graph)






        
  
            
            