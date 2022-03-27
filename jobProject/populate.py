import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","jobProject.settings")
import django
django.setup()

from jobApp.models import Hydjobs,Punejobs,Mumbaijobs,Chennaijobs
from faker import Faker
from random import *
fake=Faker()

def phoneNumGen():
    d1=randint(7,9)
    num=str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populateHyd(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        feligibility=fake.random_element(elements=("BTech","MTech","MCA","MBA","PhD"))
        ftitle=fake.random_element(elements=("Project manager","Team Lead","Software Developer"))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phoneNumGen()
        Hydjobsrecord=Hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility = feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
    print("Data populated successfully")

def populatePune(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        feligibility=fake.random_element(elements=("BTech","MTech","MCA","MBA","PhD"))
        ftitle=fake.random_element(elements=("Project manager","Team Lead","Software Developer"))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phoneNumGen()
        Punejobsrecord=Punejobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility = feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
    print("Data populated successfully")

def populateChennai(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        feligibility=fake.random_element(elements=("BTech","MTech","MCA","MBA","PhD"))
        ftitle=fake.random_element(elements=("Project manager","Team Lead","Software Developer"))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phoneNumGen()
        Chennaijobsrecord=Chennaijobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility = feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
    print("Data populated successfully")
def populateMumbai(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        feligibility=fake.random_element(elements=("BTech","MTech","MCA","MBA","PhD"))
        ftitle=fake.random_element(elements=("Project manager","Team Lead","Software Developer"))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phoneNumGen()
        Mumbaijobsrecord=Mumbaijobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility = feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
    print("Data populated successfully")

populateHyd(25)
populatePune(25)
populateChennai(25)
populateMumbai(25)
