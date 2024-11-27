from django.shortcuts import render, get_object_or_404, redirect

from .models import Card, Pokemon, Element, Expansion
from .forms import CardForm

# Create your views here.


#Card views
def card_list(request):
    cards = Card.objects.all()
    return render(request, 'PokeTCG/Card/card_list.html',{'cards':cards})

def card_detail(request, pk):
    card = get_object_or_404(Card,pk=pk)
    return render(request,'PokeTCG/Card/card_detail.html',{'card':card} )

def card_add(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
            elements = form.cleaned_data['element']
            card.element.set(elements) 

            return redirect('card_detail', pk=card.pk)
    else:
        form = CardForm()
    return render(request, 'PokeTCG/Card/card_edit.html', {'form': form})


def card_delete(request,pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method=='POST':
        card.delete()
        return redirect('card_list')
    return render(request, 'PokeTCG/Card/card_detail.html',{'card':card})

def card_edit(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            card = form.save(commit=False)  
            card.save() 
            form.save_m2m()
            return redirect('card_detail', pk=card.pk)
    else:
        form = CardForm(instance=card)
    return render(request, 'PokeTCG/Card/card_edit.html', {'form': form})



