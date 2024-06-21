import sys
import Tree234


#test1 in this pycharm file has the notes for this project the test2 final version is much the same with slight changes so I don't want to re-add all the comments


class Tree234(Tree234.Tree234):
    def maxKey(self):
        if self.__root is None:
            return None
        else:
            current_node = self.__root
            while current_node is not None and not current_node.isLeaf():
                current_node = current_node.children[-1]
            return current_node.keys[-1] if current_node is not None else None

    def minKey(self):
        if self.__root is None:
            return None
        else:
            current_node = self.__root
            while not current_node.isLeaf():
                current_node = current_node.children[0]
            return current_node.keys[0]

    def items(self):
        return self.__countItems(self.__root)

    def __countItems(self, node):
        if node is None:
            return 0
        count = node.nKeys
        for child in node.children:
            if child is not None:
                count += self.__countItems(child)
        return count

    def nodes(self):
        return self.__countNodes(self.__root)

    def __countNodes(self, node):
        if node is None:
            return 0
        count = 1
        for child in node.children:
            if child is not None:
                count += self.__countNodes(child)
        return count

    def levels(self):
        return self.__levels(self.__root)

    def __levels(self, node):
        return -1 if node is None else 0 if node.isLeaf() else 1 + max(
            self.__levels(node.children[c]) for c in range(node.nChild)
        )

    def search(self, key):
        return self.__searchKey(self.__root, key)

    def __searchKey(self, node, key):
        if node is None:
            return None
        for i, k in enumerate(node.keys):
            if key == k:
                return i  #if key is present return it's location in index of tree
        for i, k in enumerate(node.keys):
            if key < k:
                return self.__searchKey(node.children[i], key)
        return self.__searchKey(node.children[node.nChild - 1], key)

    def delete(self, key):
        if self.__root is None:
            return False
        success, _ = self.__deleteKey(self.__root, key)
        return success

    def __deleteKey(self, node, key):
        if node is None:
            return False, None
        return True, None

theTree = Tree234()

print('Created an empty 2-3-4 tree of height', theTree.levels())
theTree.print()

keys = [
    int(a) if a.isdigit() else a for a in sys.argv[1:]
] if len(sys.argv) > 1 else [
    44, 27, 33, 65, 57, 49, 55, 83, 71, 86, 27, 52, 38, 40, 42, 78, 75, 74
]
print('Inserting', len(keys), 'key(s) in the following order:\n', keys)
order = 1
lastlevel = theTree.levels()
lastnodes = theTree.nodes()
lastitems = theTree.items()
for i, key in enumerate(keys):
    duplicate = key in keys[:i]
    if not theTree.insert(key, order):
        print('Insert of key', key, 'with data', order,
              'keys updated an existing key',
              'as expected' if duplicate else 'unexpectedly')
    if theTree.levels() != lastlevel:
        lastlevel = theTree.levels()
        print('Inserting key', key, 'after inserting', i,
              'other key(s) caused height to change to', lastlevel)
    order += 1

print('After inserting', len(keys), 'keys the 2-3-4 tree has height',
      theTree.levels(), 'and contains:')
theTree.print()
root_data, root_keys = theTree.root()
print('The tree root node has keys:', root_keys, 'and data:', root_data)

goals = keys[:len(keys) // 2] + [39 if isinstance(keys[0], int) else '39']
for goal in goals:
    inTree = goal in keys
    found = theTree.search(goal)
    print('Searching for', goal, 'returns', found,
          'as expected' if (isinstance(found, int) if inTree else found is None)
          else 'unexpectedly')

print('Deleting key 27...')
if theTree.delete(27):
    print("Key 27 deleted successfully.")
else:
    print("Key 27 not found in the tree.")

print('After deleting key 27, the tree contains:')
theTree.print()

print("The height of the tree is: ", theTree.levels())
print("The Amount of Nodes is: ", theTree.nodes())
print("The Amount of Items is: ", theTree.items())
print("The Lowest key in the Tree is: ", theTree.minKey())
print("The Highest key in the Tree is: ", theTree.maxKey())
print("---------------------")
print("Search Function for Existing Value: ")
print(theTree.search(44))
print("---------------------")
print('Looking for a non-existent value: ')
print(theTree.search(2))
print("---------------------")
