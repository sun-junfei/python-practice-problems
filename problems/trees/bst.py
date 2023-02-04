class Empty:

    def __init__(self):
        # nothing to do!
        pass

    def is_empty(self):
        return True

    def is_leaf(self):
        return False

    def num_nodes(self):
        return 0

    def height(self):
        return 0

    def contains(self, n):
        return False

    def insert(self, n):
        return Node(n, Empty(), Empty())

    def balance_factor(self):
        return None

    def add_to_all(self, num):
        return Empty()


class Node:

    def __init__(self, n, left, right):
        self.value = n
        self.left = left
        self.right = right

    def is_empty(self):
        return False

    def is_leaf(self):
        return self.left.is_empty() and self.right.is_empty()

    def num_nodes(self):
        return 1 + self.left.num_nodes() + self.right.num_nodes()

    def height(self):
        return 1 + max(self.left.height(), self.right.height())

    def contains(self, n):
        if n < self.value:
            return self.left.contains(n)
        elif n > self.value:
            return self.right.contains(n)
        else:
            return True

    def insert(self, n):
        if n < self.value:
            return Node(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            return Node(self.value, self.left, self.right.insert(n))
        else:
            return self

    def inorder(self):
        out_list = []

        def dfs(node):
            if node.is_empty():
                return

            dfs(node.left)
            out_list.append(node.value)
            dfs(node.right)
            return

        dfs(self)
        return out_list

    def min_item(self):
        if not self.value:
            return None

        def helper(node):
            if node.left.is_empty():
                return node.value
            return helper(node.left)

        return helper(self)

    def max_item(self):
        if not self.value:
            return None

        def helper(node):
            if node.right.is_empty():
                return node.value
            return helper(node.right)

        return helper(self)

    def balance_factor(self):
        return self.right.height() - self.left.height()

    def balanced_everywhere(self):
        def helper(node):
            if not node.balance_factor():
                return True
            if node.balance_factor() not in [-1, 0, 1]:
                return False
            return helper(node.left) and helper(node.right)
        return helper(self)

    def add_to_all(self, num):
        left_child = self.left.add_to_all(num)
        right_child = self.right.add_to_all(num)
        return Node(self.value + num, left_child, right_child)

    def path_to(self, target):
        path = []

        def helper(node, target):
            if node.is_empty():
                return
            path.append(node.value)
            if node.value == target:
                return
            helper(node.left, target)
            helper(node.right, target)
            if path[-1] != target:
                path.pop()
            return
        helper(self, target)
        if path:
            return path
        return None


if __name__ == "__main__":
    bst = Empty().insert(42).insert(10).insert(
        15).insert(63).insert(9).insert(67).insert(100)

    target = 67

    print(f"The number of nodes is {bst.num_nodes()}")
    print(f"The height is {bst.height()}")
    print(f"The order is {bst.inorder()}")
    print(f"The min_item is {bst.min_item()}")
    print(f"The max_item is {bst.max_item()}")
    print(f"The balance factor is {bst.balance_factor()}")
    print(f"The tree is balanced everywhere? {bst.balanced_everywhere()}")
    print(
        f"The tree with num added to each ele has ele: {bst.add_to_all(2).inorder()}")
    print(f"The path from root to {target} {bst.path_to(target)}")
