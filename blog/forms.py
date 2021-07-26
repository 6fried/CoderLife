from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'placeholder':'Enter your Name', 'class':'form-control'}
        self.fields['email'].widget.attrs = {'placeholder':'Enter your Email', 'class':'form-control'}
        self.fields['body'].widget.attrs = {'placeholder':'Comment here...', 'class':'form-control', 'rows':'5'}

c = CommentForm().as_p()