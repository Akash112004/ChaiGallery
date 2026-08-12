from django.shortcuts import render


def home(request):
    skills_groups = [
        {
            'title': 'Backend',
            'icon': '⚙️',
            'skills': ['Django', 'Python', 'PostgreSQL', 'SQLite', 'Authentication'],
        },
        {
            'title': 'Systems',
            'icon': '🖥️',
            'skills': ['Linux', 'Git & GitHub', 'DevOps learning', 'Deployment basics', 'CLI workflows'],
        },
        {
            'title': 'Frontend',
            'icon': '✨',
            'skills': ['HTML5', 'CSS3', 'JavaScript', 'Tailwind CSS', 'Responsive design'],
        },
    ]

    contact_links = [
        {
            'label': 'Email',
            'value': 'solankiakash7016@gmail.com',
            'href': 'mailto:solankiakash7016@gmail.com',
            'icon': '✉',
        },
        {
            'label': 'LinkedIn',
            'value': 'linkedin.com/in/akash-solanki-21518a282',
            'href': 'https://www.linkedin.com/in/akash-solanki-21518a282/',
            'icon': 'in',
        },
        {
            'label': 'GitHub',
            'value': 'github.com/Akash112004',
            'href': 'https://github.com/Akash112004',
            'icon': 'gh',
        },
    ]

    featured_project = {
        'title': 'ChaiGallery',
        'type': 'Django Web Application',
        'description': (
            'A modern tea gallery platform where users can upload tea photos, add descriptions, browse '
            'a community gallery, edit tea entries, and explore teas through a responsive Django + Tailwind interface.'
        ),
        'tech_stack': ['Django', 'Python', 'Tailwind CSS', 'PostgreSQL / SQLite', 'HTML5', 'CSS3'],
        'github': 'https://github.com/Akash112004',
    }

    return render(request, 'portfolio/home.html', {
        'skills_groups': skills_groups,
        'contact_links': contact_links,
        'featured_project': featured_project,
    })