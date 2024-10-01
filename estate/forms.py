from django import forms
from .models import Form ,Comment
from django .forms import TextInput,Textarea,Select, FileInput
class Detailsform(forms.ModelForm):
    class Meta:
        model=Form
        fields=['name','address', 'phone','property_type','district','locality','condition']
        widgets={
            'name':TextInput(
                attrs={
                    "name":"name",
                    "class":"form-control", 
                    "placeholder":"Name"
                }
            ),
            'phone':TextInput(
                attrs={
                    "name":"phone",
                    "class":"form-control",  
                    "placeholder":"phone number"
                }
            ),
            'address':Textarea(
                attrs={
                    "name":"address",
                    "class":"form-control",
                    "placeholder":"your address"
                }
            ),
            'condition':Textarea(
                attrs={
                    "name":"condition",
                    "class":"form-control",  
                    "placeholder":"write your conditions"
                }
            ),
            'property_type':Select(
                attrs={
                    "name":"property_type",
                    "class":"form-control", 
                    "placeholder":"property type"
                }
            ),
            'district':TextInput(
                attrs={
                    "name":"district",
                    "class":"form-control",  
                    "placeholder":"district"
                }
            ),
            'locality':TextInput(
                attrs={
                     "name":"locality",
                    "class":"form-control",  
                    "placeholder":"locality"
                }
            )
        }
class Commentform(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['client_name','profession','comment','image']
        widgets={
            'client_name':TextInput(
                attrs={
                    "type":"text",
                    "class":"form-control",  
                    "placeholder":"write your name"
                }
            ),
            'profession':TextInput(
                attrs={
                    "type":"text",
                    "class":"form-control",
                    "placeholder":"write your profession"
                }
            ),
            'image':FileInput(
                attrs={
                    "type":"file",
                    "class":"form-control",
                    "placeholder":"write your profession"
                }
            ),
            'comment':Textarea(
                attrs={
                    "type":"text",
                    "class":"form-control",
                    "placeholder":"write your feedback"
                }
            ),
        }
