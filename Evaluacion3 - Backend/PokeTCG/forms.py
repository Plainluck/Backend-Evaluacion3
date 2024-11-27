from django import forms 
from .models import Card, Pokemon, Expansion, Element
from datetime import date


#CARTAS#
class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('pokemon','element','HP','expansion')
    element = forms.ModelMultipleChoiceField(
        queryset=Element.objects.all(),
        widget= forms.CheckboxSelectMultiple())
    

    def clean_pokemon(self):
        pokemon = self.cleaned_data.get('pokemon')
        if not pokemon:
            raise forms.ValidationError("El campo Pokemon es obligatorio")
        return pokemon
    

    def clean_element(self):
        elements = self.cleaned_data.get('element')
        if not elements: 
            raise forms.ValidationError("Selecciona al menos un elemento para la carta")
        if elements.count() > 2:
            raise forms.ValidationError("La carta no puede tener más de 2 tipos")
        return elements

    def clean_HP(self):
        HP = self.cleaned_data.get('HP')
        if HP is None or HP < 10: 
            raise forms.ValidationError("La carta debe tener al menos 10 puntos de vida")
        if HP > 340:
            raise forms.ValidationError("La carta no puede superar a Skeledirge EX (340 HP)")
        if HP % 10 != 0: 
            raise forms.ValidationError("El HP debe ser multiplo de 10")
        return HP

    def clean_expansion(self):
        expansion = self.cleaned_data.get('expansion')
        if not expansion:
            raise forms.ValidationError("Debes agregar una expansion")
        if not Expansion.objects.filter(name=expansion.name).exists():
            raise forms.ValidationError("La expansion especificada no existe")
        return expansion


