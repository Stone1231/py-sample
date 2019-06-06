i = 10
f = 1.5
s = "foo"
l = ['a', 1, 2]
d = {'a': 1, 2: 'foo'}
#The following statements are all equivalent
#"10 1.5 foo ['a', 1, 2] {'a': 1, 2: 'foo'}"
print("{} {} {} {} {}".format(i, f, s, l, d))
print(str.format("{} {} {} {} {}", i, f, s, l, d))
print("{0} {1} {2} {3} {4}".format(i, f, s, l, d))
print("{0:d} {1:0.1f} {2} {3!r} {4!r}".format(i, f, s, l, d))
print("{i:d} {f:0.1f} {s} {l!r} {d!r}".format(i=i, f=f, s=s, l=l, d=d))
print(f"{i} {f} {s} {l} {d}")
print(f"{i:d} {f:0.1f} {s} {l!r} {d!r}")

#Object attributes
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('My value is: {0.value}'.format(my_value)) # "0" is optional, Out: "My value is: 6"

#Dictionary
my_dict = {'key': 6, 'other_key': 7}
print("My other key is: {0[other_key]}".format(my_dict)) # "0" is optional, Out: "My other key is: 7"
print("My other key is: {m[other_key]}".format(m=my_dict))

my_dict2 = {'first': 'Hodor', 'last': 'Hodor!'}
print('{first} {last}'.format_map(my_dict2)) #Hodor Hodor!
print('{first} {last}'.format(first='Hodor', last='Hodor!')) #Without a dictionary

#tuple
my_list = ['zero', 'one', 'two']
print("2nd element is: {0[2]}".format(my_list)) # "0" is optional, Out: "2nd element is: two"

# < forces the field to be left-aligned within width.
# > forces the field to be right-aligned within width.
# ^ forces the field to be centered within width.
# = forces the padding to be placed after the sign (numeric types only).
print('{:~^20}'.format('Hello')) # ~~~~~~Hello~~~~~~
print('{:~<9s}, World'.format('Hello'))# Hello~~~~
print('{:~>9s}, World'.format('Hello'))# ~~~~Hello
print('{:0=6d}'.format(-123))# -00123
print('{:0=6d}'.format(123))#  000123
foo = 'bar'
print(f'{foo:^7s}') # ' bar '

t = (12, 45, 22222, 103, 6)
print('{0} {2} {1} {2} {3} {2} {4} {2}'.format(*t))
# Out: 12 22222 45 22222 103 22222 6 22222

number_list = [12,45,78]
print('\n'.join(map('the number is {}'.format, number_list)))

# Float formatting
print('{0:.0f}'.format(42.12345)) #42
print('{0:.1f}'.format(42.12345)) #42.1
print('{0:.3f}'.format(42.12345)) #42.123
print('{:.3f}'.format(42.12345))  #42.123
print('{0:.3e}'.format(42.12345)) #4.212e+01
print('{0:.0%}'.format(42.12345)) #4212%
print('{0:.1%}'.format(0.8235))    #82.3%

s = 'Hello'
a, b, c = 1.12345, 2.34567, 34.5678
digits = 2
print('{0}! {1:.{n}f}, {2:.{n}f}, {3:.{n}f}'.format(s, a, b, c, n=digits))
             #'Hello! 1.12, 2.35, 34.57'

#Formatting Numerical             
print('{:c}'.format(65)) # # Unicode character 'A'
print('{:d}'.format(0x0a)) # # base 10 '10'
print('{:n}'.format(0x0a)) # base 10 using current locale for separators '10'
print('{0:x}'.format(10)) # base 16, lowercase - Hexadecimal 'a'
print('{0:X}'.format(10)) # base 16, uppercase - Hexadecimal 'A'
print('{0:o}'.format(10)) # base 8 - Octal '12'
print('{0:b}'.format(10)) # base 2 - Binary '1010'
print('{0:#b}, {0:#o}, {0:#x}'.format(42)) # With prefix '0b101010, 0o52, 0x2a'
print('8 bit: {0:08b}; Three bytes: {0:06x}'.format(42)) # Add zero padding
                             #'8 bit: 00101010; Three bytes: 00002a'

r, g, b = (1.0, 0.4, 0.0)
print('#{:02X}{:02X}{:02X}'.format(int(255 * r), int(255 * g), int(255 * b)))
# '#FF6600'

