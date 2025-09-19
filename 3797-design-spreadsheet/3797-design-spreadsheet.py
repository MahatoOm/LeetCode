class Spreadsheet:

    def __init__(self, rows: int):
        self.ss = [[0 for _ in range(26) ] for _ in range(rows) ]
        

    def setCell(self, cell: str, value: int) -> None:
        
        row = cell[1:]
        col = cell[0]
        self.ss[int(row) -1 ][ord(col) - 65] = value

    def resetCell(self, cell: str) -> None:
        row = cell[1:]
        col = cell[0]
        self.ss[int(row) -1 ][ord(col) - 65] = 0
        

    def getValue(self, formula: str) -> int:
        formula = formula[1:].split('+')
        result = 0
        for datapoint in formula:
            if datapoint.isdigit():
                result += int(datapoint)
            else:
                row = datapoint[1:]
                col = datapoint[0]
                result += self.ss[int(row) -1 ][ord(col) - 65]
        return result
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)