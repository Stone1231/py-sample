from datetime import datetime as dt 

today = dt.now() 
date_string = dt.strftime(today, '%m/%d/%Y') 
print(date_string)

