import json

class ToDoMixin(object):
	def to_dict(self):
		return self._traverse_dict(self.__dict__)

	def _traverse_dict(self, instance_dict):
		output = {}
		for key,  value in instance_dict.items():
			output[key] = self._traverse(key, value)
		return output
	def _traverse(self, key, value):
		if isinstance(value, ToDoMixin):
			return value.to_dict()
		elif isinstance(value, dict):
			return self._traverse_dict(value)
		elif isinstance(value, list):
			return [self._traverse_dict(value.__dict__)]
		else:
			return value
# Here, I define  an example class that uses the mixin to make a dictionary 
# representation of a binary tree

class BinaryTree(ToDoMixin):
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right
# translating a large number of related python objects into  a dictionary 
#becomes easy 
tree = BinaryTree(10, left = BinaryTree(7, right = BinaryTree(9)),
						right = BinaryTree(13, left = BinaryTree(11)))

# print( json.dumps(tree.to_dict(), indent = 4))

class BinaryTreeWithParent(BinaryTree):
	def __init__(self, value, left = None, right = None, parent = None):
		super().__init__(value, left=None, right = None)
		self.parent = parent

#the solution is to override the ToDoMixin._traverse() method in the 
#BinaryTreeWithParent class to only process values that matter, preventing 
#cycles encountered by the mix-in.Here I override the _traverse() method to not 
#traverse the parent and just insert its numerical value
	def _traverse(self, key, value):
		if(isinstance(value, BinaryTreeWithParent) and key == 'parent'):
			return value.value # prevent cycles 
		else :
			return super()._traverse(key, value)
# calling BinaryTreeWithParent.to_dict will work without issue because the
#circular referencing properties are not followed.
root = BinaryTreeWithParent(10,left = 12)
root.left = BinaryTreeWithParent(7, parent = root)
root.left.right = BinaryTreeWithParent(9, parent  = root.left)
print(root.value)
print(json.dumps(root.to_dict(), indent = 4))

class NamedSubTree(ToDoMixin):
	def __init__(self, name, tree_with_parent):
		self.name = name
		self.tree_with_parent = tree_with_parent
my_tree = NamedSubTree('foobar', root.left.right)
print(my_tree.to_dict())


class JsonMix(object):
	@classmethod
	def from_json(cls , data):
		kwargs = json.load(data)
		return cls(**kwargs)
	def to_json(self):
		return json.dumps(self.to_dict())