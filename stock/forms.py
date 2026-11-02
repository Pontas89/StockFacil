from django import forms
from stock.models import Person  # troque courses pelo nome do seu app


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            "first_name",
            "last_name"
        ]