#   Expression class for Part One
class Expression :

    def __init__ (self, expr) :
        self.expr = list(expr)

    def binop (self, a, b, op):
        '''Takes two numbers and an operation, and evaluates the binary operation.'''
        a = int(a)
        b = int(b)

        if op == "*":
            return a * b
        elif op == "+":
            return a + b


    #   Takes expressions with brackets and evaluates the brackets to produce an equiv. bracketless expression.
    def expand_brackets (self):
        '''IN PLACE operation to remove brackets from an expression.'''
        if "(" not in self.expr:
            pass # as it is already a bracketless expression.
        else:
            while "(" in self.expr:
                cl = self.expr.index(")") # find first closing bracket
                op = cl
                while self.expr[op] != "(": # work backwards to find corresponding opening bracket
                    op -= 1

                term = self.expr[op+1 : cl] # the inside of the brackets collected together
                exp = Expression(term)
                term = exp.evaluate_lr() # calculate the inside of the brackets
                
                self.expr = self.expr[:op] + [term] + self.expr[cl+1:]

        return self.expr

    #   Takes bracketless expressions, e.g. 6+7*4+3*9
    def evaluate_lr (self):
        '''Takes an expression (w/o brackets) as a list and evaluates left to right with no precedence over a particular operation.'''
        store = []
        for term in self.expr:
            store.append(term)
        store.reverse()

        while len(store) > 1:
            a = store.pop() # take first term
            op = store.pop() # take operator
            b = store.pop() # take second term

            binop = self.binop(a, b, op)

            store.append(binop)
        
        self.expr = store

        return int(self.expr[0])


    #   Part One computes expressions without precedence, therefore calls evaluate_lr 
    def evaluate (self):
        return self.evaluate_lr() 


#   Expression class for Part Two
class ExpressionPrecedence (Expression) :
    
    #   Takes a bracketless expression as a list, evaluates addition first and then left to right for multiplication.
    def evaluate_precedence (self):
        store = []
        for term in self.expr:
            store.append(term)
        store.reverse()

        while "+" in store:
            plus = store.index("+") # find first add operation (a + b)
            left = store[plus-1] # take element on left (a)
            right = store[plus+1] # take element on right (b)

            term = self.binop(left, right, "+")

            store = store[: plus-1] + [term] + store[plus+2:]
        
        while len(store) > 1:
            a = store.pop() # take first term
            op = store.pop() # take operator
            b = store.pop() # take second term

            binop = self.binop(a, b, op)

            store.append(binop)
        
        self.expr = store

        return int(self.expr[0])


    def expand_brackets(self):
        '''IN PLACE operation to remove brackets from an expression.'''
        if "(" not in self.expr:
            pass # as it is already a bracketless expression.
        else:
            while "(" in self.expr:
                cl = self.expr.index(")") # find first closing bracket
                op = cl
                while self.expr[op] != "(": # work backwards to find corresponding opening bracket
                    op -= 1

                term = self.expr[op+1 : cl] # the inside of the brackets collected together
                exp = ExpressionPrecedence(term)
                term = exp.evaluate_precedence() # calculate the inside of the brackets
                
                self.expr = self.expr[:op] + [term] + self.expr[cl+1:]

        return self.expr

    def evaluate (self):
        return self.evaluate_precedence()



#   Puzzle Input
with open("day18input.txt", "r") as file:
    data = file.read().split("\n")


# #   PART ONE
expressions = [ expr.replace(" ", "") for expr in data ] # remove spaces in the expressions
expressions = [ Expression(expr) for expr in expressions ]


for expr in expressions:
    expr.expand_brackets() # evaluate brackets in the expression
    expr.evaluate() # evaluate the expression left to right

total1 = 0
for expr in expressions:
    total1 += expr.expr[0]

print("The solution to Part One is", total1)


#   PART TWO
expressions = [ expr.replace(" ", "") for expr in data ] # remove spaces in the expressions
expressions = [ ExpressionPrecedence(expr) for expr in expressions ]

for expr in expressions:
    expr.expand_brackets() # evaluate brackets in the expression
    expr.evaluate() # evaluate the expression left to right

total1 = 0
for expr in expressions:
    total1 += expr.expr[0]

print("The solution to Part Two is", total1)

