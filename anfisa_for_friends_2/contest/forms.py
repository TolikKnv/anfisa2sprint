from django import forms

class ContestForm(forms.Form):
    title = forms.CharField(label='Название', max_length=20)
    description = forms.CharField(
        label='Описание', widget=forms.Textarea()
    )
    price = forms.IntegerField(
        label='Цена',
        help_text='Рекомендованная розничная цена',
        min_value=10,
        max_value=100,
    )
    comment = forms.CharField(
        label='Комментарий', required=False, widget=forms.Textarea(attrs={'rows':3, 'cols':30})
    )