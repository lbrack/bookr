""" A view gets a request from a client through an HttpRequest
    processes it and returns an HttpResponse.

"""
from django.shortcuts import render  # Renders the template
from django.http import HttpResponse
from .models import Book


def average_rating(rating_list):
    if not rating_list:
        return 0

    return round(sum(rating_list) / len(rating_list))


def welcome(request):
    """Gets the name from http://localhost:8001
    renders it in the template ``base.html`` located in the ``templates`` directory
    at the same level as views (this is a default location expected by Django)

    :param request:
    :return:
    """

    page = render(request, "base.html", dict(total_books=Book.objects.count()))
    return page


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(
        request,
        template_name="reviews/search-results.html",
        context={"search_text": search_text},
    )


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append(
            {
                "book": book,
                "book_rating": book_rating,
                "number_of_reviews": number_of_reviews,
            }
        )

    context = {"book_list": book_list}
    return render(request, "reviews/book-list.html", context)


def dash_proto(request):
    return render(request, "reviews/dash-proto.html")
