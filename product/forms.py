from django import forms
from .models import Product
    
class AddProductForm(forms.ModelForm) :
    class Meta :
        model = Product
        fields = ['catagory', 'name', 'details', 'price', 'discount', 'image',]
        labels = {
            'image' : ('Main Image'),
        }
        help_texts = {
            'discount': "provide in '%' or can be empty",
        }

class AddProductFullForm(AddProductForm) :
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    
    class Meta(AddProductForm.Meta):
        fields = AddProductForm.Meta.fields + ['images',]