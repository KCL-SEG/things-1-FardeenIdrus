from django.shortcuts import render


def things_view(request):
    return render(request, 'things_page.html')


