'''Implement a basic binary tree and include methods for in-order, pre-order, and post-order traversal.
Instructions:
Implement a class Node that represents a node in the binary tree.
Implement a class BinaryTree that supports inserting nodes and three types of traversal methods: in-order, pre-order, and post-order.
Write test cases to verify the implementation.'''


class Node:
    """A node in a binary search tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """A simple Binary Search Tree with traversal utilities."""

    def __init__(self):
        self.root = None

    # -----------------
    # Insertion Methods
    # -----------------
    def insert(self, value):
        """Insert a new value into the tree (BST property: left < node <= right)."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:  # duplicates or greater values go to the right
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    # -----------------
    # Traversal Methods
    # -----------------
    def inorder(self):
        """Return a list of values visited in in-order (LNR)."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def preorder(self):
        """Return a list of values visited in pre-order (NLR)."""
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        """Return a list of values visited in post-order (LRN)."""
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)

    # -----------------
    # Left & Right Nodes Helpers
    # -----------------
    def left_nodes(self):
        """Return a list of all nodes that are left children in the tree."""
        nodes = []
        self._gather_left_nodes(self.root, nodes)
        return nodes

    def _gather_left_nodes(self, node, nodes):
        if node and node.left:
            nodes.append(node.left.value)  # left child of current node
            self._gather_left_nodes(node.left, nodes)
        if node and node.right:
            # need to traverse right subtree too to catch its left children
            self._gather_left_nodes(node.right, nodes)

    def right_nodes(self):
        """Return a list of all nodes that are right children in the tree."""
        nodes = []
        self._gather_right_nodes(self.root, nodes)
        return nodes

    def _gather_right_nodes(self, node, nodes):
        if node and node.right:
            nodes.append(node.right.value)  # right child of current node
            self._gather_right_nodes(node.right, nodes)
        if node and node.left:
            # need to traverse left subtree too to catch its right children
            self._gather_right_nodes(node.left, nodes)


def test():

    bst = BinaryTree()

    list_values = [50,30,70,80,40,60,20]

    for i in list_values:
        bst.insert(i)

    print("Root node value:", bst.root.value)
    print("\nLeft nodes:", bst.left_nodes())
    print("Right nodes:", bst.right_nodes())
    print("Preorder: ", bst.preorder())
    print("Postorder: ", bst.postorder())
    print("Inorder: ", bst.inorder())

    print ("All Test Passed")

test()

