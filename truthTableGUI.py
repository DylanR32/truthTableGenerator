from binaryEvaluation import Calculation
from parsing import Input
from tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.main()
    def main(self):
        self.textEntry = Entry(self,bg = "#252525", fg = "#c3c3c3")
        self.textEntry.grid(row = 1, column = 0, columnspan = 2, sticky = "we")
        self.calculateBtn = Button(self, text = "Calculate", command = lambda: self.calculate(),
                                   bg = "#252525", fg = "#c3c3c3")
        self.calculateBtn.grid(row = 2, column = 1, columnspan = 1, sticky = "we")
        self.keyBtn = Button(self, text = "Show Key", command = lambda: self.showKey(),
                                   bg = "#252525", fg = "#c3c3c3")
        self.keyBtn.grid(row = 2, column = 0, sticky = "we")

    def calculate(self):
        userIn = self.textEntry.get()
        userIn = Input.replaceOperators(userIn)
        varList = Input.getVarList(Input, userIn)
        length = len(varList)
        self.resultsLabelMaker(length)
    
    def resultsLabelMaker(self, length):
        self.results = Toplevel(self)
        self.results.title(f"Truth table for {self.textEntry.get()}")
        self.keyLbl = Button(self.results, text = "^ for and, v for or, > for implication, ! for negation",
                             command = lambda: self.showKey(),
                             bg = "#252525", fg = "#c3c3c3")
        self.keyLbl.grid(row = 0, column = 0, columnspan = length)
        self.formulaLbl = Button(self.results, text = self.textEntry.get(),
                                 bg = "#252525", fg = "#c3c3c3")
        self.formulaLbl.grid(row = 1, column = length + 1)
        self.spacerLbl = Button(self.results,
                               bg = "#252525", fg = "#c3c3c3")
        self.spacerLbl.grid(row = 0, column = length + 1, sticky = "we")
        input = self.textEntry.get()
        input = Input.replaceOperators(input)
        varList = Input.getVarList(Input, input)
        for pos, var in enumerate(varList):
            varLbl = Button(self.results, text = var,
                            bg = "#252525", fg = "#c3c3c3")
            varLbl.grid(row = 1, column = pos, sticky = "we")
        # the loop below plugs variable values into the evaluator,
        # then makes a label with the result
        for i in range(2**length):
            postFix = Input.convertToPostFix(Input, input)
            k = 0
            list = []
            for j in range(length):
                # complicated math that when used in conjunction with the two loops,
                # gives the variable value for the current row and current column
                # value is to be used in evaluation of the statement and used on label
                valueLbl = Button(self.results, text = i % (2**(length-j)) //
                                  (2**(length-(j+1))),
                                  bg = "#252525", fg = "#c3c3c3")
                valueLbl.grid(row = i+2, column = k, sticky = "we")
                k += 1
                list.append(i % (2**(length-j)) // (2**(length-(j+1))))
            postFix = Input.replacePostFix(postFix, varList, list)
            result = Calculation.calculate(Calculation, postFix)
            resultLbl = Button(self.results, text = result,
                               bg = "#252525", fg = "#c3c3c3")
            resultLbl.grid(row = i+2, column = k + 1, columnspan= 2, sticky = "we")
    

    def showKey(self):
        self.keyPage = Toplevel(self)
        keyDict = {
            ("^", ",", "and"):"AND",
            ("v", ",", "or"): "OR",
            ("->", ",", ">"): "IMPLICATION",
            ("~", ",", "!"):  "NEGATION",
        }
        operatorLbl = Button(self.keyPage, text = "Operator",
                            bg = "#252525", fg = "#c3c3c3")
        operatorLbl.grid(row = 0, column = 0, sticky = "we")

        operationLbl = Button(self.keyPage, text = "Operation",
                             bg = "#252525", fg = "#c3c3c3")
        operationLbl.grid(row = 0, column = 1, sticky = "we")
        for pos, key in enumerate(keyDict):
            keyLbl = Button(self.keyPage, text = key,
                           bg = "#252525", fg = "#c3c3c3")
            keyLbl.grid(row = pos + 1, column = 0, sticky = "we")
            meaningLbl = Button(self.keyPage, text = keyDict[key],
                               bg = "#252525", fg = "#c3c3c3")
            meaningLbl.grid(row = pos + 1, column = 1, sticky = "we")

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
