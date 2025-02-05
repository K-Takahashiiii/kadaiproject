from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(Article, self).__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Article
        fields = ['title', 'content']

# ArticleFormSet = forms.modelformset_factory(
#     Article, form = ArticleForm, extra=3
# )