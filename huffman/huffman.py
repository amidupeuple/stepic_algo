class TreeNode:
    def __init__(self, label, freq=-1):
        self.label = label
        self.freq = freq
        self.left = self.right = self.parent = None

    def __str__(self):
        return "label: {}, freq: {}".format(self.label, self.freq)


storage = []


def print_tree(root):
    if root.left is None and root.right is None:
        print(root)
        return
    print_tree(root.left)
    print_tree(root.right)


def pq_insert(x):
    storage.append(x)


def pq_pop_low_priority():
    sorted_storage = sorted(storage, key=lambda x: (x.freq, x.label))
    min_element = sorted_storage[0]
    storage.remove(min_element)
    return min_element


def pq_contains(c):
    list_of_keys = [x.label for x in storage]
    return c in list_of_keys


def build_tree(s):
    for c in s:
        if not (pq_contains(c)):
            counter = 0
            for x in s:
                if x == c:
                    counter += 1
            pq_insert(TreeNode(c, counter))

    if len(storage) == 1:
        return storage

    while len(storage) > 1:
        min1 = pq_pop_low_priority()
        min2 = pq_pop_low_priority()
        new = TreeNode(min1.label + min2.label, min1.freq + min2.freq)
        new.left = min2
        new.right = min1
        min2.parent = new
        min1.parent = new
        pq_insert(new)
    return storage


codes = {}


def create_dict(root, prefix):
    if root.left is None and root.right is None:
        if prefix == "":
            prefix = "1"
        codes[root.label] = prefix
        return
    create_dict(root.left, prefix + "1")
    create_dict(root.right, prefix + "0")


def encode(s, codes_dict):
    encoded = ""
    for c in s:
        encoded += str(codes_dict[c])
    return encoded


def prepare_code_dict():
    n_dict, n_str = map(int, input().split())
    code_dict = {}
    for i in range(n_dict):
        key, val = input().split()
        key = key[0]
        code_dict[key] = val
    return code_dict


def add_leaf_to_tree(parent, code, label):
    if len(code) == 1:
        leaf_node = TreeNode(label)
        leaf_node.parent = parent
        if code == "0":
            parent.left = leaf_node
        else:
            parent.right = leaf_node
        return
    if code[0] == "0":
        if parent.left is None:
            new_left = TreeNode("-")
            new_left.parent = parent
            parent.left = new_left
        new_code = code[1:]
        add_leaf_to_tree(parent.left, new_code, label)
    else:
        if parent.right is None:
            new_right = TreeNode("-")
            new_right.parent = parent
            parent.right = new_right
        new_code = code[1:]
        add_leaf_to_tree(parent.right, new_code, label)


def build_tree_by_dict(code_dict):
    root = TreeNode("-")
    for k, v in code_dict.items():
        add_leaf_to_tree(root, v, k)
    return root


def decode(encoded_str, root):
    decoded_str = ""
    while encoded_str:
        c, new_str = decode_character(encoded_str, root)
        decoded_str += c
        encoded_str = new_str
    return decoded_str


def decode_character(encoded_str, cur_node):
    if cur_node.left is None and cur_node.right is None:
        return cur_node.label, encoded_str
    else:
        if encoded_str[0] == "0":
            return decode_character(encoded_str[1:], cur_node.left)
        else:
            return decode_character(encoded_str[1:], cur_node.right)


def main():
    '''#encoding
    s = input()
    build_tree(s)
    create_dict(storage[0], "")
    encoded = encode(s, codes)
    print(len(codes), len(encoded))
    for k, v in codes.items():
        print("{}: {}".format(k, v))
    print(encoded)'''

    #decoding
    code_dict = prepare_code_dict()
    encoded_str = input()
    root = build_tree_by_dict(code_dict)
    print(decode(encoded_str, root))
    print('ok')


if __name__ == "__main__":
    main()
