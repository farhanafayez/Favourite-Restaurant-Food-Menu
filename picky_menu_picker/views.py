from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 
from django.views.generic import TemplateView

from .models import RestaurantLocation

def restaurant_listview(request):
    template_name = 'picky_menu_picker/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


































# ___Deprecated code___
# import random

# class HomeView(TemplateView):
#     template_name = "home.html"

#     def get_context_data(self, *args, **kwargs):
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#         num = 0
#         some_list = [
#             random.randint(0,10000000),
#             random.randint(0,10000000),
#             random.randint(0,10000000)
#         ]
#         condition_bool_item = True
#         if condition_bool_item:
#             num = random.randint(0,10000000)
#         context = {'num': num,
#                    'some_list': some_list
#         }
#         return context


# class AboutView(TemplateView):
   
#     template_name = "about.html"

# class ContactView(TemplateView):
   
#     template_name = "contact.html"

# Create your views here.
#
# def old_home(request):
#     html_var = 'f strings'
#     num = random.randint(0, 10000000)
#     html_ = f"""<!DOCTYPE HTML>
#     <html lang=en>
#     <head>
#     </head>
#     <body>
#     <h1>Hello Fellas</h1>
#     <p>here comes{ html_var }</p>
#     <p>here comes{ num }</p>
#     </body>
#     </html>
#     """
#     return HttpResponse(html_)

# def home(request):
#     num = 0
#     some_list = [
#         random.randint(0,10000000),
#         random.randint(0,10000000),
#         random.randint(0,10000000)
#     ]
#     condition_bool_item = False
#     if condition_bool_item:
#         num = random.randint(0,10000000)
#     context = {'num': num,
#                'some_list': some_list
#     }
#     # return render(request, "base.html", {html_var:True, 'num':num})
#     return render(request, "home.html", context)

# def about(request):
  
#     context = {
#     }
#     # return render(request, "base.html", {html_var:True, 'num':num})
#     return render(request, "about.html", context)

# def contact(request):
    
#     context = {
#     }
#     # return render(request, "base.html", {html_var:True, 'num':num})
#     return render(request, "contact.html", context)


# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
   
#         return render(request, "contact.html", context)

    # def put(self, request, *args, **kwargs):
    #     context = {}
   
    #     return render(request, "contact.html", context)

    # def post(self, request, *args, **kwargs):
    #     context = {}
   
    #     return render(request, "contact.html", context)













