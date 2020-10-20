from django.urls import path

from Events.models import News,Category
from home import views

cats = Category.objects.values_list('slug')
urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contact', views.contact, name='contact'),
    path('references', views.references, name='references'),

    path('category/', views.all_cat, name='categorys'),
    path('category/<int:id>/<slug:slug>', views.cat_news, name='category'),

    path('addcomment/<int:id>', views.add_Comment, name='addcomment'),


    path('detail/<slug:slug>/<int:id>', views.detail, name='detail'),

    path('search_auto/', views.newsSrch_auto, name='search_auto'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),

    path('signup/', views.sginup_view, name='sginup_view'),
]