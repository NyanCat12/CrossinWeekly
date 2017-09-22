import math

def uniquePath(m,n):
	return ((math.factorial(m+n-2))/((math.factorial(m-1))*(math.factorial(n-1))))

if __name__ == "__main__":
	print (uniquePath(1,1))
	print (uniquePath(3,3))
	print (uniquePath(10,20))
