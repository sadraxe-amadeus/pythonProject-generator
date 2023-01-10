# class User:
#     userName = "mohsen"
#     userFamily = "zandi"
#     userAge = 35
#
#     def showFullName(self):
#         return f"{self.userName} {self.userFamily}"
#
#
#     def __init__(self,userName,userFamily):
#         self.userName = userName
#         self.userFamily = userFamily
#
#
# mohsen = User("mohsen","zandi")
# ali = User("ali","safari")
#
# print(mohsen.showFullName())
#
# print(ali.showFullName())


class Car:
    def __init__(self,name,numberofDoors,color):
        self.name = name
        self.numberofDoors = numberofDoors
        self.color = color

    def showCarFullName(self):
        return f"car name is {self.name} & car color is {self.color}"

benz = Car("sls",2,"red")

print(benz.color)
print(benz.showCarFullName())