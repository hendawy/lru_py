#This is a simple implementation for the least recently used caching algorithm.

# Copyright (C) 2014 Mohamed Hendawy

# This file is part of lru_py.

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

from lru_py import LRU

import unittest

class LRUTestCase(unittest.TestCase):

	def _index(self, obj, index):
		return obj[index]

	def setUp(self):
		self.lru = LRU(max_size = 3)

	def tearDown(self):
		self.lru = None

	def test_adding_one_item(self):
		self.lru['itest0'] = 'itest0'
		self.assertEqual(self.lru['itest0'], 'itest0', 'incorrect item') #Assuring the item was inserted
	
	def test_adding_sequence(self):
		self.lru['itest0'] = 'itest0'
		self.assertEqual(self.lru.top(), 'itest0', 'incorrect item') #Assuring the item is in the top
		self.lru['itest1'] = 'itest1'
		self.assertEqual(self.lru.top(), 'itest1', 'incorrect item') #Assuring the item is in the top
		self.lru['itest2'] = 'itest2'
		self.assertEqual(self.lru.top(), 'itest2', 'incorrect item') #Assuring the item is in the top
		self.lru['itest3'] = 'itest3'
		self.assertEqual(self.lru.top(), 'itest3', 'incorrect item') #Assuring the item is in the top

	def test_move_to_top_after_acesss(self):
		#test case for moving item to top after accessing it, 1 item, 2 items, and more than 2 items.
		self.lru['itest0'] = 'itest0'
		self.lru['itest0']
		self.assertEqual(self.lru.top(), 'itest0', 'incorrect item') #After inserting the first item, it should be on top
		self.lru['itest1'] = 'itest1'
		self.assertEqual(self.lru.top(), 'itest1', 'incorrect item') #After adding a new item, the new item should be on top
		self.lru['itest0']
		self.assertEqual(self.lru.top(), 'itest0', 'incorrect item') #After accessing the first item, the first item should go back to the top		
		self.lru['itest2'] = 'itest2'
		self.assertEqual(self.lru.top(), 'itest2', 'incorrect item') #After adding a new item, the new item should be on top
		self.lru['itest0']
		self.assertEqual(self.lru.top(), 'itest0', 'incorrect item') #After accessing itest0, it should go from second to top.
		
	def test_change_existing_item(self):
		#test case for changing an existing item
		self.lru['itest0'] = 'itest0'
		self.assertEqual(self.lru.top(), 'itest0', 'incorrect item') #After inserting the first item, it should be on top
		self.lru['itest1'] = 'itest1'
		self.assertEqual(self.lru.top(), 'itest1', 'incorrect item') #After adding a new item, the new item should be on top
		self.lru['itest0'] = 'itest00'
		self.assertEqual(self.lru.top(), 'itest00', 'incorrect item') #After accessing the first item, the first item should go back to the top		
		self.lru['itest2'] = 'itest2'
		self.assertEqual(self.lru.top(), 'itest2', 'incorrect item') #After adding a new item, the new item should be on top
		self.lru['itest0'] = 'itest0'
		self.assertEqual(self.lru.top(), 'itest0', 'incorrect item') #After accessing itest0, it should go from second to top.
		self.lru['itest1'] = 'itest11'
		self.assertEqual(self.lru.top(), 'itest11', 'incorrect item') #After accessing itest0, it should go from second to top

	def test_getting_item(self):
		#test case for accessing an item that doesn't exist
		self.lru['itest0'] = 'itest0'
		self.assertEqual(self.lru['itest0'], 'itest0', 'incorrect item') #Getting item with key itest0.
		self.assertRaises(KeyError, lambda: self.lru['itest1'])
		# self.assertRaises(KeyError, lambda: self.lru['itest1']) #Getting item that doesn't exist.

	def test_size_out_of_bounds(self):
		#test case for maxing out in size (adding more elements than the size of the cache)
		self.lru['itest0'] = 'itest0'
		self.lru['itest1'] = 'itest1'
		self.lru['itest2'] = 'itest2'
		self.lru['itest3'] = 'itest3'
		self.assertEqual(len(self.lru), 3, 'incorrect item')  #testing size of the array after remove the least recently used item.
		self.assertEqual(self.lru['itest3'], 'itest3', 'incorrect item') #Getting item with key itest3.
		self.assertEqual(self.lru.top(), 'itest3', 'incorrect item') #Getting the most recently used item.
		self.assertRaises(KeyError, lambda: self.lru['itest0']) #Getting an item that was removed due to maxing out (The least recently used item)

	def test_delete_item_from_middle(self):
		#test case for deleting an item from the middle
		self.lru['itest0'] = 'itest0'
		self.lru['itest1'] = 'itest1'
		self.lru['itest2'] = 'itest2'
		self.assertEqual(len(self.lru), 3, 'incorrect item')  #testing size of the array before deletion.
		del self.lru['itest1']
		self.assertRaises(KeyError, lambda: self.lru['itest1']) #Getting item that was deleted.
		self.assertEqual(self.lru.top(), 'itest2', 'incorrect item')  #Getting item from the top.
		self.assertEqual(len(self.lru), 2, 'incorrect item')  #testing size of the array after deletion.

	def test_delete_item_from_top(self):
		#test case for deleting an item from the top
		self.lru['itest0'] = 'itest0'
		self.lru['itest1'] = 'itest1'
		self.lru['itest2'] = 'itest2'
		self.assertEqual(len(self.lru), 3, 'incorrect item')  #testing size of the array before deletion.
		del self.lru['itest2']
		self.assertRaises(KeyError, lambda: self.lru['itest2']) #Getting item that was deleted.
		self.assertEqual(self.lru.top(), 'itest1', 'incorrect item')  #Getting item from the top.
		self.assertEqual(len(self.lru), 2, 'incorrect item')  #testing size of the array after deletion.

	def test_delete_item_from_bottom(self):
		#test case for deleting an item from the bottom
		self.lru['itest0'] = 'itest0'
		self.lru['itest1'] = 'itest1'
		self.lru['itest2'] = 'itest2'
		self.assertEqual(len(self.lru), 3, 'incorrect item')  #testing size of the array before deletion.
		del self.lru['itest0']
		self.assertRaises(KeyError, lambda: self.lru['itest0']) #Getting item that was deleted.
		self.assertEqual(self.lru.top(), 'itest2', 'incorrect item')  #Getting item from the top.
		self.lru['itest1'] #changing the top
		self.assertEqual(self.lru.top(), 'itest1', 'incorrect item')  #Getting item from the top after the order has been changed.
		self.assertEqual(len(self.lru), 2, 'incorrect item')  #testing size of the array after deletion.

	def test_delete_nonexisting_item(self):
		#test case for deleting an item from the bottom
		self.lru['itest0'] = 'itest0'
		self.lru['itest1'] = 'itest1'
		self.assertEqual(len(self.lru), 2, 'incorrect item')  #testing size of the array before deletion.
		del self.lru['itest0']
		self.assertEqual(len(self.lru), 1, 'incorrect item')
		self.assertRaises(KeyError, lambda: self.lru['itest0']) #Getting item that was deleted.
		with self.assertRaises(KeyError):  #Deleting nonexisting item
			del self.lru['itest0']

if __name__ == '__main__':
	unittest.main()

	lru_cache = LRU(max_size = 2)
	lru_cache['hello'] = 'world'
	lru_cache['world'] = 'hello'
	lru_cache['hello'] = 'world'
	print "The value of the first item now is: " + lru_cache.top()
	print "The value of the key 'world' now is: " + lru_cache['world']
	print "The value of the first item now after retrieving the key 'world' is: " +lru_cache.top()