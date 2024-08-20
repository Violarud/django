from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = { 
            "title": TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Name'
            }),

            "anons": TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Description'
            }),

            "full_text": Textarea(attrs= {
                'class': 'form-control',
                'placeholder': 'Content of the article'
            }),

            "date": DateTimeInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Date of publication'
            }),

        }               
    