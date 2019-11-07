from django.conf.urls import url
from . import views

urlpatterns = [
    # Books Section
    url(r'^$', views.index),
    url(r'^add_book$', views.add_book),
    url(r'^books/(?P<book_id>\d+)$', views.book_profile),
    url(r'^add_author/(?P<book_id>\d+)$', views.add_author),
    # Authors section
    url(r'^author$', views.authors_summary),
    url(r'^author/add_author_summary$', views.add_author_summary),
    url(r'^author/(?P<author_id>\d+)$', views.author_profile),
    url(r'^add_book/(?P<author_id>\d+)$', views.add_book_to_author),
]