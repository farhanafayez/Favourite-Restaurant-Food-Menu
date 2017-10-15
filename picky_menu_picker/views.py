from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View 
from django.views.generic import TemplateView, ListView, DetailView

from .models import RestaurantLocation
from django.db.models import Q

def restaurant_listview(request):
    template_name = 'picky_menu_picker/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


class RestaurantListView(ListView):

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                    Q(category__iexact=slug) |
                    Q(category__icontains=slug) 
                )
        else:
            queryset = RestaurantLocation.objects.all()

        return queryset

class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()
    
    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get('rest_id')
        obj = get_object_or_404(RestaurantLocation, id=rest_id) # pk = rest_id
        return obj

































# ___Deprecated code___

# class SearchRestaurantListView(ListView):
    
#     template_name = 'picky_menu_picker/restaurants_list.html'
#     def get_queryset(self):
#         slug = self.kwargs.get("")
#         if slug:
#             queryset = RestaurantLocation.objects.filter(
#                     Q(category__iexact=slug) |
#                     Q(category__icontains=slug) 
#                 )
#         else:
#             queryset = RestaurantLocation.objects.none()

#         return queryset



# class ArabRestaurantListView(ListView):
#     queryset = RestaurantLocation.objects.filter(category__iexact='Arab')
#     template_name = 'picky_menu_picker/restaurants_list.html'


# class WesternRestaurantListView(ListView):
#     queryset = RestaurantLocation.objects.filter(category__iexact='Western')
#     template_name = 'picky_menu_picker/restaurants_list.html'

# class PortugueseRestaurantListView(ListView):
#     queryset = RestaurantLocation.objects.filter(category__iexact='Portuguese')
#     template_name = 'picky_menu_picker/restaurants_list.html'



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













