from django.shortcuts import render
from Quizapp.models import Exam,UserResults
from users.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator


lst = []
answers = Exam.objects.all()


@login_required
def examonline(request):
    results=Exam.objects.all()
    currentuser=User.objects.all()
    
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
    return render(request,'index.html',{"Exam":results,"questions":questions,"total_pages":total_pages})

def resultpage(request):
    
    results=Exam.objects.all()
    score=0
    lenlst=len(lst)
    print(lst)
    anslist = []
    for results in answers:
        anslist.append(results.Correct_ans)
    
    for i in range(len(lst)):
        if lst[i]==anslist[i]:
            score +=1
    return render(request,'result.html',{"score":score,'lenlst':lenlst,'lst':lst,'results':results})
def save_ans(request):
    
    ans = request.GET['ans']
    lst.append(ans)
    