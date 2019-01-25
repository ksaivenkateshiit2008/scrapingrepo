class HeapNode(object):
    def __init__(self, key, value, heap_index):
        self.key = key
        self.value = value
        self.heap_index = heap_index

class MaxHeap(object):
    """
    Binary MAX HEAP
    """
    def __init__(self):
        self.array = []
        self.heap_size = 0

    def heapsize(self):
        return self.heap_size

    def insert(self, obj):
        parent = self.parent(obj)
        obj.heap_index = self.heap_size
        curnode = obj
        self.array.append(obj)
        self.heap_size += 1
        while parent and parent.value < curnode.value:
            self.swap(parent, curnode)
            parent = self.parent(parent)

    def parent(self, obj):
        node_index = obj.heap_index
        if node_index == 0:
            #Head Node has no parent
            return None
        else:
            return self.array[(node_index-1)/2]

    def children(self, obj):
        node_index = obj.heap_index
        child_index_list = [node_index * 2 + 1, node_index * 2 + 2]
        children_list = []
        for child_index in child_index_list:
            if child_index < self.heap_size:
                children_list.append(self.array[child_index])
        return children_list

    def max_heapify(self, obj):
        parent = self.parent(obj)
        curnode = obj
        while parent and parent.value < curnode.value:
            next_parent = self.parent(parent)
            self.swap(parent, curnode)
            parent = next_parent

    def max_heapify_root(self, obj):
        cur_children = self.children(obj)
        if cur_children:
            cur_index_value = obj.value
            child_values = [ele.value for ele in cur_children]
            if len(child_values) == 1:
                #Only Left child exists
                if cur_index_value > child_values[0]:
                    #Dont swap
                    return
                else:
                    #Swap and change indexes
                    self.swap(obj, cur_children[0])
            else:
                if cur_index_value > child_values[0] and cur_index_value > child_values[1]:
                    #Dont Swap
                    return
                else:
                    if child_values[0] > child_values[1]:
                        #Swap CURNODE with LEFT CHILD NODE and recurse
                        self.swap(obj, cur_children[0])
                    else:
                        #Swap CURNODE with RIGHT CHILD NODE and recurse
                        self.swap(obj, cur_children[1])
                    self.max_heapify_root(obj)

    def swap(self, parent_node, child_node):
        cur_index = parent_node.heap_index
        child_index = child_node.heap_index
        parent_node.heap_index = child_index
        child_node.heap_index = cur_index
        self.array[cur_index] = child_node
        self.array[child_index] = parent_node

    def extract_max(self):
        if self.heap_size > 0:
            node = self.array[0]
            self.swap(node, self.array[self.heap_size-1])
            last_node = self.array.pop()
            self.heap_size -= 1
            if self.heap_size > 0:
                self.max_heapify_root(self.array[0])
            return last_node
        else:
            raise ValueError

    def print_heap(self):
        height = 1
        print
        for i in range(self.heap_size):
            if i == pow(2,height) - 1:
                height += 1
                print
            print (self.array[i].key, self.array[i].value),
        print

class MyDataStructure(object):
    def __init__(self):
        self.__count_node_dict = {}
        self.__heap = MaxHeap()

    def insert(self, key):
        if key in self.__count_node_dict:
            # Already the key exists in Dict
            node = self.__count_node_dict[key]
            node.value += 1
            self.__heap.max_heapify(node)
        else:
            # New Node
            newnode = HeapNode(key, 1, self.__heap.heapsize())
            self.__count_node_dict[key] = newnode
            self.__heap.insert(newnode)

    def get_max_n_elements(self, n):
        n_elements_list = []
        for i in range(n):
            max_val = self.__heap.extract_max()
            n_elements_list.append(max_val)
            #self.print_ds()
        for element in n_elements_list:
            element.heap_index = self.__heap.heapsize()
            self.__heap.insert(element)
            #self.print_ds()
        return [(node.key, node.value) for node in n_elements_list]

    def print_ds(self):
        self.__heap.print_heap()

if __name__ == '__main__':
    ds = MyDataStructure()
    ds.insert("key1")
    ds.print_ds()
    ds.insert("key2")
    ds.print_ds()
    ds.insert("key3")
    ds.print_ds()
    ds.insert("key4")
    ds.print_ds()
    ds.insert("key4")
    ds.print_ds()
    #import pdb;pdb.set_trace()
    ds.insert("key3")
    ds.print_ds()
    ds.insert("key3")
    ds.print_ds()
    ds.insert("key3")
    ds.print_ds()
    ds.insert("key3")
    ds.print_ds()
    ds.get_max_n_elements(2)
    ds.print_ds()

#    heapobj = MaxHeap()
#    ele1 = HeapNode("key1", 1, 0)
#    ele2 = HeapNode("key2", 1, 1)
#    ele3 = HeapNode("key3", 1, 2)
#    ele4 = HeapNode("key4", 1, 3)

#    heapobj.insert(ele1)
#    heapobj.insert(ele2)
#    heapobj.insert(ele3)
#    heapobj.insert(ele4)

#    heapobj.print_heap()

#    ele4.value = 2
#    heapobj.max_heapify(ele4)
#    heapobj.print_heap()

#    ele3.value = 5
#    heapobj.max_heapify(ele3)
#    heapobj.print_heap()

#    max = heapobj.extract_max()
#    print "Maximum 1 is (%s, %d)" %(max.key, max.value)
#    heapobj.print_heap()

#    max = heapobj.extract_max()
#    print "Maximum 2 is (%s, %d)" % (max.key, max.value)
#    heapobj.print_heap()

