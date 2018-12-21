class BinaryTree:
    """
    Implementation of the Binary Tree
    """
    def __init__(self, root_object):
        self.key = root_object
        self.left_child = None
        self.right_child = None


    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            tmp_ = BinaryTree(new_node)
            tmp_.left_child = self.left_child
            self.left_child = tmp_

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            tmp_ = BinaryTree(new_node)
            tmp_.right_child = self.right_child
            self.right_child = tmp_

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_val(self, new_val):
        self.key = new_val

    def get_root_val(self):
        return self.key

class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]

    def curr_size():
        return len(self.heap_list)

    def insert(self, val):
        if len(self.heap_list) == 1:
            self.heap_list.append(val)
            return

        self.heap_list.append(val)
        child_index = len(self.heap_list) - 1
        parent_index = child_index // 2
        while parent_index > 0 and self.heap_list[child_index] < self.heap_list[parent_index]:
            self.heap_list[child_index], self.heap_list[parent_index] = (self.heap_list[parent_index],
                                                                         self.heap_list[child_index])
            child_index = parent_index
            parent_index = child_index // 2


