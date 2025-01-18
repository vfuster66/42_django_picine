from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Article, UserFavouriteArticle
from .forms import ArticleForm, FavouriteForm
from django.shortcuts import redirect
import logging
from django.http import HttpResponseBadRequest

logger = logging.getLogger(__name__)

class ArticleListView(ListView):
   model = Article
   template_name = 'articles/article_list.html'
   context_object_name = 'articles'

class UserLoginView(LoginView):
   template_name = 'articles/login.html'

   def form_valid(self, form):
       logger.error(f"Form valid called with POST data: {self.request.POST}")
       logger.error(f"Next URL: {self.request.POST.get('next')}")
       logger.error(f"Current path: {self.request.path}")
       
       # Log in the user
       login(self.request, form.get_user())
       logger.error(f"User {form.get_user().username} logged in successfully")

       # Get the next URL
       next_url = self.request.POST.get('next')
       if next_url:
           logger.error(f"Redirecting to next URL: {next_url}")
           return redirect(next_url)
           
       logger.error("No next URL found, redirecting to article_list")
       return redirect('article_list')

   def form_invalid(self, form):
       logger.error(f"Login form invalid - Errors: {form.errors}")
       logger.error(f"POST data: {self.request.POST}")
       return super().form_invalid(form)

   def get(self, request, *args, **kwargs):
       logger.error(f"GET request to login view from: {request.META.get('HTTP_REFERER', 'unknown')}")
       return super().get(request, *args, **kwargs)

class PublicationsView(LoginRequiredMixin, ListView):
   model = Article
   template_name = 'articles/publications.html'
   context_object_name = 'articles'
   login_url = reverse_lazy('login')

   def get_queryset(self):
       return Article.objects.filter(author=self.request.user)

class ArticleDetailView(LoginRequiredMixin, DetailView):
   model = Article
   template_name = 'articles/article_detail.html'
   context_object_name = 'article'
   login_url = reverse_lazy('login')

class UserLogoutView(LogoutView):
   next_page = reverse_lazy('home')

   def dispatch(self, request, *args, **kwargs):
       logger.error(f"Logout request for user: {request.user}")
       response = super().dispatch(request, *args, **kwargs)
       logger.error("User logged out successfully")
       return response

class FavouritesView(LoginRequiredMixin, ListView):
   model = UserFavouriteArticle
   template_name = 'articles/favourites.html'
   context_object_name = 'favourites'
   login_url = reverse_lazy('login')

   def get_queryset(self):
       return UserFavouriteArticle.objects.filter(user=self.request.user)

class RegisterView(CreateView):
   form_class = UserCreationForm
   template_name = 'articles/register.html'
   success_url = reverse_lazy('login')

   def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('article_list')
        return super().dispatch(request, *args, **kwargs)

   def form_valid(self, form):
       logger.error(f"Registration form valid for user: {form.cleaned_data.get('username')}")
       response = super().form_valid(form)
       logger.error("User registered successfully")
       return response

   def form_invalid(self, form):
       logger.error(f"Registration form invalid - Errors: {form.errors}")
       return super().form_invalid(form)

class PublishArticleView(LoginRequiredMixin, CreateView):
   model = Article
   form_class = ArticleForm
   template_name = 'articles/publish.html'
   success_url = reverse_lazy('publications')

   def form_valid(self, form):
       form.instance.author = self.request.user
       logger.error(f"Publishing article: {form.cleaned_data.get('title')} by {self.request.user}")
       return super().form_valid(form)

class AddToFavouriteView(LoginRequiredMixin, CreateView):
   model = UserFavouriteArticle
   form_class = FavouriteForm
   template_name = 'articles/add_favourite.html'
   success_url = reverse_lazy('favourites')

   def form_valid(self, form):
       form.instance.user = self.request.user
       form.instance.article_id = self.kwargs['pk']
       # Vérifier si l'article est déjà en favoris
       if UserFavouriteArticle.objects.filter(
           user=self.request.user,
           article_id=self.kwargs['pk']
       ).exists():
           return HttpResponseBadRequest("Article déjà en favoris")
       logger.error(f"Adding article {self.kwargs['pk']} to favourites for user {self.request.user}")
       return super().form_valid(form)