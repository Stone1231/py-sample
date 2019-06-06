from collections import deque
# Create a deque
dq = deque(["Mon","Tue","Wed"])
print (dq)

# Append to the right
print("Adding to the right: ")
dq.append("Thu")
print (dq)

# append to the left
print("Adding to the left: ")
dq.appendleft("Sun")
print (dq)

# Remove from the right
print("Removing from the right: ")
dq.pop()
print (dq)

# Remove from the left
print("Removing from the left: ")
dq.popleft()
print (dq)

# Reverse the dequeue
print("Reversing the deque: ")
dq.reverse()
print (dq)