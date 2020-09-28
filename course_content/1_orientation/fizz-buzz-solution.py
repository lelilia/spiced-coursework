def fizzbuzz(n):
  for i in range(1,n+1):
    printStatement = ""
    if i % 3 == 0:
      printStatement += "Fizz"
    if i % 5 == 0:
      printStatement += "Buzz"
    if printStatement == "":
      printStatement = i
    print(printStatement)

fizzbuzz(100)
