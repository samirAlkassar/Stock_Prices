n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20,20]
def sockMerchant(n, ar): 
  # Write your code here\
  stack = []
  pairs=0
  for number in ar:
    if number not in stack:
      stack.append(number)
    else:
      stack.remove(number)
      pairs+=1
  return pairs
      
    


sockMerchant=sockMerchant(n,ar)
print(sockMerchant)

