from django.shortcuts import render
from django.http import HttpResponse
import random

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

def home(request):
    num = 0
    some_list = [
        random.randint(0,10000000),
        random.randint(0,10000000),
        random.randint(0,10000000)
    ]
    condition_bool_item = False
    if condition_bool_item:
        num = random.randint(0,10000000)
    context = {'num': num,
               'some_list': some_list
    }
    # return render(request, "base.html", {html_var:True, 'num':num})
    return render(request, "home.html", context)

def home2(request):
    num = 0
    some_list = [
        random.randint(0,10000000),
        random.randint(0,10000000),
        random.randint(0,10000000)
    ]
    condition_bool_item = False
    if condition_bool_item:
        num = random.randint(0,10000000)
    context = {'num': num,
               'some_list': some_list
    }
    # return render(request, "base.html", {html_var:True, 'num':num})
    return render(request, "home2.html", context)

def home3(request):
    num = 0
    some_list = [
        random.randint(0,10000000),
        random.randint(0,10000000),
        random.randint(0,10000000)
    ]
    condition_bool_item = False
    if condition_bool_item:
        num = random.randint(0,10000000)
    context = {'num': num,
               'some_list': some_list
    }
    # return render(request, "base.html", {html_var:True, 'num':num})
    return render(request, "home3.html", context)