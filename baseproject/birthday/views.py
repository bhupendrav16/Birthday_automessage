from django.shortcuts import render
from datetime import date
# Create your views here.

from birthday.models import Student
from birthday.smtp import send_message
from birthday.date_convertion import change_date


def navbar( request):
    return render( request,  "birthday/navbar.html")


def info ( request):
    s = Student.objects.raw("Select * from birthday_student")
    return render ( request, "birthday/info.html", {"students":s})


def birthday_day(request):
    today = str(date.today()) 
    today= change_date(today) 
    s = Student.objects.raw("SELECT * FROM birthday_student WHERE dob = 'today'")
    
    return render ( request, "birthday/birthday_day.html" ,{"students":s})
    
def home(request):
    return render(request, "birthday/home.html")
    

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        date_of_joining = request.POST.get('date_of_joining')  
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no') 
        obj_student = Student(name=name, address=address, dob=dob, date_of_joining=date_of_joining, email=email, phone_no=phone_no)
        obj_student.save()
        print("data is saved")
        today = str(date.today())
        if dob == today:
            print("in if condition")
        
            c = Student.objects.raw("SELECT * FROM birthday_student WHERE dob = 'today'")
            email = [entry.email for entry in c]
            name = [entry.name for entry in c]
            print(email,name)
            if ( len(email)!= 0 and len(name)!= 0):
                print("function called")
                send_message(email, name)            
            return render( request, "birthday/home.html" , {"students":c})
        else:
            print("else condition")
            
            c = Student.objects.raw("SELECT * FROM birthday_student ")
        
            return render( request,  "birthday/info.html", {"students":c})
    
    print("not saved")
    return render(request, "birthday/contact.html")


def messagepage(request):
    today = str(date.today())
    c = Student.objects.raw("SELECT * FROM birthday_student WHERE dob = 'today'")
    email = [entry.email for entry in c]
    name = [entry.name for entry in c]
    print(email,name)
    if ( len(email)!= 0 and len(name)!= 0):
        print("function called")
        send_message(email, name)            
    return render( request, "birthday/messagepage.html" , {"students":c})