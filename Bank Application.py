class ourbank():
    nob  = 1
    ifsc = 'OUB102030'
    ROI  = 5
    def __init__(self,name,mob,bal,pin,Aadhar):
        self.name = name
        self.mob  = mob
        self.bal  = bal
        self.pin  = pin
        self.Adr  = Aadhar
    # the  below method is used to check the balance 
    def check_bal(self):
        if self.pin==self.takepin():
            print(f'Availabe balance is {self.bal}')
        else:
            print('Invalid pin')
    # the  below method is used to Depodite the amount 
    def deposite(self):
        if self.pin==self.takepin():
            amount = int(input('Enter the Amount:'))
            self.bal += amount
            print('amount is credited successfully...')
            print(f'Available balance is {self.bal}')
        else:
            print('Invalid pin')
    # Hear the method is used to withdraw the amount 
    def withdraw(self):
        if self.pin==self.takepin():
            amount = int(input('Enter the Amount:'))
            if amount <= self.bal:
                self.bal -= amount
                print('Amount is debited successfully...')
                print(f'Available balance is {self.bal}')
            else:
                print('Insuffcient funds')
        else:
            print('Invalid pin')
    #Hear you can change the class attributes
    @classmethod
    def croi(self):
        newv = float(input('Enter the new roi'))
        ourbank.ROI = newv
    # Pin checking by using stattic method
    @staticmethod
    def takepin():
        pasword =int(input('Enter the pin'))
        return pasword
user1 = ourbank('A',19282838,5000,1111,1029379)
user2 = ourbank('B',192182838,5000,2222,1029379)
user2.withdraw()
print('-'*20)
user2.deposite()
print('-'*20)
user2.check_bal()

            
        
            
            
 
            
