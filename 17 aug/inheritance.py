# class parent:
#     surname=" "
#     village= " "
#     def __init__(self,surname,village) -> None:
#         self.surname=surname
#         self.village=village
#     def property(self):
#         a=input("Enter Money")
#         print(a)
#     def details(self):

#         print("Details:",self.surname,self.village)
# class child(parent):
#     def __init__(self,surname,village) -> None:
#         super().__init__(surname,village)
# rohan=child("Mane","Solapur")
# rohan.details()

# class bank_account:
#     def __init__(self, acc_no, acc_holder_name,acc_type,password,debit_card, credit_card):
#         self.acc_no=acc_no
#         self.acc_holder_name= acc_holder_name
#         self.acc_type= acc_type
#         self.password= password
#         self.debit_card = debit_card
#         self.credit_card = credit_card

#     def display_details(self):
#         print(f"Account No: {self.acc_no}")
#         print(f"Account Name: {self.acc_holder_name}")
#         print(f"Account Type: {self.acc_type}")
#         print(f"Password: {self.password}")
#         print(f"Debit Card: {self.debit_card}")
#         print(f"Credit Card {self.credit_card}")

# class savings_account(bank_account):
#     def __init__(self, acc_no, acc_holder_name, acc_type, password, debit_card, credit_card,FD,SIP,acc_balance):
#         super().__init__(acc_no, acc_holder_name, acc_type, password, debit_card, credit_card)
#         self.FD=FD
#         self.SIP=SIP
#         self.acc_balance=acc_balance
#     def show(self):
#         print(f"FD: {self.FD}")
#         print(f"SIP: {self.SIP}")
#         print(f"Account Balance: {self.acc_balance}")

# a=bank_account()
# a.show()


'''

Create a class bank_account that has the following attributes:

 1. acc_no

 2. acc_holder_name

 3. acc_type

 4. password

 5. boolean debit card

 6. boolean credit card

Make a subclass savings_account that has inherited parent class bank_account and

also has the below attributes added:

FD

SIP..

account_balance

Child class bank account has method that will show account balance if the

user enters correct password that was submitted while creating the account

If the user enters wrong password 3 times the account balance should change to zero

Make two more such classes as Loan account, Current account

'''

class bank_account:
  acc_no = " "
  acc_holder_name = " "
  acc_type = " "
  password = " "
  debit_card = False
  credit_card = False

  def __init__(self,a,b,c,d,e,f) -> None:
    self.acc_no = a
    self.acc_holder_name = b
    self.acc_type = c
    self.password = d
    self.debit_card = e
    self.credit_card = f
  def details(self):
    print("Here are a few details --- ", self.acc_holder_name , " and the account number is " , self.acc_no)
class savings_account(bank_account):
  fd = False
  sip = False
  account_balance = " "

  def __init__(self, a, b, d, e, f, g, h , i ) -> None:
    super().__init__(a, b, "Savings ", d, e, f)
    self.fd = g
    self.sip = h
    self.account_balance = i

  def about(self):
    print("Here is the savings account details", self.acc_holder_name, " " , self.acc_no)

  def check_balance(self):
    par = input("Enter your account password")

    if par == self.password:
      print("Tere account mei hai - ", self.account_balance)

    else:
      par = input("Please Reenter the password")
      if par == self.password:
       print("Tere account mei hai - ", self.account_balance)
      else:
       par = input("Please Reenter the password")
       if par == self.password:
        print("Tere account mei hai - ", self.account_balance)
       else:
        par = input("Please Reenter the password")

class loan_account(bank_account):

 loan_amount = 0

 si = 0

 time_period = 0

 bounce_charge = 0

 emi = 0

 closure = " "

 def __init__(self, a, b, d, e, f, g ,h , i , j , l) -> None:

   super().__init__(a, b, "Loan Account", d, e, f)

   self.loan_amount = g

   self.si = h

   self.time_period = i

   self.bounce_charge = j

   self.closure = l

   self.emi = (float)((self.loan_amount * self.si * 0.01) + self.loan_amount) / self.time_period

 def details(self):

  print(f"Loan Amount: {self.loan_amount}")

  print(f"Interest: {self.si}")

  print(f"Time Period: {self.time_period}")

  print(f"Bounce charge: {self.bounce_charge}")

  print(f"EMI: {self.emi}")

  print(f"Loan closure: {self.closure}")

 def loan_close(self):

   print(self.loan_amount * self.closure * 0.01 + self.loan_amount)

abcd = loan_account(1234, "Satish" , "12345678", False, False, 100000, 10, 12, 1000, 3)

abcd.details()

abcd.loan_close()

















































