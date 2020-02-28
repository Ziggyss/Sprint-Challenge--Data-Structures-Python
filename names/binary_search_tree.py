from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # LEFT CASE

        # check if our new node's value is less than the current node's value
        if value <= self.value:
        # does it have a child to the left?
            if self.left == None:
        # place our new node here
                self.left = BinarySearchTree(value) 
        # otherwise
            else:   
        # repeat process for the left (recursive?)
                self.left.insert(value)
        # RIGHT CASE
        # check if the new node's value >= current node's value
        if value >= self.value:
        # does it have a child to the right?
            if self.right == None:
        # if not, place new node here
                self.right = BinarySearchTree(value)
        # otherwise
            else:
        # repeat process for the right
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # BASE CASE
        if target == self.value:
            return True

        # LEFT CASE
        elif target < self.value:
            if self.left != None:
                return self.left.contains(target)

        # RIGHT CASE
        elif target > self.value:
            if self.right != None:
                return self.right.contains(target)
    

    # Return the maximum value found in the tree
    def get_max(self):
        # BASE CASE
        # if empty tree
        if self.value == None:
            return None
        # return none
        # recursive case
        # if there is no right value
        if self.right == None:
            return self.value
        # return the root node value
        # otherwise
        else:
            return self.right.get_max()
        # return get max of right hand child
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #BASE CASE - empty tree
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        cb(self.value) 
    # Question for Pascal: when I tried to return on line 78 and 80, the tests fail. In previous methods return is needed on the recursive functions but I don't fully understand why it is used there and in other cases not.         

    def dft_for_each_i(self, cb):
        #Create an empty stack
        stack = Stack()
        # push self onto stack
        stack.push(self)

        # iterate over the stack
        while stack.len() > 0:
            # pop the stack off into current node
            current_node = stack.pop()
            # check if node to left
            if current_node.left: 
                # push the current node's left child onto the stack
                stack.push(current_node.left)

            # check if node to right
            if current_node.right:
                # push the node to the right onto the stack
                stack.push(current_node.right)
            # invoke callback on the value of the current node 
            cb(current_node.value)

    def bft_for_each_i(self, cb):
        #Create an empty stack
        q= Queue()
        # push self onto stack
        q.enqueue(self)

        # iterate over the stack
        while q.len() > 0:
            # pop the stack off into current node
            current_node = q.dequeue()
            # check if node to left
            if current_node.left: 
                # push the current node's left child onto the stack
                q.enqueue(current_node.left)

            # check if node to right
            if current_node.right:
                # push the node to the right onto the stack
                q.enqueue.push(current_node.right)
            # invoke callback on the value of the current node 
            cb(current_node.value)





    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        current_node = node
        if current_node.left:
            self.in_order_print(current_node.left)
        print(current_node.value)    
        if current_node.right:
            self.in_order_print(current_node.right) 
        # print(current_node.value)   
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        
    # Create an empty queue
        q = Queue()
    # Add the starting node to the queue
        q.enqueue(node)

    # Iterate over the queue
        while q.len() > 0:
        # set the current_node to the first item in the queue
            current_node = q.dequeue()  
        # the print the current value
            print(current_node.value)
        # if the current node has a left child
            if current_node.left:
            # call enqueue on the current left
                q.enqueue(current_node.left)
        # if the current node has a right child
            if current_node.right:
            # call enqueue on the current right
                q.enqueue(current_node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Create an empty stack
        s = Stack()
    # Add the starting node to the stack
        current_node = s.push(node)

    # Iterate over the stack
        while s.len() > 0:
        # set the current_node to the first item in the stack
            current_node = s.pop()
        # the print the current value
            print(current_node.value)
        # if the current node has a left child
            if current_node.left:
            # call push on the current left
                s.push(current_node.left)
        # if the current node has a right child
            if current_node.right:
            # call push on the current right
                s.push(current_node.right)
        
       

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        current_node = node 
        print(current_node.value)  
        if current_node.left:
            self.pre_order_dft(current_node.left)  
        if current_node.right:
            self.pre_order_dft(current_node.right) 

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        current_node = node 
        if current_node.left:
            self.post_order_dft(current_node.left)  
        if current_node.right:
            self.post_order_dft(current_node.right) 
        print(current_node.value)      


