import json
#from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer
from products.models import Product

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    
    #if request.method != "GET":
        #return Response({"detail": "POST not allowed"}, status=405)
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        #data = model_to_dict(model_data, fields=['id','title','price', 'sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)
