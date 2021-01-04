from django.shortcuts import render
from Quizapp.models import Exam,UserResults
from users.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator


lst = []
@login_required
def examonline(request):
    results=Exam.objects.all()
    print(results)
    currentuser=User.objects.all()
    user_results=UserResults.objects.all()
    paginator=Paginator(results,1)
    
    total_pages = paginator.count
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        questions=paginator.page(page)
    except(EmptyPage,InValidPage):
        questions=paginator.page(paginator.num_pages)
    print(results)
    return render(request,'index.html',{"Exam":results,"questions":questions,"total_pages":total_pages,"user_results":user_results})

def resultpage(request):
    
    results=Exam.objects.all()
    score=0
    lenlst=len(lst)
    print(lst)
    user_results=UserResults.objects.all()
    anslist = []
    for i in results:
        anslist.append(i.Correct_ans)
    for i in range(len(lst)):
        if lst[i]==anslist[i]:
            score +=1
    return render(request,'result.html',{"score":score,'lst':lst,'results':results,'user_results':user_results})
def save_ans(request):
    Quiz=Exam.objects.all()
    if request.method=="POST":
        
        # if request.POST.get('answer'):
        #     savedata=UserResults.objects.first()
        #     savedata.results=request.POST.get('answer')
        #     if savedata.results==Quiz.Correct_ans:
        #         savedata.score+=1
        # savedata.save()
    return render(request,'result.html',{'savedata':savedata})

            
    
    