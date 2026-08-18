from django import forms
from .models import Tea


class TeaForm(forms.ModelForm):
    class Meta:
        model = Tea
        fields = [ 'user', 'name','description', 'image']
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        tea = super().save(commit=False)
        if self.user is not None:
            tea.user = self.user
        if commit:
            tea.save()
        return tea