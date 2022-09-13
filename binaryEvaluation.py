class Calculation(object):
    def __init__(self):
        object.__init__(self)
        
    # evaluates and statements
    def binaryAnd(p,q):
        p = int(p)
        q = int(q)
        if p == 1 and q == 1:
            return 1
        else:
            return 0
        
    # evaluates or statements
    def binaryOr(p,q):
        p = int(p)
        q = int(q)
        if p == 1 or q == 1:
            return 1
        else:
            return 0
        
    # evaluates implication statements
    def binaryImp(p,q):
        p = int(p)
        q = int(q)
        # effectively negates p in order to fit to (¬p v q)
        p = (p+1) % 2

        if p == 1 or q == 1:
            return 1
        else:
            return 0
    

    def negation(p):
        p = int(p)
        p = (p+1) % 2
        return p
    # iterate through postFix, calling appropriate evaluation as needed
    def calculate(self, postFix):
        operatorSet = {"^", "v", ">", "!"}
        calcDict = {
            "^": self.binaryAnd,
            "v": self.binaryOr,
            ">": self.binaryImp,
            "!": self.negation
        }
        stack = []
        for char in postFix:
            if char not in operatorSet:
                stack.append(char)
            elif char == "!":
                right = stack.pop()
                result = calcDict[char](right)
                stack.append(result)
            else:    # should only evaluate if the current character is an operator
                right = stack.pop()
                left = stack.pop()
                result = calcDict[char](left,right)
                stack.append(result)
        try:
            return stack[0]
        except:
            pass


def main():
    pass

if __name__ == "__main__":
    main()
