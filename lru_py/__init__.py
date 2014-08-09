#This is a simple implementation for the least recently used caching algorithm.

# Copyright (C) 2014 Mohamed Hendawy

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class DNode(object):
	"""
	The class for the Doubly Node
	"""

	def __init__(self, data = None, previous = None, next = None):
		self._data = data
		self._previous = previous
		self._next = next

	@property
	def data(self):
		return self._data

	@property
	def previous(self):
		return self._previous

	@property
	def next(self):
		return self._next

	@data.setter
	def data(self, data):
		self._data = data

	@previous.setter
	def previous(self, previous):
		self._previous = previous

	@next.setter
	def next(self, next):
		self._next = next

class DLinkedList(object):
	"""
	The class for the Doubly Linked List
	"""

	def __init__(self, head = None, tail = None):
		self._head = head
		self._tail = tail

	@property
	def head(self):
		return self._head

	@head.setter
	def head(self, head):
		self._head = head

	@property
	def tail(self):
		return self._tail

	@tail.setter
	def tail(self, tail):
		self._tail = tail


class LRU(object):
	"""
	The class for the LRU Cache
	"""

	def __init__(self, max_size=1024):
		"""
		Initializing a new LRU Cache. Creating new empty dictionary, 
		new empty doubly linked list,
		and sets the maximum size of the cache.
		"""
		if max_size > 0:
			self._max_size = max_size
			self._dict = {}
			#data will be a dictionary { 'key': key, 'value': value }
			self._list = DLinkedList()
		else:
			raise ValueError("max_size must be greater than zero")

	def __len__(self):
		"""
		Returns the length of the cache
		"""
		return len(self._dict)

	def __contains__(self, key):
		"""
		When calling "key in cache", return true if the key exists, 
		and false if it doesn't exist
		"""
		return key in self._dict

	def __setitem__(self, key, value):
		"""
		__setitem__ uses the operator [] to add an item to the cache, 
		or set an existing item to another value.
		If the key doesn't exist, it is added with its value, 
		to the top of the cache.
		If the key does exist, its value gets overwritten with the new value, 
		and moved to the top of the cache.
		If a new key is inserted, and the cache is full (current length of the 
		dictionary equals to _max_size), a new item is inserted to the top, 
		and least recently used item is removed from the cache.
		"""
		if key in self._dict:
			self._dict[key].data['value'] = value 
			self._move_to_top(key)
		elif self._max_size > 0:
			node  = DNode( data = { 'key': key, 'value': value } )
			if self._list.head is None:
				self._list.head = node
				self._list.tail = node
				self._dict[key] = node
			else:
				if len(self._dict) >= self._max_size:
					tail_key = self._list.tail.data['key']
					self._list.tail = self._list.tail.previous
					self._list.tail.next = None
					del self._dict[tail_key]
				node.next = self._list.head
				self._list.head.previous = node
				self._list.head = node
				self._dict[key] = node
		elif self._max_size < 1:
			raise ValueError("max_size must be greater than zero")

	def __getitem__(self, key):
		"""
		__getitem__ uses the operator [] to retrieve an existing item 
		from the cache.
		Raises KeyError if they key doesn't exist
		"""
		try:
			if self._dict[key] is not self._list.head:
				self._move_to_top(key)
			return self._dict[key].data['value']
		except(KeyError):
			raise KeyError("Key does not exist")

	def __delitem__(self, key):
		"""
		Uses operator del (del cache[key]) to delete an item from the cache.
		Raises KeyError if they key doesn't exist
		"""
		try:
			current_node = self._dict[key]
			
			if not current_node.previous:
				self._list.head = current_node.next
				self._list.head.previous = None

			elif current_node.next and current_node.previous:
				current_node.previous.next = current_node.next
				current_node.next.previous = current_node.previous

			elif current_node.previous:
				self._list.tail = current_node.previous
				self._list.tail.next = None

			del self._dict[key]

		except(KeyError):
			raise KeyError("Key does not exist")

	def top(self):
		"""
		Returning the value of the most recently used item
		"""
		if len(self._dict) > 0:
			return self._list.head.data['value']
		else:
			return None

	def _move_to_top(self, key):
		"""
		Moving an node to the top of the linked list 
		"""
		current_node = self._dict[key]

		if not current_node.previous:
			return

		elif current_node.next and current_node.previous:
			current_node.previous.next = current_node.next
			current_node.next.previous = current_node.previous

		elif current_node.previous:
			self._list.tail = current_node.previous

		current_node.next = self._list.head
		self._list.head.previous = current_node
		self._list.head = current_node
		self._list.head.previous = None
		self._list.tail.next = None