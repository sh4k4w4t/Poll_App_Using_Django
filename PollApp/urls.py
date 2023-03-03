from django.contrib import admin
from django.urls import path
from polls import views as pollsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",pollsViews.home,name='home'),
    path("create/",pollsViews.create,name='create'),
    path("vote/<poll_id>",pollsViews.vote,name='vote'),
    path("results/<poll_id>",pollsViews.results,name='results'),
]