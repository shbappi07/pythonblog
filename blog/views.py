from django.shortcuts import render

# Create your views here.
def home_view(request):
    contex = {}
    return render(request, "blog/index.html", contex)