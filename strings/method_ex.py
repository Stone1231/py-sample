print("XßΣ".casefold()) # xssσ
print("XßΣ".lower()) # xßς
print("This is a 'string'.".upper()) # THIS IS A 'STRING'.
print("This is a 'string'.".lower()) # this is a 'string'.
print("this Is A 'String'.".capitalize()) # This is a 'string'. 第一個大寫,其他小寫
print("this Is a 'String'".title()) # This Is A 'String'
print("this iS A STRiNG".swapcase()) # THIS Is a strIng 大小寫相反
print(list(map(str.upper,["These","are","some","'strings'"]))) # ['THESE', 'ARE', 'SOME', "'STRINGS'"]

#translate:
translation_table = str.maketrans("aeiou", "12345")
my_string = "This is a string!"
translated = my_string.translate(translation_table)
print(translated)

#useful constants
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits) # 0123456789
print(string.hexdigits) # 0123456789abcdefABCDEF
print(string.octdigits) # 01234567
print(string.punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.whitespace) #  ' \t\n\r\x0b\x0c'
print(string.printable) # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

#去掉空白
print(" spacious string   ".strip()) # 'spacious string'
print(" spacious string   ".rstrip()) # '   spacious string'
print(" spacious string   ".lstrip()) # 'spacious string   '

#Reversing
print([char for char in reversed('hello')]) # ['o', 'l', 'l', 'e', 'h']
print(''.join(reversed('hello'))) # olleh

#split
print(" This is a sentence. ".split()) # ['This', 'is', 'a', 'sentence.']
print("Earth,Stars,Sun,Moon".split(',')) # ['Earth', 'Stars', 'Sun', 'Moon']
print("Earth,Stars,Sun,Moon".split(',', maxsplit=2)) # ['Earth', 'Stars', 'Sun,Moon'] 
print("Earth,Stars,Sun,Moon".rsplit(sep=',', maxsplit=2)) # ['Earth', 'Stars', 'Sun,Moon'] 

#replace
"Make sure to foo your sentence.".replace('foo', 'spam')

#isalpha
"Hello World".isalpha() # contains a space,False
"Hello2World".isalpha() # contains a number,False
"HelloWorld!".isalpha() # contains punctuation,False
"HelloWorld".isalpha() # True

#counting
s = "She sells seashells by the seashore."
s.count("sh") #2

s = "This is a test string"
s.startswith("Thi") # True
s.endswith(' string') # True
print("This is a test something".endswith(('.', 'something'))) # . or something is True

#Conversion between str or bytes
sb = b'\xc2\xa9 abc'
print(sb[0])
print(type(sb))

u = sb.decode('utf-8')
print(u[0])
print(type(u))

sb2 = u.encode('utf-8')
print(type(sb2))