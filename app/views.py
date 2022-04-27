from django.shortcuts import get_object_or_404, render, redirect
from .models import Class, Quiz, RegClass, Score
from .forms import addClassForm
from django.db.models import Max, Min, Avg
# Create your views here.
def main(request):
    return render(request, 'app/main.html')

def manage(request):
    context ={}
    _class = Class.objects.filter(profid = request.user.id)
    context['class'] = _class
    if request.method == 'POST':
        form = addClassForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.profid = request.user
            question.save()
            return redirect('app:manage')
    else:
        form = addClassForm()
        context['form'] = form
        
        return render(request, 'app/manage.html', context)

def class_delete(request, deleteid):
    print(deleteid)
    model = Class.objects.filter(profid = request.user.id, id = deleteid)
    model.delete()
    return redirect('app:manage')

def quiz_student_print(request, class_id):
    context ={}
    _quiz = Quiz.objects.filter(profid = request.user.id, classid = class_id)
    _class = Class.objects.filter(profid = request.user.id)
    _student = RegClass.objects.filter(classid= class_id)
    context['quiz'] = _quiz
    context['class'] = _class
    context['form'] = addClassForm()
    context['student'] = _student
    context['classid'] = class_id
    
    return render(request, 'app/manage.html', context)

def quiz_delete(request, classid, quizdeleteid):
    model= Quiz.objects.filter(classid = classid, id = quizdeleteid)
    model.delete()
    return redirect('app:manage')

def enroll(request):
    return render(request, 'app/enroll.html')

def quizenroll_1(request):
    return render(request, 'app/quizenroll_1.html')

def student_print(request, classid, quizid):
    context ={}
    _quiz =  Quiz.objects.filter(classid= classid, profid = request.user.id)
    print(_quiz)
    _class = Class.objects.filter(profid = request.user.id)
    _student = RegClass.objects.filter(classid= classid)
    _grade = Score.objects.filter(classid = classid, quizid= quizid).values('id')
    print(_grade.query)
    context['quiz'] = _quiz
    context['class'] = _class
    context['form'] = addClassForm()
    context['student'] = _student
    context['classid'] = classid
    
    return render(request, 'app/manage.html',context)

def quizreg_1(request):
    return render(request, 'app/quizreg_1.html')