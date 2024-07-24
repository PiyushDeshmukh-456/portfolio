from django.shortcuts import render, redirect
from .models import Project, Resume
from .forms import ResumeForm

def home(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ResumeForm()

    projects = Project.objects.all()
    resume = Resume.objects.first()
    context = {
        'form': form,
        'resume': resume,
        'projects': projects,
    }
    return render(request, 'portfolio/index.html', context)
