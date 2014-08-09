lru_py
======

A simple implementation for the least recently used caching algorithm


Hello, world
------------

A simple use for LRU 

	from lru_py import LRU

	lru_cache = LRU(max_size = 2)
	lru_cache['hello'] = 'world'
	lru_cache['world'] = 'hello'
	lru_cache['hello'] = 'world'
	print "The first item now is: " + lru_cache.top()
	print "The value of the key 'world' now is: " + lru_cache['world']
	print "The first item now after retrieving the key 'world' is: " +lru_cache.top()


How To:
------------

Initializing an object:

	lru_cache = LRU(max_size = 2)

Setting a value, regular assigningment with the square bracket operator [ ]:

	lru_cache['hello'] = 'world'

Retrieving a value, using square bracket operator [ ]:

	lru_cache['hello']

Deletin, using the del and using square bracket operators:

	del lru_cache['hello']

Retrieving the most recently used item:

	lru_cache.top()

Installation
------------

**Automatic installation**::

	pip install lru_py

**Manual installation**: Download the latest source from `GitHub <https://github.com/hendawy/lru_py/releases>`_.

	tar xvzf lru_py-[VERSION].tar.gz
	cd lru_py-[VERSION]
	python setup.py build
	sudo python setup.py install