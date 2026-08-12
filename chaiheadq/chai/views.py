from django.shortcuts import render,redirect,get_object_or_404
from .forms import TeaForm
from .models import Tea


def _tea_categories():
    return [
        {
            'name': 'Masala & Spiced',
            'description': 'Bold, warm blends with ginger, cardamom, cinnamon, and other spices.',
            'keywords': ['masala', 'chai', 'spice', 'spiced', 'ginger', 'cardamom', 'cinnamon'],
        },
        {
            'name': 'Green & Fresh',
            'description': 'Fresh, grassy teas and lighter everyday brews.',
            'keywords': ['green', 'matcha', 'fresh', 'mint'],
        },
        {
            'name': 'Herbal & Floral',
            'description': 'Caffeine-free or botanical infusions with gentle aromatics.',
            'keywords': ['herbal', 'flower', 'floral', 'chamomile', 'lavender', 'rose'],
        },
        {
            'name': 'Strong & Black',
            'description': 'Robust teas with deeper flavor and a stronger finish.',
            'keywords': ['black', 'assam', 'darjeeling', 'english breakfast', 'strong'],
        },
    ]


def _build_category_cards(teas):
    cards = []

    for category in _tea_categories():
        matched_teas = []
        for tea in teas:
            searchable_text = f"{tea.name} {tea.description}".lower()
            if any(keyword in searchable_text for keyword in category['keywords']):
                matched_teas.append(tea)

        cards.append({
            'name': category['name'],
            'description': category['description'],
            'teas': matched_teas,
            'count': len(matched_teas),
        })

    return cards


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

def categories(request):
    teas = Tea.objects.all()
    category_cards = _build_category_cards(teas)
    return render(request, 'categories.html', {
        'category_cards': category_cards,
        'total_teas': teas.count(),
    })

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