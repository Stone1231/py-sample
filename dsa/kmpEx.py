
def failure(s):

    length = len(s)
    p = [0] * length
    
    for i in range(1,length):        
    #for i := 1; i < length; i++

        j = p[i-1]
        while j > 0 and s[j] != s[i]:
            j = p[j-1]
        
        if s[j] == s[i]: 
            j+=1

        p[i] = j;
    
    return p

def KMP(t, p):
    
    f = failure(p)
    length = len(t)
    p_length = len(p)

    j = 0
    for i in range(0,length):        
        while j > 0 and p[j] != t[i]: 
            j = f[j-1] #再試次長相同前後綴
        if p[j] == t[i]:
            j +=1
        if j == p_length:
            j = 0
            print("位置" + str(i - p_length + 1) + "開始出現P")
    
#print(failure("113113211131132"))    
KMP("qtuueheheeejdiojdweoheheehfowei","hehee") 