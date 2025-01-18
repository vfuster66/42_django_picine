from django.urls import path
from .views import (
    UserLoginView, PublicationsView,
    ArticleDetailView, UserLogoutView, FavouritesView,
    RegisterView, PublishArticleView, AddToFavouriteView
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('publications/', PublicationsView.as_view(), name='publications'),
    path(
        'article/<int:pk>/',
        ArticleDetailView.as_view(),
        name='article_detail'
    ),
    path('favourites/', FavouritesView.as_view(), name='favourites'),
    path('register/', RegisterView.as_view(), name='register'),
    path('publish/', PublishArticleView.as_view(), name='publish'),
    path(
        'article/<int:pk>/favourite/',
        AddToFavouriteView.as_view(),
        name='add_favourite'
    ),
]
