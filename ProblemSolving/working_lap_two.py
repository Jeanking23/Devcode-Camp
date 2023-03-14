#Task 1: Happy Numbers
#write a  loop that a number is less than or equal to 1 and the number is equal or less than 4
# assign the number to a variable called happy_number
# if the number is equal to 1 or 4 return true

def happy_numbers(n):
    n = input("Enter a number: ")
    while n != 1 and n != 4:
        n = sum(int(i) ** 2 for i in str(n))
    return n == 1
print(happy_numbers(n))


#Task 2: Prime Numbers
# def prime_numbers():
#     for num in range(1, 101):
#         if num > 1:
#             for i in  range(2,num):
#                if num % i == 0:
#                    break
#             else:
#                    print(num)
# prime_numbers()

#

#Task 3: Fibonaci Numbers
# def fibonacci_numbers():
#     n = int(input("Enter a number: "))
#     n1 = 0
#     n2 = 1
#     count = 0
#     if n <= 0:
#         print("Please enter a positive integer")
#     elif n == 1:
#         print("Fibonacci sequence upto", n, ":")
#         print(n1)
#     else:
#         print("Fibonacci sequence:")
#         while count < n:
#             print(n1)
#             nth = n1 + n2
#             n1 = n2
#             n2 = nth
#             count += 1
# fibonacci_numbers()
# def fibonacci_number():
#    for numbers in range(1, 101):
#     count = 0
#     if numbers <= 0:
#        print(count)
#     elif numbers == 1:
#         print(numbers)
#         while count < numbers:
#             count += 1
# fibonacci_number()