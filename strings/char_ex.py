def get_char(num):
    s_char = 'A'
    e_char = ''
    if num < 26:
        e_char = chr(ord(s_char) + num)
    else:
        mod = num - 26
        e_char = 'A' + chr(ord(s_char) + mod)
    return e_char


for i in range(60):
    print(get_char(i))