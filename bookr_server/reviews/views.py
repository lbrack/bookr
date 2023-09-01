""" A view gets a request from a client through an HttpRequest
    processes it and returns an HttpResponse.

"""
from django.shortcuts import render  # Renders the template
from django.http import HttpResponse


def index(request):
    """Gets the name from http://localhost:8001?name=bob
    renders it in the template ``base.html`` located in the ``templates`` directory
    at the same level as views (this is a default location expected by Django)

    :param request:
    :return:
    """
    name = request.GET.get("name") or "Andrzej"
    page = render(request, "base.html", dict(name=name))
    return page


# The is the original form of the view without a template.
# def index(request):
#     name = request.GET.get("name") or "Andrzej"
#     return HttpResponse(f"Hello {name}!")
