def max_num(num1, num2, num3):
    maxNum = max(num1,num2,num3)
    
    print(maxNum)



max_num(-15,5,3)


def mult_list(list):
    num = 1
    for x in list:
        num = num * x

    print(num)

myList = [2,2,2,2]
mult_list(myList)

def rev_string(str):
    print(str[::-1])

rev_string("this is a string")

def num_within(num, min, max):
    within = False
    for x in range(min, max + 1):
        if x == num:
            within = True
            break

    print(within)   

num_within(3,1,10)

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)
    

pascal(2)

pascal(6)