
# PRE: n is an integer  
# POST: fibonacci serie result fro n 

def fibonacci(n):
    if(n < 0):
        return 0

    if(n == 0 or n == 1):
        return 1
    
    return n + fibonacci(n-1) 
