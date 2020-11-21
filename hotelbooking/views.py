from django.shortcuts import render,HttpResponse
import datetime
from datetime import date
from hotelbooking.models import Exam

# Create your views here.
# def Hello1(request):
#     return  HttpResponse ("Hello!!! This is my first application")
def index(request):    
    return render(request, 'hotelbooking1/index.html',{'main_link':'http://127.0.0.1:8000/main/','adv_link':'http://127.0.0.1:8000/advance/'})

def quiz(request):
    if request.POST:
        marks = 0
        for i in range(3):
            ans = request.POST['radio'+str(i+1)]
            correct_ans = Exam.objects.filter(Qid=str(i+1))[0].Corrans
            print(correct_ans)
            print(ans)
            if ans==correct_ans:
                marks += 4
            else:
                marks -= 1
        print(marks)
        results=Exam.objects.all()
        return render(request,'hotelbooking1/marks.html',{"Exam":results,"marks":marks})
    else:
        results=Exam.objects.all()
        return render(request, 'hotelbooking1/quiz.html',{"Exam":results})

def main(request):
    return render(request, 'hotelbooking1/main.html',{'quiz_link':'http://127.0.0.1:8000/quiz/'})

def advance(request):
    return render(request, 'hotelbooking1/advance.html',{'quiz_link':'http://127.0.0.1:8000/quiz/'})



