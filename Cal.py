from uu import Error


def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y


print("\n Select Operations \n1) ADD \n2) SUBTRACT \n3) MULTIPLY \n4) DIVIDE")

while(True):
    chc=input("Enter Your Choice (1/2/3/4)")
    if chc in ('1','2','3','4'):
        try:
            a=int(input("Enter the first number"))
            b=int(input("Enter the second number"))
        except Error:
            print("\n Please Enter a correct value")
            continue
        if chc=='1':
            print(a,"+",b,"=", add(a,b))
        elif chc=='2':
            print(a,"-",b,"=",subtract(a,b))
        elif chc=='3':
            print(a,"*",b,"=",multiply(a,b))
        elif chc=='4':
            print(a,"/",b,"=",divide(a,b))
        next=input("Lets do the next calculation? (yes/no): ")
        if next =="no":
            break
    else:
        print("\n Invalid Input")   

   

