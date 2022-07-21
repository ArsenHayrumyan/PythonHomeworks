class Calc:
    def __init__(self, n1, op, n2):
        self.n1 = n1
        self.n2 = n2
        self.op = op
    
    def sum(self):
        if self.op == '+':
            return f'{self.n1} + {self.n2} = {self.n1 + self.n2}'
        if self.op == '-':
            return f'{self.n1} - {self.n2} = {self.n1 - self.n2}'
        if self.op == '*':
            return f'{self.n1} * {self.n2} = {self.n1 * self.n2}'
        if self.op == '/':
            return f'{self.n1} / {self.n2} = {self.n1 / self.n2}'

operation = Calc(int(input('Enter first number: ')), input('Enter operation: '), int(input('Enter second number: ')))
print(operation.sum())




