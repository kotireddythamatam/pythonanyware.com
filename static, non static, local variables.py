#static variables:
class X:
    """static variables"""
    a=100
    b=200
    def display(self):
        print(X.a)
        print(X.b)
        print(x1.a)
        print(x1.b)
        print(self.a)
        print(self.b)
print(X.a)
print(X.b)
x1=X()
print(X.a)
print(X.b)
print(x1.a)
print(x1.b)


#local variables:
class Y:
    """local variables"""
    def m1(self):
        a=100
        b=200
        print(a)
        print(b)
    def modify(self):
        a=a+10
        print(a)
    def m2(self):
        c=300
        d=400
        print(c)
        print(d)
y1=Y()
y1.m1()
y1.m2()
y2=Y()
y2.m1()
y2.m2()
print(y1)
print(y2)



#non static variables:
class Y:
    """non static variables"""
    def insert(self):
        self.a=100
        self.b=200
    def display(self):
        print(self.a)
        print(self.b)
        print(y1.a)
        print(y1.b)
y1=Y()
y1.insert()
y1.display()
print(y1.a)
print(y1.b)


class Z:
    """modifyin of non static variables"""
    def insert(self):
        self.a=100
        self.b=200
    def modify(self):
        self.a=self.a+10
        self.b-=10
    def display(self):
        print(z1.a)
        print(self.b)
z1=Z()
z1.insert()
z1.display()
z1.modify()
z1.display()


class Z:
    """constructor in non static variables"""
    def __init__(self):
        self.a=100
        self.b=200
    def display(self):
        print(self.a)
        print(self.b)
z1=Z()
z1.display()


class Z:
    """parameters passing through constructor in non static variables"""
    def __init__(self,a,b):
        self.k=a
        self.j=b
    def display(self):
        print(self.k)
        print(z1.j)
z1=Z(100,200)
z1.display()
z2=Z(300,400)
z2.display()
print(z1)
print(z2)

#static, non static, local variables:
class XYZ:
    """testing of static, non static, local variables"""
    a=100
    b=200
    def __init__(self):
        self.c=300
        self.d=400
    def m1(self):
        e=500
        f=600
        print(e)
        print(f)
    def display(self):
        print(xyz1.a)
        print(XYZ.b)
        print(xyz1.c)
        print(self.d)
xyz1=XYZ()
xyz1.display()
xyz1.m1()


#Real time project:
class Custmer:
    """custmer details of a SBI"""
    bankname="SBI"
    def __init__(self,custmername,custmeraddress,custmerid,custmerbalance):
        self.custmername=custmername
        self.custmeraddress=custmeraddress
        self.custmerid=custmerid
        self.custmerbalance=custmerbalance
    def deposit(self,depositamount):
        self.custmerbalance=self.custmerbalance+depositamount
    def withdraw(self,withdrawamount):
        self.custmerbalance=self.custmerbalance-withdrawamount
    def display(self):
        print(self.custmername)
        print(self.custmeraddress)
        print(self.custmerid)
        print(self.custmerbalance)
        print(Custmer.bankname)
c1=Custmer("ramu","guntur",17435,10000.00)
c1.display()
c2=Custmer("malli","hyderabad",56424,10000.00)
c2.deposit(2000.00)
c2.display()
c3=Custmer("govind","ongole",12345,10000.00)
c3.withdraw(4000.00)
c3.display()
print(c1)
print(c2)
print(c3)
