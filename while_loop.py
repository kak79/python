password = input("Please enter the password:   ")
#do not actually do a logon this way!!!
while password != 'opensesame':
  password = input("Invalid password, try again:   ")
print("Welcome!")