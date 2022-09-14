class Input(object):
    def __init__(self):
        object.__init__(self)
    
    # return set of variables
    def getVarList(self, input):
        allOperators = {"^", "v", ">", "!", "(", ")"}
        varList = []
        # varList = [char for char in input if char not in allOperators and char not in varList]
        for char in input:
            if char not in allOperators and char not in varList:
                    varList.append(char)
        
        return varList

    # reduce input down to single character operators
    def replaceOperators(input):
        input = input.upper()
        replaceDict = {
            " ": "",
            "AND": "^",
            "OR": "v",
            "->": ">",
            "~": "!",
            "[": "(",
            "]": ")" 
        }
        for key in replaceDict:
            input = input.replace(key, replaceDict[key])
        return input.lower()

    # switches out variables for their values
    def replacePostFix(postFix, varList, valList):
        postFix = list(postFix)
        for pos, i in enumerate(varList):
            for char in range(len(postFix)):
                if postFix[char] == i:
                    postFix[char] = str(valList[pos])
        return "".join(postFix)
    
    # check if balanced number of parentheses
    def isBalanced(input):
        stack = []
        # posStack = []
        for pos, char in enumerate(input):
            if char == "(":
                stack.append(char)
                # posStack.append(pos)
            elif char == ")":
                try:
                    stack.pop()
                except:
                    return False#, posStack
        if len(stack) > 0:
            return False#, posStack
        else:
            return True#, posStack
    
    # returns precedence of operator
    def getPrecedence(input):
        precedenceDict = {
            "(": 0,
            ">": 1,
            "v": 2,
            "^": 3,
            "!": 4,
            ")": 5,
        }
        return precedenceDict[input]

    # converts infix to postfix
    def convertToPostFix(self,input):
        allOperators = {"^", "v", ">", "!", "(", ")"}
        stack = []
        result = ""
        for char in input:
            if char not in allOperators:
                result += char
            else:
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    popped = stack.pop()
                    while popped != "(":
                        result += popped
                        popped = stack.pop()
                else:
                    while (len(stack) != 0) and self.getPrecedence(char) <= self.getPrecedence(stack[-1]):
                        result += stack.pop()
                    stack.append(char)
        while len(stack) != 0:
            result += stack.pop()
        return result


def main():
    pass

if __name__ == "__main__":
    main()
