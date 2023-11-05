from django.shortcuts import HttpResponse, render

# Create your views here.
# def member(request):
#   return HttpResponse("hello world!!!")

def contact(request):
  return render(request, 'contact.html')