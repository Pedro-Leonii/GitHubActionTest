from functions import fibonacci

if __name__ == '__main__':
	
	val = int(input("Insert a natural number: "))
	
	print("fibonacci series of {} is: {}".format(val, fibonacci(val)))