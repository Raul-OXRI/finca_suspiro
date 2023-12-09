from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
TEMPLATE_DIRS = (
    'es.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request, "mod_dashboard.html")
    