def number(n):
    if n==0:
        return -1
    
    print(n)
    return number(n-1)

number(996)


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         print(n)
#         return n * factorial(n-1)



# factorial(5)
# print(factorial(5))