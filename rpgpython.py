#Random Password Generator
import random

x = int(input("Enter the length of password to be generated\n"))
 

if x >=4:
        
        special_string = "!@#$%^&*()_+-=;<>?./"
        special_list = ",".join(special_string).split(',')

        special = ''
        y = random.randint(1,x-3)
        for i in range(1,y+1):
            special+=random.choice(special_list)


        digit = ''
        z = random.randint(1,x-y-2)
        for i in range (1,z+1):
            digit+=str(random.randint(0,9))


        upper = ''
        w = random.randint(1,x-y-z-1)
        for i in range (1,w+1):
            upper+=chr(random.randint(65,90))


        lower = ''
        u = (x-y-z-w)
        for i in range(1,u+1):
            lower+=chr(random.randint(97,122))



        password = special+lower+upper+str(digit)
        password_list = ",".join(password).split(",")
        random.shuffle(password_list)

        result = "".join(password_list)
        print(result)

else:
        print("Enter minimum password length of 4 characters")
