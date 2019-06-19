from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^books+$', views.books),
    url(r'^authors+$', views.authors),
    url(r'^books/(?P<b_id>\d+)$', views.show_book),
    url(r'^authors/(?P<a_id>\d+)$', views.show_author),
    url(r'^books/add+$', views.add_book),
    url(r'^authors/add+$', views.add_author),
    url(r'^authors/add_book+$', views.auth_add_book),
    url(r'^books/add_author+$', views.book_add_auth)



]