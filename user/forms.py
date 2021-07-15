from django import forms
from .models import PostModel

class PostForm(forms.ModelForm):
	class Meta:
		model = PostModel
		fields = ['text']

		widgets={'text':forms.Textarea(attrs={'placeholder':'Enter Text',
						'style':"resize:none",
						'rows':3,
						'cols':20,
						'required':True,
						'autofocus':True
				})}

		labels= {"text":""}


class UpdatePost(forms.Form):
	id = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter id"}),label="")
	text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter Text',
						'style':"resize:none",
						'rows':3,
						'cols':22,
						'required':True}),label="")
	
		