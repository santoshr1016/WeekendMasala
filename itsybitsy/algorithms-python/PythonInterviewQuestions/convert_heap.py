

class HeapConverter(object):

	def __init__(self, heap):
		#represent the heap with a one-dimensional array
		self.heap = heap;
	
	def transform(self):
	
		#we do not have to consider leaf nodes (thats why the last node we have to consider has index (length-2)/2
		index = (len(self.heap)-2)//2
		
		#conider the internal node in a reverse order
		while index>=0:
			#we "heapify" all the internal nodes: we check whether the parent is smaller than the children
			#if not: than we swap the nodes accordingly
			self.heapify(index)
			index=index-1
			
		return heap
		
	#argument is the index of an internal node in the heap
	def heapify(self, index):
	
		#index of the left child
		left_child_index = 2*index+1
		#index of the right child
		right_child_index = 2*index+2
		
		#index of the smallest child node
		smallest = index
		
		#check the left child whether it is smaller than the parent
		if left_child_index<len(self.heap) and self.heap[left_child_index]<self.heap[index]:
			smallest = left_child_index
			
		#compare the right child and the left child
		if right_child_index<len(self.heap) and self.heap[right_child_index]<self.heap[smallest]:
			smallest = right_child_index
	
		#we do not want to swap the node with itself only when necessary
		if smallest!= index:
			self.heap[index],self.heap[smallest]=self.heap[smallest],self.heap[index]
			#call the method recursively on the smaller child
			self.heapify(smallest)
	
if __name__ == "__main__":		
	
	heap = [210,100,23,2,5]
	
	converter = HeapConverter(heap)
	
	print(converter.transform())