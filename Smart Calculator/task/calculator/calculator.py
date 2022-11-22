from collections import deque

class Calculator:
    variables = {}
    stack = deque()

    def __init__(self):
        self.input = None

    def assign_var(self):
        components = self.input.replace("=", "").split()
        if not components[0].isalpha():
            print("Invalid identifier")
        elif components[1].isdigit():
            calc.variables[components[0]] = components[1]
        elif components[1].isalpha() and components[1] in calc.variables:
            calc.variables[components[0]] = calc.variables[components[1]]
        elif components[1].isalpha() and components[1] not in calc.variables:
            print("Invalid assignment")
        elif not components[1].isalpha() and not components[1].isdigit():
            num = [x for x in components[1] if x.isdigit()]
            var = [str(x) for x in components[1] if x in calc.variables]
            if len(var) > 0 and len(num) > 0:
                calc.variables[components[0]] = int(int(num[0]) * int(calc.variables[var[0]]))
            else:
                print("Invalid assignment")
            # components.append(components[1[1:]])
            # components[1] = components[1[0]]

    def calc_var(self, components):
        values = [self.variables[x]  if x.isalpha and x in calc.variables else x for x in components]
        self.input = " ".join(values)

    def handle_var(self):
        components = self.input.split()
        if "=" in self.input and self.input.count("=") == 1:
            if " " in self.input:
                self.assign_var()
            else:
                self.input = self.input.replace("=", " = ")
                self.assign_var()
        elif "=" in self.input and self.input.count("=") > 1:
            print("Invalid assignment")
        elif "+" in self.input or "-" in self.input or "*" in self.input or "/" in self.input:
            self.calc_var(components)
            #self.evaluate()
            print(int(eval(self.input)))
        else:
            if len(components) == 1 and components[0] in calc.variables:
                print(calc.variables[components[0]])
            else:
                print("Unknown variable")

    def execute(self):
        special = set("*()/")
        while True:
            nocont = False
            self.input = input()
            for i in range(len(self.input)):
                if self.input[i] in ["+", "-", "*", "/"] and self.input[i + 1] in ["+", "-", "*", "/"]:
                    print("Invalid expression")
                    nocont = True
                    break
            if self.input.startswith('/'):
                if self.input == "/help":
                    print("The program calculates the sum of numbers")
                    continue
                elif self.input == "/exit":
                    print("Bye!")
                    break
                else:
                    print("Unknown command")
                    continue
            elif self.input == '':
                continue
            if nocont == False:
                if any(x.isalpha() for x in self.input):
                    self.handle_var()
                elif self.input.endswith('-') or self.input.endswith('+'):
                    print("Invalid expression")
                    continue
                elif "(" in self.input and ")" not in self.input:
                    print("Invalid expression")
                    continue
                elif ")" in self.input and "(" not in self.input:
                    print("Invalid expression")
                    continue
                elif any(c in special for c in self.input):

                    for x in self.input:
                       if x in calc.variables:
                           x = calc.variables[x]
                    #self.input = [calc.variables[x] if  else x for x in self.input]
                    print(eval(self.input))
                elif self.input:
                    self.evaluate()

    def convert(self):
        result = deque()
        prio = ["*", "/", "^", "(", ")"]
        infix = self.input.split(" ")
        for x in infix:
            if x.isdigit():
                self.stack.append(int(x))
            elif len(self.stack) == 0:
                self.stack.append(x)
            elif self.stack[0] == "(":
                self.stack.append(x)
            elif x in prio and self.stack[0] not in prio:
                self.stack.append(x)
            elif (x in prio and self.stack[0] in prio) or (x not in prio and self.stack[0] in prio):
                result.append(self.stack.pop())
            elif x == "(":
                self.stack.append(x)
            elif x == ")":
                while self.stack[0] != "(":
                    result.append(self.stack.pop())
                if self.stack[0] == ")":
                    self.stack.pop()
                    continue
        while self.stack:
            result.append(self.stack.pop())
        return result







    def rpn(self):
        operators = ["+", "-", "*", "/", "^", "(", ")"]
        postfix = self.convert()
        for x in postfix:
            if x.isdigit():
                self.stack.append(x)
            elif x in calc.variables:
                self.stack.append(calc.variables[x])
            elif x in operators and len(self.stack) == 2:
                a = self.stack.pop()
                b = self.stack.pop()
                z= [a,x,b]
                self.stack.append(eval(" ".join(z)))
            elif x in operators and len(self.stack) == 1:
                a = self.stack.pop()
                z= [a,x]
                self.stack.append(eval(" ".join(z)))
        if len(self.stack) == 1:
            print(self.stack.pop())


    def evaluate(self):
        self.input = self.input.replace("+", "").split()
        i = 1
        while i < len(self.input):
            if not isinstance(self.input[i], int):
                if self.input[i].count("-") % 2 == 1:
                    del self.input[i]
                    self.input[i] = "-" + self.input[i]
                elif self.input[i].count("-") > 0:
                    del self.input[i]
                i += 1
        print(sum(int(number) for number in self.input))



calc = Calculator()
calc.execute()
