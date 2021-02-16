# Wesley Murray
# 2/16/2021
# This file was created to house dynamic programming utilities.
# This goal is to have a program that can solve any dynamic programming problem.
# It will define a standard template that problems will be transformed into.

#create a class to represent items
class Item():
    def __init__(self,itemId,cost,value):
        self.__id=itemId
        self.__cost=cost
        self.__value=value

    def getCost(self):
        return self.__cost

    def getValue(self):
        return self.__value

    def getId(self):
        return self.__id

#Set up the dynamic programming problem
class OptimizationProblem():
    #Create a collection of items for dynamic programming solutions
    @staticmethod
    def createItemCollection(costs,values):
        if costs==None or values==None: return None
        if len(costs)!=len(values): return None

        items =[]
        for i in range(len(costs)):
            items.append(Item(i,costs[i],values[i]))
        return items

    def __init__(self,items,limit):
        self.__items=items
        self.__numItems=len(items)
        self.__limit=limit
        self.__table=None
        self.__solution=None

    def solve(self):
        #create table
        #get solution from table
        pass

    def _createTable(self):
        table = TwoDList(self.__numItems+1,self.__limit+1)
        for i in range(1,table.getNumRows()):
            for j in range(1,table.getNumCols()):
                valueAbove=table.get(i-1,j)
                valueWithCurrObject=table.get(i-1,j-self.__items[i-1].getCost())+self.__items[i-1].getValue() if j-self.__items[i-1].getCost()>=0 else 0
                table.replace(i,j,max(valueAbove,valueWithCurrObject))
        self.__table=table

    def _parseTableForSolution(self):
        self.__solution=[]
        table=self.__table
        row=-1
        col=-1
        value=table.get(row,col)
        while value>0:
            if table.get(row-1,col)==value:
                row-=1
                continue
            
            self.__solution.append(self.__items[row].getId())
            value-=self.__items[row].getValue()
            while table.get(row,col)!=value: 
                if col%table.getNumCols()!=0:
                    col-=1
                else:
                    row -=1
                    col+=table.getNumCols()-1
                if row<(-table.getNumRows()):
                    value=0
                    break

    def getSolution(self):
        return self.__solution

    def getTable(self):
        return self.__table

#helper class to make working with 2D lists easier.
class TwoDList(list):
    #constructor
    def __init__(self,numRows,numCols):
        self.__numRows=numRows
        self.__numCols=numCols
        super().__init__([0]*numRows*numCols)

    #convert 2D index to 1D
    #Support negative indices
    def __2Dto1DIndex(self,row,col):
        adj=0 if col>=0 else self.__numCols
        return row*self.__numCols+adj+col

    #get item from list
    def get(self,row,col):
        return super(TwoDList,self).__getitem__(self.__2Dto1DIndex(row,col))

    #replace item in list
    def replace(self,row,col,val):
        list.__setitem__(self,self.__2Dto1DIndex(row,col),val)

    def getNumCols(self):
        return self.__numCols

    def getNumRows(self):
        return self.__numRows