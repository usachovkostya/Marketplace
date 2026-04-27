from django.shortcuts import render, redirect
from .models import Marketplace
from .forms import MarketplaceForm
from django.utils import timezone
def index(request):

    declares = Marketplace.objects.all()
    return render(request, 'web_app/index.html', {'declares': declares })

def add_post(request):

    if request.method == "POST":
        form = MarketplaceForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()  
            return redirect('index') 
    else:
        form = MarketplaceForm()

    return render(request, 'web_app/add_post.html', {'form': form})