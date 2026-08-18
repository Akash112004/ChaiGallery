from django.shortcuts import render, redirect, get_object_or_404
from .forms import TeaForm
from .models import Tea


def home(request):
    teas = Tea.objects.all()[:4]

    return render(request, 'index.html', {
        'teas': teas
    })




def gallery(request):
    teas = Tea.objects.all()

    return render(request, 'gallery.html', {
        'teas': teas,
        'total_teas': teas.count(),
    })


def categories(request):
    teas = Tea.objects.all().order_by('-created_at')

    return render(request, 'categories.html', {
        'teas': teas
    })


def upload(request):

    if request.method == 'POST':

        form = TeaForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            tea = form.save(commit=False)

            tea.user = request.user

            tea.save()

            return redirect('gallery')

    else:
        form = TeaForm()

    teas = Tea.objects.all()

    return render(request, 'upload.html', {
        'form': form,
        'teas': teas
    })


def edit_tea(request, tea_id):

    tea = get_object_or_404(
        Tea,
        pk=tea_id,
        user=request.user
    )

    if request.method == 'POST':

        form = TeaForm(
            request.POST,
            request.FILES,
            instance=tea
        )

        if form.is_valid():

            tea = form.save(commit=False)

            tea.user = request.user

            tea.save()

            return redirect('gallery')

    else:

        form = TeaForm(
            instance=tea
        )

    teas = Tea.objects.all()

    return render(request, 'upload.html', {
        'form': form,
        'teas': teas,
        'tea': tea
    })


def tea_delete(request, tea_id):

    tea = get_object_or_404(
        Tea,
        pk=tea_id,
        user=request.user
    )

    if request.method == 'POST':

        tea.delete()

        return redirect('gallery')

    return render(request, 'gallery', {
        'tea': tea
    })


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def login_view(request):
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')