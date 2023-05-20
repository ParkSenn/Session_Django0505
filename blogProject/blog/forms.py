from .models import Post, Comment
from django import forms

class PostModelForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ['title', 'body', 'photo']


class CommentForm(forms.ModelForm): # 또다른 class로서 forms 안에 ModelForm을 상속받은 클래스를 하나 만들어줌
    class Meta: # Meta 클래스 하에, 어떤 모델을 기반으로 자동으로 form을 생성할 것인지 명시
        model = Comment 
        # 어떤 필드를 입력 받을지 써주기
        fields = ['comment']