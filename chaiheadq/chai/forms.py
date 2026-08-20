from django import forms
from .models import Tea


class TeaForm(forms.ModelForm):

    class Meta:
        model = Tea
        fields = ['name', 'description', 'image']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': (
                    'w-full px-4 py-3 rounded-xl '
                    'border border-gray-300 dark:border-gray-700 '
                    'bg-white dark:bg-gray-800 '
                    'text-gray-900 dark:text-white '
                    'focus:outline-none focus:ring-2 '
                    'focus:ring-amber-500'
                ),
                'placeholder': 'e.g. Masala Chai',
            }),

            'description': forms.Textarea(attrs={
                'class': (
                    'w-full px-4 py-3 rounded-xl '
                    'border border-gray-300 dark:border-gray-700 '
                    'bg-white dark:bg-gray-800 '
                    'text-gray-900 dark:text-white '
                    'focus:outline-none focus:ring-2 '
                    'focus:ring-amber-500'
                ),
                'placeholder': 'Tell us about this tea...',
                'rows': 5,
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': (
                    'w-full px-4 py-3 rounded-xl '
                    'border border-gray-300 dark:border-gray-700 '
                    'bg-white dark:bg-gray-800 '
                    'text-gray-700 dark:text-gray-300'
                ),
            }),
        }