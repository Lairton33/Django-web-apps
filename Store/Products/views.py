from django.shortcuts import redirect, render
from .models import Product

def get_fields(obj):
    return (obj['name'], obj['price'], obj['description'])

class Views:

    def main_page(request):
        products = Product.objects.all()[::-1]
        return render(request, "templates/home.html", {"products": products})
    
    def add_product(request):
        if request.method == "POST":
            name, price, description = get_fields(request.POST)
            Product.objects.create(image_path=None, name=name, price=price, description=description)
            return redirect('main-page')
        
        return render(request, 'templates/add_product.html')
    
    
    def update_product(request, id):
        product = Product.objects.filter(id=id)[0]
        if request.method == 'POST':
            name, price, description = get_fields(request.POST)
            Product.objects.filter(id=id).update(name=name, price=price, description=description)
            return redirect('main-page')
        return render(request, 'templates/update_product.html', {'product': product})

    def delete_product(request, id):
        Product.objects.filter(id=id).delete()
        return redirect('main-page')
