import sys
import Tree234
class Tree234(Tree234.Tree234):
  def maxKey(self):
      if self.__root is None:
          return None
      else:
          current_node = self.__root
          while not current_node.isLeaf():
              current_node = current_node.children[2]
          return current_node.keys[2]
  def minKey(self): #function for finding the min key value in the tree
      if self.__root is None: # if there isn't a root then void
          return None # void
      else:
          current_node = self.__root # not needed but makes this much easier to read and way less annoying to type fr
          while not current_node.isLeaf(): #this ensures that it gets to the bottom leaf node bc while loop will keep going till current node isleaf is true.
              current_node = current_node.children[0] # goes towards the leftmost node as I entered 0 in the children 0 = lowest node in this instance
          return current_node.keys[0] # returns the key in the node that is lowest (0) . this one is really upsetting like the ones before as the tree isn't being generated correctly but my logic is working as the lowest value would be located bottom left of tree in leaf node

  def items(self):
      return self.__countItems(self.__root)
  def __countItems(self, node):
      if node is None:
          return 0
      count = node.nKeys
      for child in node.children:
          if child is not None: #ensures that there is an item and runs this if there is
              count += self.__countItems(child)
      return count
  def nodes(self): #def to run when wanting to get total nodes in 234 tree
      return self.__countNodes(self.__root) #returns the node counting fucnction below which determines how many nodes are in the tree

  def __countNodes(self, node): #def for counting the nodes
      if node is None:  #this checks and ensures that there are nodes in the tree prior to attempting to count them without this there'd be errors in a 0 node tree.
          return 0
      count = 1  #without starting the count at one you miss the top node in which you don't count as you traverse down the tree and then start counting on the way back up with each node you pass
      for child in node.children:  #this is the counting algorithm for the def of countnodes
          if child is not None:  #as we have the none alg above we now need the situation in which a child is not null
              count += self.__countNodes(child) #count appends and counts each node inserted
      return count
  def levels(self):           #levels func 1
    return self.__levels(self.__root) # same as above
  def __levels(self, node): #this is all the same algorithm just different letters words and spacing/system in a way//recursive func separated to make code easier/organized
    return -1 if node is None else 0 if node.isLeaf() else 1 + max( # -1 is delagated as a no levels 0 is one leaf and then a recursive function is used if there are levels appending the values for each level
       self.__levels(node.children[c]) for c in range(node.nChild))


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




print('Reinserting the same', len(keys), 'keys into the tree...')
for i, key in enumerate(keys):
 if theTree.insert(key, order):
    print('Reinserting key', key, 'with data', order,
          'unexpectedly added a new key to the tree')
 if theTree.levels() != lastlevel:
    lastlevel = theTree.levels() # updates the variable if the stored values aren't aligned
    print('Reinserting key', key, 'with value', order, 'after inserting', i,
          'other key(s) caused height to change to', lastlevel) # Like below this displays the above calc
 order += 1
lastnodes = theTree.nodes() #updates the nodes after insertion
lastitems = theTree.items() #updates the items after insertion








print('Leaves tree with height', theTree.levels(), 'and containing:')
theTree.print()
root_data, root_keys = theTree.root()
print('The tree root node has keys:', root_keys, 'and data:', root_data)




for order in ['pre', 'in', 'post']:
 print('Traversing the tree using', order, 'order')
 for key, data in theTree.traverse(order):
    print('{' + str(key) + ', ' + str(data) + '}', end=' ')  # none of the printing of the tree is really needed but I'm leaving it in in case you wanted to view it with the code and outputs
 print()




print("The height of the tree is: ", lastlevel) #prints the final and updated level count/height of the tree
print("The Amount of Nodes is: ", lastnodes) #prints the final and updated node count
print("The Amount of Items is: ", lastitems)#prints the final and updated Item count
print("The Lowest key in the Tree is: ", theTree.minKey())
print("The Highest key in the Tree is: ", theTree.maxKey())
