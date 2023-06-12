from django import forms
from tinymce.widgets import TinyMCE

from users.models import Specialist
from specialists.models import SpecialistReviews


class SpecialistEditForm(forms.ModelForm):

    class Meta:
        model = Specialist
        fields = ['first_name', 'last_name', 'image', 'excerpt', 'description', 'experience']
        widgets = {'description': TinyMCE(attrs={'cols': 80, 'rows': 30})}


class SpecialistAddReviewForm(forms.ModelForm):
    rate = forms.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = SpecialistReviews
        fields = ['rate', 'text']
