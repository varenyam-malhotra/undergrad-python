# Binary search tree
class Node:
    
    '''
    Node objects that are members of a heap
    '''
    
    def __init__(self, key, data):
        '''
        Method to initialize a Node object
        
        Each node object has two attributes
        
        Parameters
        ----------
        key  : Priority value of each node (integer)
        data : Data correspending to each key (any object)
        
        Returns
        -------
        None.

        '''

        # Key for each node is a positive number
        self.key         = key

        # Any object which contains some info corresponding to key
        self.data        = data

        # References to parent, left and right nodes
        self.parent      = None
        self.child_left  = None
        self.child_right = None

        return

    def __str__(self):
        '''
        Generates user friendly output of Node object
        

        Returns
        -------
        TYPE string
            Prints key value of each node.

        '''
        return 'Key: ' + str(self.key) 

    def __repr__(self):

        return self.__str__()



    
class BinaryHeap:
    '''
    Class definition for binary max heap
    Each node in the heap is a Node object
    '''
    def __init__(self, keys = None, data = None):
        '''
        Initialize a binary max heap object

        Parameters
        ----------
        keys : list of integer objects, optional
            DESCRIPTION. Used to set key of each node in heap
        data : list of (any type) objects, optional
            DESCRIPTION. Used to set corresponding data of each node in heap.

        Returns
        -------
        None.

        '''
        
        # Initializing an empty binary tree
        if keys is None:

            # Empty binary heap
            self.heapsize = 0

        else:

            if data is None:
                self.nodes     = [Node(n, 0) for n in keys]
            else:
                
                if len(keys) != len(data):
                    raise ValueError('No of keys must be equal to number of data objects')
                
                self.nodes     = [Node(k, d) for k,d in zip(keys, data)]
            
            # Set size of heap    
            self.heapsize  = len(self.nodes)
            
            # Rearrange nodes such that the heap property is obeyed
            self.build_max_heap()

            
    @staticmethod
    def _parent(i):
        '''
        Return index of parent of node i
        '''
        return (i-1)//2
    
    @staticmethod
    def _left(i):
        '''
        Return index of left child of node i
        '''
        return 2*i + 1
    
    @staticmethod
    def _right(i):
        '''
        Return index of right child of node i
        '''
        return 2*i + 2


    def _swap_nodes(self, i, j):
        '''
        Swap nodes i and j in heap

        Parameters
        ----------
        i : integer
            index value in heap.
        j : integer
            index value in heap.

        Returns
        -------
        None.

        '''

        temp_i, temp_j = self.nodes[i], self.nodes[j]
                
        self.nodes[i]  = temp_j
        self.nodes[j]  = temp_i

            

            
    def maximum(self):
        '''
        Lookup the node with highest key and corresponding key

        Returns
        -------
        TYPE integer 
            the largest key in the heap
        TYPE type of data object
            Data stored in the node with the largest key.

        '''

        # Node with highest key is at index postion 0
        return (self.nodes[0].key, self.nodes[0].data)
    

    def pop_max(self):
        '''
        Pop (remove) the node with highest key and corresponding key
        and update the binary heap

        Returns
        -------
        TYPE integer 
            the largest key in the heap
        TYPE type of data object
            Data stored in the node with the largest key.

        '''

        if self.heapsize==0:
            raise IndexError ('No elements in heap to pop')

        # Node with highest key is at index postion 0
        max_node = self.nodes[0]

        # Swap this node with the last node in the heap
        self._swap_nodes(0, self.heapsize-1)
        
        # Remove last node
        _ = self.nodes.pop()
        
        # Update heap size
        self.heapsize -= 1

        # Reset the binary heap starting from node 0
        self.max_heapify(0)
        
        return (max_node.key, max_node.data)

  
    def build_max_heap(self):
        '''
        Goes through the nodes list and organizes it such that the 
        elements of list obey the heap property

        Returns
        -------
        None.

        '''        
        """
        Write your code here
        """
            
    def max_heapify(self, i = 0):
        '''
        Make sure node i obeys the heap property

        Parameters
        ----------
        i : integer, optional
            DESCRIPTION. The default is 0.

        Returns
        -------
        None.

        '''
        
        """
        Write your code here
        """
            


    def insert(self, key, data):
        '''
        Insert a new ndoe into the heap

        Parameters
        ----------
        key : integer
            key value of new node to be insert.
        data : 
            data to be stored in the new node

        Returns
        -------
        None.

        '''
        # Create new node with key = -1
        node = Node(-1, data)

        # Update heap size
        self.heapsize += 1

        # Add key to end of nodes list
        self.nodes.append(node)

        # Update key of new node and reset heap
        self.heap_increase_key(self.heapsize - 1, key)

        
    def heap_increase_key(self, i, key):
        '''
        Modify key value of node i

        Parameters
        ----------
        i : integer
            index of node whose key is being updated.
        key : integer
            new key value.

        Raises
        ------
        KeyError
            Error is raised if new key is less than current key.

        Returns
        -------
        None.

        '''
        if key < self.nodes[i].key:
            raise KeyError ('New Key' +str(i) + 'must be larger than current key ', + str(self.nodes[i].key))
        
        self.nodes[i].key = key

        while i > 0 and self.nodes[self._parent(i)].key < self.nodes[i].key:
            self._swap_nodes(i, self._parent(i))
            i = self._parent(i)
        




# Define heapsort functions

def heapsort_II(item_list, reverse=True):

    '''
    Sort elemts of item_list

    Parameters
    ----------
    item_list : list 
        list that is to be sorted.
    reverse : boolean, optional
        Sorting order is descending by default. 

    Returns
    -------
    sortd : list
        a sorted copy of array in descending order

    '''
    
    # Create a binary heap with the elements of item_list as keys
    bheap = BinaryHeap ( keys = item_list )
    sortd = []

    # Pop one element of the heap at a time
    # and add it to a new list
    while bheap.heapsize>0:
        k, _  = bheap.pop_max()
        sortd.append(k)
    
    if not reverse:
        sortd.reverse()

    return sortd


# A different approach
def heapsort_I(item_list, reverse=False):

    '''
    Sort elemts of item_list

    Parameters
    ----------
    item_list : list 
        list that is to be sorted.
    reverse : boolean, optional
        Sorting order is descending by default. 

    Returns
    -------
    sortd : list
        a sorted copy of array in ascending order

    '''

    # Create a binary heap with the elements of item_list as keys
    bheap = BinaryHeap ( keys = item_list )

    # Iterate from last element to all but first
    for i in range(len(item_list)-1, 0, -1):

        # Swap nodes 0 and the node i (last node)
        bheap._swap_nodes(0,i)
        # Reduce heap size by 1
        bheap.heapsize -= 1
        
        # Since heapsize is reduced by 1
        # Heap property is only obeyed by elements 0 through heapsize-1
        bheap.max_heapify(0)

    # Nodes in the heap are now in ascending order
    # Copy them over to a list
    sortd = [n.key for n in bheap.nodes]

    # If reverse is set to true reverse the list
    if reverse:
        sortd.reverse()

    # Return sorted list
    return sortd



        
