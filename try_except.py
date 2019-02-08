try:
	import file1
	print("Hi")
except:
	print("file not found")

L=[]
try:
	print(L[1])
except:
	print("Index Error")

try:
	meruert("Wrong command")
except:
	print("Syntax Error")


