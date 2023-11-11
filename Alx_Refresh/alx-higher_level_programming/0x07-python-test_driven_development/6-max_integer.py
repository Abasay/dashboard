def max_integer(list=[]):
     """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
     max = 0
     if list is not isinstance(list, int):
          raise ValueError("must be a list of integers")
     if (len(list) == 0):
          return None
     
     numList = len(list)
     for elem in range(numList):
          if elem is not isinstance(elem, int):
               raise ValueError("must be an integer")
          if (list[elem] > max):
               max = list[elem]
     return max

if __name__ == "__main__":
     print(max_integer([4, 5, 1,6, 'r', '5']))