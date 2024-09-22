from django import forms
from .models import Blog

class CommentsForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full name'
                           ,widget=forms.TextInput(attrs={'class': 'form-control',
                            'placeholder': 'Enter your full name'}))
    
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                            'placeholder': 'Enter your email'}))
    
    comments = forms.CharField(label='Comments',
                             widget=forms.Textarea(attrs={'class': 'form-control',
                            'placeholder': 'Enter your comments'}))

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full name'
                           ,widget=forms.TextInput(attrs={'class': 'form-control',
                            'placeholder': 'Enter your full name'}))
    
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                            'placeholder': 'Enter your email'}))
    
    comments = forms.CharField(label='Comments',
                             widget=forms.Textarea(attrs={'class': 'form-control',
                            'placeholder': 'Enter your email'}))
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 5 :
            raise forms.ValidationError('Name must be at least 5 characters long')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "@gmail.com" not in email:
            raise forms.ValidationError("Invalid email domain. Only example.com emails are allowed.")
        
    def clean_comments(self):
        comments = self.cleaned_data.get('comments')
        if len(comments) < 10 :
            raise forms.ValidationError('Comments must be at least 10 characters long')

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'