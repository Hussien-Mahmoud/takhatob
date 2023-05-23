from django import forms
from tinymce.widgets import TinyMCE

from users.models import Center
from centers.models import CenterReviews


class CenterEditForm(forms.ModelForm):

    class Meta:
        model = Center
        fields = ['username', 'image', 'excerpt', 'description', 'experience']
        widgets = {'description': TinyMCE(attrs={'cols': 80, 'rows': 30})}


class CenterAddReviewForm(forms.ModelForm):
    rate = forms.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = CenterReviews
        fields = ['rate', 'text']

