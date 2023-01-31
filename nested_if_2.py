email="rajamouli@gmail.com"
pwd="Raja8"
otp="8787"
cemail=input("enter your email:")
cpwd=input("enter your password:")

if(email==cemail and pwd==cpwd):
    rotp=int(input("enter your otp:"))

if(rotp==otp):
    print("login successful")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to wrong email")
elif(email==cemail and pwd!=cpwd ):
    print("login failed due to incorrect password")
else:
    print("login failed due to incorrect email and password")

    
