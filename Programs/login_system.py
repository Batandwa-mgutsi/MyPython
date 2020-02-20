
# A  simple authentication system
# Batandwa Mgutsi
# 20/02/202

user1 = 'Bob'
user2 = 'Joe'
user3 = 'Alice'

user1Password = 'rtsfghd'
user2Password = 'gstysyhv'
user3Password = 'hhdguydhjh'

username = input("Please enter your username: ")
password = input("Enter Your password: ")

if(username == user1 and password == user1Password):
    print("Welcome", user1)
elif(username == user2 and password == user2Password):
    print("Welcome", user2)
elif(username == user3 and password == user3Password):
    print("welcome", user3)

else:
    print("Who the hell are you?")