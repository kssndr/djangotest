from django.shortcuts import render


def item_list(request):
    return render(request, 'landing/item_list.html', {})
