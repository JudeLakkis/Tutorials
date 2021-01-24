<h1 align="center">Binary Search Trees</h1>

A **Binary Search Tree (BST)** is a tree data structure in which each node has links to at most two children. These children are referred to as the *left child* and *right child*.

Binary search trees differ from binary trees in that the entries are ordered.

So the entire tree is built out of nodes, so it is important to understand how these would be built

### Building a Node

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
```

Ok so now we have built a basic node structure that we can use in our tree, so we need to build our tree now.

### Building the Tree

```python
class BST:
	def __init__(self):
		self.root = None
```

## Inserting Nodes

Inserting nodes in a binary search tree is actually rather simple. Starting with a root node at the top and center is what every other operation is based on. If the inserted nodes value is less than the root it is pushed to the left. If it is greater than the root value it is pushed to the right. It continues this pattern until it finds itself a free space in the tree. In very simple and straight forward rules:

### Insertion Rules

1. If the **Current Value** < **Root Value**
    1. Traverse Left
2. If the **Current Value** > **Root Value**
    1. Traverse Right
3. If there's a gap fill it. Else repeat the process

In plain english that is simple enough, but actually coding this out can be rather challenging if you don't have a reasonably good grasp on recursion (trust me I know…). So let's work through this step by step. 

## Coding Inserts

### Does the tree exist?

To begin with we need to check if the tree actually exists. If it doesn't we need to create a root node, and if it does then we have to start working through our rules

```python
def insert(self, data):
	if self.root is None:
		self.root = Node(data)
	else:
		self._insert(data, self.root) # Our Inserting Code
```

This member function of our tree class checks if the root is equal to None. If it is, it creates a Node with our data.

### Adding to the left

Ok now that we know if the root node exists or not, we need to add our first rule.

```python
def _insert(self, data, current_node):
	# Is data less than current value?
	if data < current_node.data:
		# Is there a left child node?
		if current_node.left is None:
			current_node.left = Node(data)
		else:
			# Recursively inserting the node again to the left
			self._insert(data, current_node.left)
```

Just as we lay out in our rules, we need to check if the value is less than our current value. If that is the case, we first check if there is a connected left child node. If there isn't one, we create a new node with our data and link it to our current node. If there is one, we call the function again and repeat the steps we just set up.

Good, the left side is done. Now give the right side a try before looking at the next bit if you're feeling confident.

### Adding to the right

It's pretty much the same as the code for the left, but this time we check the right side.

```python
# Is data greater than current value?
if data > current_node.data:
	# Is there a right child node?
	if current_node.right is None:
		current_node.right = Node(data)
	else:
		# Recursively inserting the node again to the right
		self._insert(data, current_node.right)
```

See? It's almost exactly the same. 

Ok now we just need to make sure there are no repeat values in our tree.

```python
if data == current_node.data:
	print("Value is already in the tree")
```

And that's it, we've written out the code needed to insert a value into our tree in the right position.

### Final Insert Code

```python
def insert(self, data):
	if self.root is None:
		self.root = Node(data)

	else:
		self._insert(data, self.root)

def _insert(self, data, current_node):
	if data < current_node.data:
		if current_node.left is None:
			current_node.left = Node(data)
		else:
			self._insert(data, current_node.left)

	elif data > current_node.data:
		if current_node.right is None:
			current_node.right = Node(data)
		else:
			self._insert(data, current_node.right)

	else:
		print("Value is already in the tree")
```

## Searching Trees

Searching is actually pretty similar to inserting values into a tree, with the only difference being that we aren't adding anything this time. If you think you understand how this would work feel free to try it on your own first before look at the example code.

### Does the tree exist?

Alright so once again we need to make sure the tree actually exists to be able to search for it.

```python
def find(self, data):
	if self.root:
		is_found = self._find(data, self.root)
		if is_found:
			return True
		return False
	else:
		return None
```

So we begin by checking if the our root node actually exists, and if it doesn't we just return `None`. We then define the variable `is_found` and assign it to our finding function, taking the chance to set up a conditional that returns `True` if the value is found and `False` if it isn't in our tree.

Time to check our nodes.

### Checking Left and Right

```python
def _find(self, data, current_node):
	if data < current_node.data:
		# Recursively check the left node
		return self._find(data, current_node.left)

	elif data > current_node.data:
		# Recursively check the right node
		return self._find(data, current_node.right)

	if data == current_node.data:
		return True
```

Nice and simple. We check if the value we are looking for is less than our current nodes value. If it is then we recall the function again and search again at the left node. Same process for the right side, and if our data matches the current nodes data then we return `True`.

### Final Search Code

```python
def find(self, data):
	if self.root:
		is_found = self._find(data, self.root)
		if is_found:
			return True
		return False

	else:
		return None

def _find(self, data, current_node):
	if data < current_node.data:
		return self._find(data, current_node.left)

	elif data > current_node.data:
		return self._find(data, current_node.right)

	if data == current_node.data:
		return True
```

## But why go to all this effort?

You might be thinking, why go to all this effort to essentially store a list of numbers? Couldn't we just put these all in a regular array or linked list?

Yes you could do that, but the reason we go to this effort is the massive speed difference we get when it comes to searching for items in our "list". When searching through a typical array, with the most basic of methods you have to start at the beginning of the array and work your way through every item until you find it.

The advantage we have here is that we can cut out half of search space per operation saving us massive amounts of time. Say in a list of values 0 - 100 we are checking to see if 67 is in the data set.

Our root value is 50, we know that 67 is greater than 50 so we can cut out the first 50 values we need to look through. Do this process a couple times and we can very quickly tell if 67 is in our data set.

## Final Thoughts

Binary search trees are a very helpful tool to use in a lot of circumstances and can really help you optimize your code as you progress. If you have any questions let me know, and I'll try and clear it up some more.
