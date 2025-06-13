password = input("Enter password: ")
number = "1234567890"
symbols = '''.,'/<>:;?"[]}|-{_=+!#$\\%^&*()`~'''

len_flag = False
n_flag = False
s_flag = False

if len(password) >= 8:
    len_flag=True
for i in number:
    if i in password:
        n_flag=True
        
for i in symbols:
    if i in password:
        s_flag=True

if len_flag and n_flag and s_flag:
    print("Password has been created.")
elif len_flag == False:
    print("Passowrd too short.")
elif n_flag == False:
    print("Passowrd must contain a number.")
elif s_flag == False:
    print("Passowrd must contain a special symbol.")
