from django import forms
from app.models import Class


class addClassForm(forms.ModelForm):
    class Meta:
        model = Class  # 사용할 모델
        fields = ['classname']  # QuestionForm에서 사용할 Question 모델의 속성

        labels={
            'classname' : '수업이름',
        }
        
