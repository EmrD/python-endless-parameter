def plus(*args):
  numbers = []
  for i in args:
    numbers.append(i)
    for number in numbers:
      result = sum(numbers)
  return result

print(plus(1,2 , 3 , 4))