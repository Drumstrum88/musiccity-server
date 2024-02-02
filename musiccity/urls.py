"""
URL configuration for musiccity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from musiccityapi.views import check_user, register_user
from django.urls import include, path
from rest_framework import routers
from musiccityapi.views.post_reaction_views import PostReactionView

from musiccityapi.views.post_view import PostView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'posts', PostView, 'post')
router.register(r'post_reactions', PostReactionView, 'post_reaction')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkuser', check_user),
    path('registeruser', register_user),
    path('', include(router.urls)),

]
