import heapq

mylist = [21,1,45,78,3,5]

k = 3  
largest = heapq.nlargest(k, mylist)  
smallest = heapq.nsmallest(k, mylist)  
print(f"original list is {mylist}")#print('original list is', mylist)  
print(f'largest-{k}  is {largest}')  
print('smallest-'+str(k), ' is ', smallest)  
  
# heapify  
print('original list is', mylist)  
heapq.heapify(mylist)  
print('heapify  list is', mylist)  
  
# heappush
heapq.heappush(mylist, 105)  
print('pushed heap is', mylist)

# heappop
pop =  heapq.heappop(mylist)
print(f"Pop the smallest item: {pop}")
print('popped heap is', mylist)  
  
# heappushpop 先把item加入到堆中，然后再pop
pop = heapq.heappushpop(mylist, 130)    # heappush -> heappop  
print(f"Pop the smallest item: {pop}")
print('heappushpop', mylist)  

# heapreplace 先pop，然后再把item加入到堆中
pop = heapq.heapreplace(mylist, 2)    # heappop -> heappush  
print(f"Pop the smallest item: {pop}")
print('heapreplace', mylist)  