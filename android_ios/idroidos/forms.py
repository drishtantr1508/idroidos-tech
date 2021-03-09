from django import forms
from django.contrib.auth.models import User
from .models import (SmartphonesInfo,QuickLinks,ComparisonInfo,SmartphoneComment,ComparisonComment,NewsComment,NewsArticle,UserProfileInfo)

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
    class Meta():
        model=User
        fields=('username','email','password')
        widgets={
            'username':forms.TextInput(attrs={'class':"form-control",'placeholder':"Enter Your username..."}),
            'email':forms.EmailInput(attrs={'class':"form-control",'placeholder':'abc@example.com'}),
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('firstname','middlename','lastname','contact')
        widgets={
            'firstname':forms.TextInput(attrs={'class':"form-control",'placeholder':'Enter your first name...'}),
            'middlename':forms.TextInput(attrs={'class':"form-control",'placeholder':'Enter your middle name...'}),
            'lastname':forms.TextInput(attrs={'class':"form-control",'placeholder':'Enter your last name...'}),
            'contact':forms.TextInput(attrs={'class':"form-control",'placeholder':'Mobile no...'}),
        }

class QuickLinksForm(forms.ModelForm):
    class Meta():
        model=QuickLinks
        fields=('post',)
        widgets={
            'post':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),

        }

class SmartphonesInfoForm(forms.ModelForm):
    class Meta():
        model = SmartphonesInfo
        exclude=['published_date']
        widgets={
            'smartphone':forms.TextInput(attrs={'class':"form-control postcontent",'placeholder':'Type your text...'}),
            'title':forms.TextInput(attrs={'class':"form-control postcontent",'placeholder':'Type your text...'}),
            'intro':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'overview':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'display':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'design':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'performance':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'camera':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'battery':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'software':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'extras':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'conclusion':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            #'':forms.Textarea(attrs={'class':"form-control",'placeholder':''}),


        }

class SmartphoneCommentForm(forms.ModelForm):
    class Meta():
        model = SmartphoneComment
        fields=('author','text')
        widgets={
            'author':forms.TextInput(attrs={'class':'postcontent','placeholder':'Enter Your Username...'}),
            'text':forms.Textarea(attrs={'class':"editable medium-editor-textarea  postcontent"})
        }

class ComparisonInfoForm(forms.ModelForm):
    class Meta():
        model = ComparisonInfo
        exclude=['published_date']
        widgets={
            'smartphone_one':forms.TextInput(attrs={'class':"form-control postcontent",'placeholder':'Type your text...'}),
            'smartphone_two':forms.TextInput(attrs={'class':"form-control postcontent",'placeholder':'Type your text...'}),
            'title':forms.TextInput(attrs={'class':"form-control postcontent",'placeholder':'Type your text...'}),
            'intro':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'overview':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'display':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'design':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'performance':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'camera':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'battery':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'software':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'extras':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'conclusion':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),

        }

class ComparisonCommentForm(forms.ModelForm):
    class Meta():
        model = ComparisonComment
        fields=('author','text')
        widgets={
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username...'}),
            'text':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"})
        }

class NewsArticleForm(forms.ModelForm):
    class Meta():
        model = NewsArticle
        exclude=['published_date']
        widgets={
            'heading':forms.Textarea(attrs={'class':"form-control postcontent"}),
            'para1':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'para2':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'para3':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),
            'conclusion':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"}),

        }

class NewsCommentForm(forms.ModelForm):
    class Meta():
        model = NewsComment
        fields=('author','text')
        widgets={
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username...'}),
            'text':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"})
        }
