from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Item


class ItemList(TemplateView):
    template_name = "item_list.html"

	# def item_list(request):
	# 	items = Item.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# 	return render(request, 'landing/item_list.html', {'items':items})

	