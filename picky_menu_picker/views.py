from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation

@login_required(login_url = "/login/")
def restaurant_createview(request):
    form = RestaurantCreateForm(request.POST or None)
    errors = None
    # if request.method == 'POST':

        # title = request.POST.get("title")
        # location = request.POST.get("location")
        # category = request.POST.get("category")
        # form = RestaurantCreateForm(request.POST)
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit = False)
            instance.owner = request.user
            instance.save()

        # obj = RestaurantLocation.objects.create(
        #     name = form.cleaned_data.get('name'),
        #     location = form.cleaned_data.get('location'),
        #     category = form.cleaned_data.get('category'),

        # )
            return HttpResponseRedirect("/restaurants/")
        else:
            return HttpResponseRedirect("/login/") #not best practice

    if form.errors:
        errors = form.errors

    template_name = 'picky_menu_picker/form.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "form" : form,
        "errors" : errors,
    }
    return render(request, template_name, context)

def restaurant_listview(request):
    template_name = 'picky_menu_picker/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

def restaurant_detailview(request, slug):
    template_name = 'picky_menu_picker/restaurantlocation_detail.html'
    obj = RestaurantLocation.objects.get(slug=slug)
    context = {
        "object": obj
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
    queryset = RestaurantLocation.objects.all() #filter(category__iexact= 'Arab')
    
    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id) # pk = rest_id
    #     return obj


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'picky_menu_picker/form.html'
    success_url = "/restaurants/"
    login_url = "/login/" # this can be over ridden here in the views, as login url is defined in base settinsg

    def form_valid(self,form):
        instance = form.save(commit = False)
        instance.owner = self.request.user
        instance.save() # removing this worl work as well, does it for default
        return super(RestaurantCreateView, self).form_valid(form)


    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context




























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













