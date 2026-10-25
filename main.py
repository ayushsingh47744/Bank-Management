# we are creating json file such that user's data won't be deleted if we shut down our laptop
import json 
import random
import string 
from pathlib import Path 


class Bank:
    database = 'data.json'
    data = []
    
    try:
        if Path(database).exists():  #database ko load kr liya
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist ")
    except Exception as err:
        print(f"an exception occured as {err}")
    
    @classmethod
    def __update(cls): #static method he hum nhi chahte ki sb log yhi use kren
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):  #account number generate hoga yha
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k= 3)
        spchar = random.choices("!@#$%^&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)  #string me chahieye account number



    def Createaccount(self):  #account create krne ke liye kya chaheiye
        info = {
            "name": input("Tell your name :- "),
            "age" : int(input("tell your age :- ")),
            "email": input("tell your email :- "),
            "pin": int(input("tell your 4 number pin :- ")),
            "accountNo." : Bank.__accountgenerate(),
            "balance" : 0
        }
        if info['age'] < 18  or len(str(info['pin'])) != 4:
            print("sorry you cannot create your account")
        else:
            print("account has been created successfully")   #account create ho gya he ab data.json me daal denge
            for i in info:  #data key value pair me he hota he
                print(f"{i} : {info[i]}")
            print("please note down your account number")

            Bank.data.append(info)  #data.json me data ko daal diya he

            Bank.__update()
        

            

user = Bank()
print("press 1 for creating an account")
print("press 2 for Deposititing the money in the bank ")
print("press 3 for withdrawing the money ")
print("press 4 for details ")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response :- "))

if check == 1:
    user.Createaccount()
