from django.shortcuts import render,HttpResponse
import datetime
from datetime import date
from hotelbooking.models import Exam,Chemistry,Math

def index(request):    
    return render(request, 'hotelbooking1/index.html',{'main_link':'/main/','adv_link':'/advance/'})

def quiz(request):
    if request.POST:
        marks = 0
        user_resp = []
        for i in range(30):
            try:
                ans = request.POST['radio'+str(i+1)]
                user_resp.append(ans)
                correct_ans1 = Exam.objects.filter(Qid=str(i+1))[0].Corrans

            except:
                user_resp.append("null")
                print("error")
            else:
                if ans==correct_ans1:
                    marks += 4
                elif ans:
                    marks -= 1

        for i in range(30,60):
            try:
                ans = request.POST['radio'+str(i+1)]
                user_resp.append(ans)
                correct_ans2 = Chemistry.objects.filter(Qid=str(i+1))[0].Corrans
                
            except:
                user_resp.append("null")
                print("error")
            else:
                if ans==correct_ans2:
                    marks += 4
                elif ans:
                    marks -= 1
        
        for i in range(60,90):
            try:
                ans = request.POST['radio'+str(i+1)]
                user_resp.append(ans)
                correct_ans3 = Math.objects.filter(Qid=str(i+1))[0].Corrans
            except:
                user_resp.append("null")
                print("error")
            else:
                if ans==correct_ans3:
                    marks += 4
                elif ans:
                    marks -= 1

        print(marks)
        print(user_resp)
        results=Exam.objects.all()
        results1=Chemistry.objects.all()
        results2=Math.objects.all()
        value = 0
        return render(request,'hotelbooking1/marks.html',{"Exam":results,"marks":marks,'index':'/index/',"user_resp":user_resp,"value":value,"results1":results1,"results2":results2})
    else:
        results=Exam.objects.all()
        print(results)
        print(type(results))
        results1=Chemistry.objects.all()
        results2=Math.objects.all()
        return render(request, 'hotelbooking1/quiz.html',{"Exam":results,"results1":results1,"results2":results2})

def quiz_adv(request):
    if request.POST:
        marks = 0
        user_resp = []
        for i in range(30):
            try:
                ans = request.POST['radio'+str(i+1)]
                user_resp.append(ans)
                correct_ans1 = Exam.objects.filter(Qid=str(i+1))[0].Corrans

            except:
                user_resp.append("null")
                print("error")
            else:
                if ans==correct_ans1:
                    marks += 4
                elif ans:
                    marks -= 1

        for i in range(30,60):
            try:
                ans = request.POST['radio'+str(i+1)]
                user_resp.append(ans)
                correct_ans2 = Chemistry.objects.filter(Qid=str(i+1))[0].Corrans
                
            except:
                user_resp.append("null")
                print("error")
            else:
                if ans==correct_ans2:
                    marks += 4
                elif ans:
                    marks -= 1
        
        for i in range(60,90):
            try:
                print(i)
                ans = request.POST['radio'+str(i+1)]
                user_resp.append(ans)
                correct_ans3 = Math.objects.filter(Qid=str(i+1))[0].Corrans
            except:
                user_resp.append("null")
                print("error")
            else:
                if ans==correct_ans3:
                    marks += 4
                elif ans:
                    marks -= 1

        print(marks)
        print(user_resp)
        results=Exam.objects.all()
        results1=Chemistry.objects.all()
        results2=Math.objects.all()
        value = 0
        return render(request,'hotelbooking1/marks.html',{"Exam":results,"marks":marks,'index':'/index/',"user_resp":user_resp,"value":value,"results1":results1,"results2":results2})
    else:
        results=Exam.objects.all()
        results1=Chemistry.objects.all()
        results2=Math.objects.all()
        return render(request, 'hotelbooking1/quiz_adv.html',{"Exam":results,"results1":results1,"results2":results2})
    

def main(request):
    return render(request, 'hotelbooking1/main.html',{'quiz_link':'/quiz/'})

def advance(request):
    return render(request, 'hotelbooking1/advance.html',{'quiz_adv_link':'/quiz_adv/'})



