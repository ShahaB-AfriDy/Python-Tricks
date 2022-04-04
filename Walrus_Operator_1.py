# The Walrus(:=) Operator
# Walrus operators is one of the latest additions to Python.
# It was recently added to Python in Python version 3.8. It is an assignment expression that allows assignment directly in the expression.

List = [1,2,3]

if n:=len(List):
	print(n)

if (n:=len(List)) > 2:
	print(n)

# we declare and assign the value at the same time. That’s the power of the Walrus operator.