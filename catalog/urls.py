from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                    # name parameter is a name of this url mapping and can be used in template to create a link to this page("").
    path('oneshot/', views.oneshot, name='oneshot'), 

    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    # All borrowed view got 2 ways to maps, from file: base_beneric.html
        # if use {% if user.is_staff %}                         it reverse url to mapping name "all-borrowed1" and then use view "AllLoanedBooksListView1".
        # if use {% if perms.catalog.can_mark_returned %}       it reverse url to mapping name "all-borrowed2" and then use view "AllLoanedBooksListView2".
    path('allborrowed1/', views.AllLoanedBooksListView1.as_view(), name='all-borrowed1'),
    path('allborrowed2/', views.AllLoanedBooksListView2.as_view(), name='all-borrowed2'),    

    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),

    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
]
