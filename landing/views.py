from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Item


def item_list(request):
	items = Item.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'landing/item_list.html', {'items':items})

	