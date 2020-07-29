from django import forms
from .models import Blogapp

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blogapp 
        fields = ['title','body','image'] 


    def __init__(self,*args,**kwargs): 
        super().__init__(*args,**kwargs)
        self.fields['title'].label="제목"
        self.fields['body'].label="본문"
        self.fields['title'].widget.attrs.update({
            'class' : 'title_class',
            'placeholder':'제목을 입력하세요',
        })