email="rajamouli@gmail.com"
pwd="Raja8"
cemail=input("enter your email:")
cpwd=input("enter your cpwd:")
if(email==cemail and pwd==cpwd):
    print("login successful")
elif(email==cemail and pwd!=cpwd):
    print("login failed due to wrong password")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to incorrect email")
else:
    print("login failed due to incorrect email and password")
    
