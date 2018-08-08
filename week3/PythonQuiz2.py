'''
SmallestNumber = (3,65,3)
print min(SmallestNumber)
'''

#1
def SmallestNumber(7,8,9):
    var = 7
    if 8<var:
        var = 8
    if 9<var:
        var = 9
        return var

#2
def SumOfEven(n):
    sum = 0
    for i in range(n):
        sum = sum + 2*(i+1)
    return sum
'''
#3
The output of the function would be 45
'''
