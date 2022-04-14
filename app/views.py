from django.shortcuts import get_object_or_404, render, redirect
from .models import addClass
from .forms import addClassForm
# Create your views here.
def main(request):
    return render(request, 'app/main.html')

def manage(request):
    context ={}
    model = addClass.objects.filter(profname = request.user.id)
    
    context['model'] = model
    if request.method == 'POST':
        form = addClassForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.profname = request.user
            question.save()
            return redirect('app:manage')
    else:
        form = addClassForm()
        context['form'] = form
        
        return render(request, 'app/manage.html', context)