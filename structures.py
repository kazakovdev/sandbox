class LinkedList:
    head = None

    class Node:
        element = None
        next_element = None

        def __init__(self, element, next_element=None):
            self.element = element
            self.next_element = next_element

    def append(self, element):
        if not self.head: #если первое добавление в список
            self.head = self.Node(element)
            return element
        node = self.head
        while node.next_element:
            node = node.next_element
        node.next_element = self.Node(element)

    def out(self):
        node = self.head
        while node.next_element:
            print(node.element)
            node = node.next_element
        print(node.element)

class OrintedGraph():
    class Node():


        def __init__(self, dict_of_node_attr = {}, node_num = 0, edges = {}):
            self.num = node_num
            self.attributes = {}
            self.edges = {}

            for (k, v) in dict_of_node_attr.items():
                self.attributes.update({k: v})
            for (k, v) in edges.items():
                self.edges.update({k: v})


    def __init__(self, list_of_edges = [], dict_of_nodes_attr = {}):
        self.nodes = {}
        self.edges = {}
        for edge in list_of_edges:
            if edge[0] in self.nodes:
                pass
            if edge[1] in self.nodes:
                pass

            self.attributes.update({k: v})


        for (k, v) in edges.items():
            self.edges.update({k: v})
    pass


G = OrintedGraph(list_of_edges = [[1,2, 0.5],
                                  [1,3, 6],
                                  [3, 2, 0.01]],
                 dict_of_nodes_attr={1: {'func': 'f1'},
                                     2: {'func': 'f1'},
                                     3: {'func': 'f2'}})