class Calculator:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        
    def get_precedence(self, operator):
        return self.operators.get(operator, 0)

    def is_operator(self, char):
        return char in self.operators

    def infix_to_postfix(self, expression):
        result = []
        stack = []

        for char in expression:
            if char.isalnum():  
                result.append(char)
            elif char == '(':  
                stack.append(char)
            elif char == ')':  
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()  
            elif self.is_operator(char):
                while stack and self.get_precedence(stack[-1]) >= self.get_precedence(char):
                    result.append(stack.pop())
                stack.append(char)

        while stack:
            result.append(stack.pop())

        return ''.join(result)

    def evaluate_postfix(self, expression):
        stack = []

        for char in expression:
            if char.isalnum():  
                stack.append(float(char))
            elif self.is_operator(char):
                operand2 = stack.pop()
                operand1 = stack.pop()

                if char == '+':
                    stack.append(operand1 + operand2)
                elif char == '-':
                    stack.append(operand1 - operand2)
                elif char == '*':
                    stack.append(operand1 * operand2)
                elif char == '/':
                    stack.append(operand1 / operand2)
                elif char == "^":
                    stack.append(operand1 ** operand2)

        return stack[0]


expression_converter = Calculator()
input_expression = "3 + 4 * 2 / (1 - 5) ^ 2 "
postfix_expression = expression_converter.infix_to_postfix(input_expression)
result = expression_converter.evaluate_postfix(postfix_expression)

print(f"Infix вираз: {input_expression}")
print(f"Зворотній польський запис: {postfix_expression}")
print(f"Результат обчислення: {result}")