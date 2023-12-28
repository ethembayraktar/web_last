from django.shortcuts import render
from sample.models import Sample

def index(request):
    
    context=dict()

    context['samples'] = Sample.objects.all()
    
    return render(request, 'index.html',context)
# Create your views here.

def product_detail(request, product_id):
    product = Sample.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


def search_results(request):
    query = request.GET.get('query', '')
    results = Sample.objects.filter(title1__icontains=query) | Sample.objects.filter(category__icontains=query)| Sample.objects.filter(price__icontains=query)| Sample.objects.filter(description__icontains=query)| Sample.objects.filter(id__icontains=query)| Sample.objects.filter(image__icontains=query)
    return render(request, 'search_results.html', {'query': query, 'results': results})