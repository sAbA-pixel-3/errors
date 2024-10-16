# исключения (errors) - syntax and logical errors

# try:
#     код, который может вызвать тсключение
# exept:
#     код, который выполгяется, если исключение возникает
# else:
#     код, кот. выполняется, если искл не возникает
# finally:
#     код, кот выполнится в любом случае


# try:
#     name = int(input("enter ur name: "))
#     print(10 / name) 
#     print(name) 
# except ValueError:
#     print("value error, must write a number") 
# except ZeroDivisionError:
#     print("Can't devide by ZERO!") 
# else:
#     print("Alles Gut!") 
# finally:
#     print("The END!") 

# print("Hello World!") 


# try:
#     name = int(input("enter ur name:"))
#     print(10 / name)
# except Exception as i: # for all errors
#     print(f"Error: {i}") 

# try:
#     name = "John"
#     print(name[4])
# except IndexError: 
#     print("must finish!") 

# try:
#     name = input("enter ur name: ")
#     mess = name / 5
#     print(name)
# except TypeError:
#     print("error") 







# functions


# def func_name():
#     print("Hello World!")



# встроенные фун-ии
# print() 
# input()
# sum()
# max()
# min() 

# кастомные (пользовательские)
# def hello_world():
#     print("HW") 
# # вызов фун-ии надо написать имя фун-ии и круглые скобки
# hello_world()

# def hello_w():
#     a = 5
#     b = 10
#     print(a+b)
# hello_w() 


# user_input = int(input("enter a num: "))
# def even():
#     if user_input % 2 == 0:
#         print("even")
#     else:
#         print("unevn")
# even() 

# user_input = int(input("enter a num: "))
# user_input1 = int(input("enter a num: "))
# def summa():
#     print(sum([user_input + user_input1]))
# summa() 

