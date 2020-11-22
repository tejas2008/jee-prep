from django.shortcuts import render,HttpResponse
import datetime
from datetime import date
from hotelbooking.models import Exam

def index(request):    
    return render(request, 'hotelbooking1/index.html',{'main_link':'http://127.0.0.1:8000/main/','adv_link':'http://127.0.0.1:8000/advance/'})

def quiz(request):
    if request.POST:
        marks = 0
        user_resp = []
        for i in range(30):
            try:
                ans = request.POST['radio'+str(i+1)]
                user_resp.append(ans)
                correct_ans = Exam.objects.filter(Qid=str(i+1))[0].Corrans
            except:
                user_resp.append("null")
                print("error")
            else:
                if ans==correct_ans:
                    marks += 4
                elif ans:
                    marks -= 1
        print(marks)
        print(user_resp)
        results=Exam.objects.all()
        value = 0
        return render(request,'hotelbooking1/marks.html',{"Exam":results,"marks":marks,'index':'http://127.0.0.1:8000/index/',"user_resp":user_resp,"value":value})
    else:
        results=Exam.objects.all()
        return render(request, 'hotelbooking1/quiz.html',{"Exam":results})
    

def main(request):
    return render(request, 'hotelbooking1/main.html',{'quiz_link':'http://127.0.0.1:8000/quiz/'})

def advance(request):
    return render(request, 'hotelbooking1/advance.html',{'quiz_link':'http://127.0.0.1:8000/quiz/'})



