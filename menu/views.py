from django.shortcuts import render

def indexView(request):
    title="Nazi"
    return render(request, 'menu/index.html', {"title":title})
