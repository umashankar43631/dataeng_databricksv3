from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def allRelatedLinks(request):
    return render(request, 'dataengbricksv3/managedeltalake/relatedurls.html')

# C:\Users\shankar\Desktop\Personal Website\templates\dataengbricksv3\managedeltalake\relatedurls.html

def deltalakeBasics(request):
    pass

def loadDataIntoDeltaLake(request):
    pass

def schemasTables(request):
    pass

def setupDeltaTable(request):
    pass

def versionAndOptimizeDeltaTables(request):
    pass

def sample(request):
    return HttpResponse("Hello World")