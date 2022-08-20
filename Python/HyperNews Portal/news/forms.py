from django import forms


class AddNewsPost(forms.Form):
    title = forms.CharField(max_length=255, label='title')
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='text')


class SearchNews(forms.Form):
    q = forms.CharField(label='q')
