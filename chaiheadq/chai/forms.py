from django import forms
from .models import Tea


class TeaForm(forms.ModelForm):
    class Meta:
        model = Tea
        fields = ['name', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-gray-300 bg-white text-gray-900 placeholder-gray-500 p-3 focus:ring-2 focus:ring-chai-500 focus:border-chai-500 dark:bg-gray-800 dark:border-gray-700 dark:text-white dark:placeholder-gray-400',
                'placeholder': 'Enter Tea Name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full rounded-lg border border-gray-300 bg-white text-gray-900 placeholder-gray-500 p-3 h-32 resize-none focus:ring-2 focus:ring-chai-500 focus:border-chai-500 dark:bg-gray-800 dark:border-gray-700 dark:text-white dark:placeholder-gray-400',
                'placeholder': 'Write a short description about the tea...'
            }),
        }