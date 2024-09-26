# print("Hello world")
# name="roshini"
# print("I am "+name)

# print(10, 10)
# # arthmetic operator
# num1=int(input("Enter number1:"))
# num2=int(input("Enter number2:"))
# print("Addition",num1+num2)
# print("Subraction",num1-num2)
# print("Multiplication",num1*num2)
# print("Division",num1/num2)
# print("Modulus",num1%num2)
# print("Floor Division",num1//num2)
# print("Power",num1**num2)

# #comparison operator
# x=20
# y=30
# # print(x>y,x<y,x==y,x!=y)

# #logical operator
# print(x>y or x==y)

# #assignment orperator
# a=10
# b=20
# a+=b
# print(a)


# #if else statement
# num=int(input("Enter number"))

# if num%2==0:
#     print(num,"is a even number")
# else:
#     print(num,"is a odd number")

# num3=20

# if num3!=20:
#     print("If statement is executed")
# elif num3==20:
#     print("elif statement is executed")
# else:
#     print("else statement is executed")

# # Nested if
# r=10
# if r==10:
#     if r>=5:
#         print("Inside if is executed")
#     else:
#         print("inside else is executed")
# else:
#     print("else is executed")

# age=65
# if age<5:
#     print("Child")
# elif age>=5 and age<20:
#     print("Teenage")
# elif age>=20 and age<55:
#     print("Adult")
# elif age>=55 and age<65:
#     print("Retirement")
# else:
#     print("Rest")



#list

vegetables=["carrot", "betroot", "tomato", "onion", "brinjal"]
fruits=["apple", "banana", "cherry"]

print(vegetables)
print(vegetables[3])
vegetables.pop()
vegetables.append("raddish")

print(vegetables)
vegetables.remove("tomato")
print(vegetables)
fruits.extend(vegetables)
print(fruits)

#tuple ordered amd immutable because we cannot modify the values inside tuple  
students=("Rosini", "Rakesh", "Nila", "Sibi")
print(students)
students=("Rosini", "Rakesh", "Nila")
print(students)

print(students[2])


# students[2]="Hari"
print(students)  

#tyoecasting
students=list(students)  
print(students)


#set data type 
friends={"neela", "Sibi", "suganya", "hari"}
friends.add("snekha") #adding a single element
friends2=["saranya", "tamil"]
friends.update(friends2)
print(friends)
friends=list(friends)
print(friends[3])
friends.append("priya") #if we change the datatype then the list function will be performed
print(friends)










