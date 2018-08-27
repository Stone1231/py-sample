import sys
import time

class StaticAttrs:
    Val = "hi"

gVal = "hello"

def print_classStaticAttrs():    
    print(StaticAttrs.Val)

    params = sys.argv[1:]
    
    StaticAttrs.Val = params[0]
    while(True):
        time.sleep(2)
        print(StaticAttrs.Val)    

def print_global():

    global gVal

    print(gVal)

    params = sys.argv[1:]
    
    gVal = params[0]
    while(True):
        time.sleep(2)
        print(gVal)

    

def main():
    if len(sys.argv) < 2: # 1
        print("Usage:", sys.argv[0], "<WHO>")
        sys.exit(1)       # 2

    #print_global()
    print_classStaticAttrs()

if __name__ == "__main__":
    main()