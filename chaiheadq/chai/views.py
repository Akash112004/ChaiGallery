from django.shortcuts import render,redirect,get_object_or_404
from .forms import TeaForm
from .models import Tea
def index(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'index.html')

def categories(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST':
        form = TeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = TeaForm()

    teas = Tea.objects.all()
    return render(request, 'upload.html', {'form': form, 'teas': teas})

def about(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'index.html')

def upload_tea(request):
    if request.method == 'POST':
        form = TeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = TeaForm()

    teas = Tea.objects.all()
    return render(request, 'upload.html', {'form': form, 'teas': teas})


def edit_tea(request, tea_id):
    tea = get_object_or_404(Tea, id=tea_id)

    if request.method == 'POST':
        form = TeaForm(request.POST, request.FILES, instance=tea)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = TeaForm(instance=tea)

    teas = Tea.objects.all()
    return render(request, 'upload.html', {'form': form, 'tea': tea, 'teas': teas})    