from django.shortcuts import get_object_or_404, render, redirect
from .models import addClass
from .forms import addClassForm
# Create your views here.
def main(request):
    return render(request, 'app/main.html')

def classManage(request):
    if request.method == 'POST':
        form = addClassForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.profname = request.user
            question.save()
            print('qfqf')
            return redirect('app:grade')
    else:
        form = addClassForm()
        context ={'form': form}

        return render(request, 'grade/grade.html', context)