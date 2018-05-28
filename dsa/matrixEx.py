from numpy import * 
#from array import * 不是這個

#adding a column
m = array([
    ['Mon',18,20,22,17],
    ['Tue',11,18,21,18],
    ['Wed',15,21,20,19],
    ['Thu',11,20,22,21],
    ['Fri',18,17,23,22],
    ['Sat',12,22,20,18],
    ['Sun',13,15,19,16]])
    
m_c = insert(m,[5],[[1],[2],[3],[4],[5],[6],[7]],1)
print(m)
print(m_c)

#Delete a row form a Matrix
m_dr = delete(m,[2],0) 
print(m_dr)

#Delete a column from a Matrix
m_dc = delete(m,s_[2],1)
print(m_dc)

#Update a row in in a Matrix
m_up = copy(m)
m_up[3] = ['Thu',0,0,0,0]
print(m_up)