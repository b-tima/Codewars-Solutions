class Calculator(object):
    """
    With great inspiration from
    https://www.digitalocean.com/community/conceptual_articles/understanding-order-of-operations
    """

    def isFloat(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def infix2postfix(self, tokens):
        output = []
        operatorStack = []

        while len(tokens) > 0:
            c = tokens.pop(0)
            if self.isFloat(c):
                output.append(c)
            elif c != '(':
                while True:
                    if len(operatorStack) == 0:
                        operatorStack.append(c)
                        break
                    elif c in ['*', '/'] and operatorStack[0] in ['+', '-']:
                        operatorStack.insert(0, c)
                        break
                    elif (c in ['*', '/'] and operatorStack[0] in ['*', '/']) or (c in ['+', '-'] and operatorStack[0] in ['+', '-']):
                        last = operatorStack.pop(0)
                        output.append(last)
                        operatorStack.insert(0, c)
                        break
                    else:
                        last = operatorStack.pop(0)
                        output.append(last)
            else:
                right = "".join(tokens).rindex(')')
                output.extend(self.infix2postfix(tokens[0:right]))
                tokens = tokens[right+1:]

        output.extend(operatorStack)
        return output

    def evaluate(self, string):
        expression = self.infix2postfix(string.split(' '))
        
        stack = []

        while len(expression) > 0:
            token = expression.pop(0)
            if self.isFloat(token):
                stack.insert(0, float(token))
            else:
                b = stack.pop(0)
                a = stack.pop(0)
                if token == '+':
                    stack.insert(0, a + b)
                elif token == '-':
                    stack.insert(0, a - b)
                elif token == '*':
                    stack.insert(0, a * b)
                elif token == '/':
                    stack.insert(0, a / b)
        
        return stack[0]

        
if __name__ == "__main__":
    calc = Calculator()

    string = "( 5 + 3 ) * 10"

    result = calc.evaluate(string)

    print(result)