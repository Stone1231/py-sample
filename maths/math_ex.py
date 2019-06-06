import math
import cmath

print(3 / 2) # = 1.5
print(7 // 2) # = 3
print(3 / 2.0) # = 1.5
print(3 // 2.0) # = 1.0
print(-3 / 2) # = -1.5
print(2 / 3) # = 0.6666666666666666
print(-3 / 10) # = -0.3
print(10 / 2) # = 5.0
print(7 % 4) # = 3

"first string " + "second string" # = 'first string second string'
[1, 2, 3] + [4, 5, 6] # = [1, 2, 3, 4, 5, 6]

print((2 ** 3)) # = 8
print(pow(2, 3)) # = 8
print(pow(2, 3, 2)) # 0, calculates (2 ** 3) % 2, 
                    # but as per Python docs,
                    # does so more efficiently

math.sqrt(4) # = 2.0 (always float; does not allow complex results)
cmath.sqrt(4) # = (2+0j) (always complex)
 
math.pow(8, 1/3) # evaluates to 2.0
8**(1/3) # evaluates to 2.0

math.sin(1) # returns the sine of 'a' in radians
# Out: 0.8414709848078965
math.cosh(2) # returns the inverse hyperbolic cosine of 'b' in radians
# Out: 3.7621956910836314
math.atan(math.pi) # returns the arc tangent of 'pi' in radians
# Out: 1.2626272556789115
math.hypot(1, 2) # returns the Euclidean norm, same as math.sqrt(a*a + b*b)
# Out: 2.23606797749979

print(math.hypot(5-1, 4-1)) #distance between two points (x1, y1) & (x2, y2)
                            #math.hypot(x2-x1, y2-y1)

math.exp(0) # 1.0
math.exp(1) # 2.718281828459045 (e)

math.log(5) # = 1.6094379124341003
math.log(5, math.e) # = 1.6094379124341003
cmath.log(5) # = (1.6094379124341003+0j)  Default is math.e
math.log(1000, 10) # 3.0 (always returns float)
cmath.log(1000, 10) # (3+0j)

# Logarithm base 2
math.log2(8) # = 3.0

# Logarithm base 10
math.log10(100) # = 2.0
cmath.log10(100) # = (2+0j)

print(math.log1p(pow(10, -16))) # = 1e-16  log(x+1)  
print(math.log(1 + pow(10, -16))) # = 0.0

print(math.expm1(math.exp(-15))) # = 1e-16  exp(x) - 1  
print(math.exp(-15)-1) # = 0.0
print(math.exp(-15)-1.0)

