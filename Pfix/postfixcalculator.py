def calculate(expression):
	while True:
		arr = expression.split(" ")
		stacky = []

		while len(arr) > 0:
			item = arr.pop(0)

			if item != "+" and item != "-" and item != "*" and item != "/":
				stacky.append(int(item))

			elif item == "+":
				if len(stacky) > 1: 
					stacky.append(stacky.pop() + stacky.pop())

			elif item == "-":
				if len(stacky) > 1:
					tempo = stacky.pop()
					stacky.append(stacky.pop() - tempo)

			elif item == "*":
				if len(stacky) > 1:
					stacky.append(stacky.pop() * stacky.pop())

			else:
				tempo = stacky.pop()
				stacky.append(stacky.pop() / tempo)

		return stacky.pop()