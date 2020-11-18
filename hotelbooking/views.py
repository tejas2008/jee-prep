from django.shortcuts import render,HttpResponse
import datetime
from datetime import date

# Create your views here.
# def Hello1(request):
#     return  HttpResponse ("Hello!!! This is my first application")
def index(request):
    today = datetime.datetime.now().date()  
    x = datetime.datetime.now() 
    m=x.strftime("%m")
    d=x.strftime("%m")
    f_date = date(x.year, int(m), int(d))
    l_date = date(x.year, 12, 10)
    # l_date = date(x.year, 4, 10)
    delta = l_date - f_date
    rem=delta.days
    dict={'today':today,'rem':rem}
    return render(request, 'hotelbooking1/index.html',context=dict)

def quiz(request):
    return render(request, 'hotelbooking1/quiz.html')

def main(request):
    return render(request, 'hotelbooking1/main.html')

def advance(request):
    return render(request, 'hotelbooking1/advance.html')

