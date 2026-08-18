from django.conf.locale import te
from django.http import request
from django.shortcuts import render,redirect,get_object_or_404
from .forms import TeaForm
from .models import Tea


def tea_categories():
   teas = Tea.objects.all().order_by('created_at')
   return render(request, 'categories.html', {'teas': teas})


   
def upload(request):
    if request.method == 'POST':
        form = TeaForm(request.POST, request.FILES)
        if form.is_valid():
             tea = form.save(commit=False)
             tea.user = request.user
             tea.save()
        return redirect('upload')
    else:
        form = TeaForm()

    teas = Tea.objects.all()
    return render(request, 'upload.html', {'form': form, 'teas': teas})


def edit_tea(request,tea_id):
    tea = get_object_or_404(Tea, pk=tea_id, user = request.user)
    if request.method == 'POST':
        form = TeaForm(request.POST, request.FILES,  instance=te)
        if form.is_valid():
            tea=form.save(commit=False)
            tea =form.user = request.user
            tea.save()
        return redirect('tea_categories')    
    else:
        tea = TeaForm(isinstance=tea)
    teas = Tea.objects.all()
    return render(request, 'upload.html', {'form': form, 'teas': teas})

def tea_delete(request, tea_id):
    tea = get_object_or_404(tea, pk=tea_id, user = request.user)
    if request.method == 'POST':
       tea.delete()
       return redirect('upload.html')
    return render(request, 'upload.html', { 'teas': teas})

def index(request):
    teas = Tea.objects.all()[:4]
    return render(request, 'index.html', {'teas': teas})

def home(request):
    """Backward-compatible ChaiGallery landing view."""
    teas = Tea.objects.all()[:4]
    return render(request, 'index.html', {'teas': teas})

def gallery(request):
    teas = Tea.objects.all()
    context = {
        'teas': teas,
        'total_teas': teas.count(),
    }
    return render(request, 'gallery.html', context)

def about(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'index.html')

