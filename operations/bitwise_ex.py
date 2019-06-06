# ~n = -|n+1| 
print(~0) #-1
print(~1) #-2
print(~123) #-124

# ~-n -> |n-1|
print(~-0) #-1
print(~-1) #0
print(~-123) #122

#Bitwise XOR
# 60 = 0b111100
# 30 = 0b011110
# 34 = 0b100010
print(60 ^ 30) # Out: 34

#Bitwise AND
# 60 = 0b111100
# 30 = 0b011110
# 28 = 0b11100
print(60 & 30) # Out: 28

#Bitwise OR
# 60 = 0b111100
# 30 = 0b011110
# 62 = 0b111110
60 | 30 # Out: 62

#Bitwise Left Shift
# 2 = 0b10
# 8 = 0b1000
print(2 << 2) # Out: 8
print(bin(2 << 2)) # Out: 0b1000
print(7 << 1) # Out: 14
print(3 << 4) # Out: 48

#Bitwise Right Shift
# 8 = 0b1000
# 2 = 0b10
print(8 >> 2) # Out: 2

a = 0b001
a &= 0b010
print(a) # 0b000

a = 0b001
a |= 0b010
print(a) # a = 0b011

a = 0b001
a <<= 2
print(a) # a = 0b100

a = 0b100
a >>= 2
print(a) # a = 0b001

a = 0b101
a ^= 0b011
print(a) # a = 0b110


#Bitwise NOT
# 0 = 0b0000 0000
print(~-1000)
# Out: -1
# -1 = 0b1111 1111

# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0

#Bitwise XOR (Exclusive OR)
60 ^ 30
# 60 = 0b111100
# 30 = 0b011110
# Out: 34
# 34 = 0b100010
bin(60 ^ 30)
# Out: 0b100010

print(bin(~1))

b = bin(60)
print(b)
print(~b) # TypeError: bad operand type for unary ~: 'str'
print(bin(~60))