#Lab #0
#Due Date: 01/22/2021, 11:59PM
"""
### Collaboration Statement:

"""

def sumSquares(aList):
    """
        >>> sumSquares(5)
        >>> sumSquares('5') is None
        True
        >>> sumSquares(6.15)
        >>> sumSquares([1,5,-3,5,9,8,14,-25])
        277
        >>> sumSquares(['14',5,-3,5,9.0,8,14,7,'Hello'])
        245
    """
    sum = 0
    if type(aList) == list:
      for num in aList:
        if type(num) == int and (num % 3 == 0 or num % 7 == 0) and num > 0:
          sum += num*num
    else:
      return None
    return sum


## Uncomment next 3 lines if not running doctest in the command line
#if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
