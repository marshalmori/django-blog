"""
URL configuration for djangocourse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import include, path

from app.views import (ArticleCreateView, ArticleDeleteView, ArticleListView,
                       ArticleUpdateView)

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('create/', ArticleCreateView.as_view(), name= 'create_article' ),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name= 'update_article' ),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name= 'delete_article' ),
]
