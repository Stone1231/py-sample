
def ex1():
    prompt = "How many tickets do you need? " 
    num_tickets = input(prompt) 
    try: 
        num_tickets = int(num_tickets) 
    except ValueError: 
        print("Please try again.") 
    else: #successfully
        print("Your tickets are printing.")

def ex2():
    f_names = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt'] 
    for f_name in f_names: 
        # Report the length of each file found. 
        try: 
            with open(f_name) as f_obj: 
                lines = f_obj.readlines() 
        except FileNotFoundError: 
            # Just move on to the next file. 
            pass #continue running
        else: 
            num_lines = len(lines) 
            msg = "{0} has {1} lines.".format( f_name, num_lines) 
            print(msg)


def throw(x):
    if x in (3,4,5):
        return x**2
    raise Exception("You should provide a valid exponent")


#ex1()  
#ex2()      

print(throw(3)) #scuuess
try:
    print(throw(6)) #raise Exception
except Exception as identifier:
    print(identifier)
