def irreducible_fraction(num1, num2):
    if num2 == 0:
        #return str(num1) + '/' + str(num2)
        return 'error'
    elif num1 % num2 == 0:
        return str(num1 / num2)
    else:        
        a = max(num1, num2)
        b = min(num1, num2)
        while (a % b != 0):
            _b = b
            b = a % b
            a = _b

        num1 /= b
        num2 /= b

        return str(int(num1)) + '/' + str(int(num2))

if __name__ == '__main__':
    print(irreducible_fraction(4, 6))
    print(irreducible_fraction(4, 12))
    print(irreducible_fraction(4, 0))
