from django.shortcuts import render, redirect
from django.views.generic import View
from store_app.models import Manufacturers, Products
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'products': Products.objects.all(),
        'manufacturers': Manufacturers.objects.all().order_by('name'),
    }
    return render(request, 'index.html', context)

class ProductsView(View):
    def get(self, request, pk):
        context = {
            'product': Products.objects.get(id=pk),
            'manufacturers': Manufacturers.objects.all().order_by('name'),
        }
        return render (request, 'product.html', context)
    
    def post(self, request, pk):
        errors = Products.objects.prod_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect (f"/products/{pk}")
        else:
            prod1 = Products.objects.get(id=pk)
            prod1.name = request.POST['name']
            prod1.price = request.POST['price']
            prod1.description = request.POST['description']
            prod1.manufacturer =Manufacturers.objects.get(id=request.POST['manufacturer'])
            prod1.save()
            messages.success(request,"Product was updated.")
            return redirect(f'/products/{pk}')   
        
    def delete(self, request, pk):
        Products.objects.get(id=pk).delete()
        return redirect('/')
    
class ProductCreateView(ProductsView):
    def post(self, request):
        errors = Products.objects.prod_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect ("/")
        else:
            Products.objects.create(name=request.POST['name'], price=request.POST['price'], description=request.POST['description'], manufacturer=Manufacturers.objects.get(id=request.POST['manufacturer']))
            messages.success(request, "New Product was added!")
            return redirect('/')
    

class ManufacturersView(View):
    
    def post(self, request):
        errors = Manufacturers.objects.mfg_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect ("/")
        else:
            mfg1 = Manufacturers.objects.create(name=request.POST['name'])
            
            print(mfg1)
            return redirect('/')
        