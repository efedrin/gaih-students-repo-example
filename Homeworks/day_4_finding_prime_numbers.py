def prime(first_number, last_number):
  number = first_number
  while (number <= last_number):
    count = 0
    i = 2
    while (i <= number//2):
      if (number % i == 0):
        count = count + 1
        break
      i = i + 1

    if (count == 0 and number != 1):
        print(" %d" %number, end = " ")
    number = number  + 1

prime(1,100)
