# def goods():
#     computers = int(input("Enter the number of computers "))
#     mens = int(input("Enter the number of mens : "))
#     containers = int(input("Enter the number of containers : "))

#     while(computers!=0 or mens!=0 or containers!=0):
#         print("The shipping company demands : ")
#         c = int(input("Company wants no. of computers : "))
#         m = int(input("Company wants no. of mens : "))
#         con = int(input("Company wants no. of containers : "))

#         if(c<=computers):
#             print("The %d no. of computers are allocated to the company ."%(c))
#             computers = computers-c;
#         else:
#             print("The company's demand is not possible .")
        
#         if(m<=mens):
#             print("The %d no. of computers are allocated to the company ."%(m))
#             mens = mens-m;
#         else:
#             print("The company's demand is not possible .")
        
#         if(con<=containers):
#             print("The %d no. of computers are allocated to the company ."%(m))
#             containers = containers-con;
#         else:
#             print("The company's demand is not possible .")

#         print("the remaining number of computer are %d , mens are %d , containers are %d"%(computers,mens,containers))

# if __name__ == '__main__':
#     goods()
        

# student={
#     "name":"Pawan",
#     "age" : 20,
#     "major":"computer science"
# }

# print("Name",student['name'])
# print("age",student['age'])
# print("major",student['major'])

# student['age'] = 21

# print("the updated dictionary is : ",student)



# dic2 = {
#     "Name" : ["Prakhar","Pawan","peeush"],
#     "Age" : [21,20,20],
#     "Major" : ["Computer Science","Computer Science","Computer Science"]
# }

# print(dic2)



# Now we use the concept of the lists 

# n = int(input("Enter the number of elements you wants to enter in the lists : "))

# lst = []

# for i in range(n):
#     ele = int(input())
#     lst.append(ele)

# print("the list you entered is : ",lst)

# choice = int(input("Enter your choice : "))

# def poped():
#     lst.pop()
#     print("The elements are poped from the list .")

# def removed():
#     lst.remove(lst[-1])
#     print("The last element is removed from the list ")

# match (choice):
#     case 1 : poped()
#     case 2 : removed()
#     case 3 : print("the choice is 3")

# import numpy as np 


# arr = np.random.randint(0,10,size=10)
# print(arr)

# print(arr**2)
# print(arr.mean())

# print(np.mean(arr))

# arr2 = np.random.randn(10)

# print(arr2)
# print(arr2.mean())
# # print()


with open("data.txt",'r') as file:
    data = file.read()

processed_data = data.upper()

with open("data.txt",'a') as file:
    file.write(processed_data)

print("processing file")