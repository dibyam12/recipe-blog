"""
URL configuration for chefsTable project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from vege.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sharedRecipes, name='sharedRecipes'),
    path('add/', addRecipes, name='addRecipes'),
    path('recipe/<int:recipe_id>/', recipeDetail, name='recipeDetail'),
    path('delete-recipe/<id>/', deleteRecipes, name='deleteRecipe'),
    path('update-recipe/<id>/', updateRecipe, name='updateRecipe'),
    path('share/<int:recipe_id>/', shareRecipe, name='shareRecipe'),
    path('login/', loginPage, name='loginPage'),
    path('register/', registerPage, name='registerPage'),
    path('logout/', logoutPage, name='logoutPage'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()