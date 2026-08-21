from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TeaForm
from .models import Tea


def index(request):
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
    teas = Tea.objects.all()

    categories = {
        'Masala & Spiced': [
            'masala', 'chai', 'spice', 'spiced',
            'ginger', 'cardamom', 'cinnamon'
        ],

        'Green & Fresh': [
            'green', 'matcha', 'mint', 'fresh'
        ],

        'Herbal & Floral': [
            'herbal', 'flower', 'floral',
            'chamomile', 'lavender', 'rose'
        ],

        'Strong & Black': [
            'black', 'assam', 'darjeeling',
            'english breakfast', 'strong'
        ],
    }

    category_cards = []

    for category_name, keywords in categories.items():
        matched_teas = []

        for tea in teas:
            text = f"{tea.name} {tea.description}".lower()

            if any(keyword in text for keyword in keywords):
                matched_teas.append(tea)

        category_cards.append({
            'name': category_name,
            'teas': matched_teas,
            'count': len(matched_teas),
        })

    return render(request, 'categories.html', {
        'category_cards': category_cards,
        'total_teas': teas.count(),
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

def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(request, "register.html", {
                "error": "Passwords do not match."
            })

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already exists."
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect("index")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            messages.success(
                request,
                f"Login successful! Welcome back, {user.username}."
            )

            return redirect("index")

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def profile(request):
    return render(request, 'profile.html')