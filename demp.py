if __name__ == '__main__':
	lru_cache = LRU(max_size = 2) #initializing cache with size 2
	lru_cache['hello'] = 'world' #assigning the value 'world' to the key 'hello'
	lru_cache['world'] = 'hello' #assigning the value 'hello' to the key 'world'
	lru_cache['hello'] = 'world' #assigning the value 'world' to the key 'hello'
	print "The value of the first item now is: " + lru_cache.top() #retrtieving the value of the first item
	print "The value of the key 'world' now is: " + lru_cache['world'] #retrtieving the value of the key 'world'
	print "The value of the first item now after retrieving the key 'world' is: " +lru_cache.top() #retrtieving the value of the first item