
from django.contrib import admin
from django.urls import path,re_path,include
from ego import views  # Переименуйте 'ego' на имя вашего приложения, если оно отличается
from . import views
from django.views.generic import TemplateView

egoistnews =  [
    path('<int:id>/news',views.news), 
    path('<int:id>/newsbluelock',views.newsbluelock),
    path('<int:id>/newsneoego',views.newsneoego),
    path('personality/',views.personality)
]
redirection = [
    path('fake/', views.fake, name='fake'),
    path('json/', views.json, name='json'),
    path('set-cookie/', views.set_cookie, name='set_cookie'),
    path('get-cookie/', views.get_cookie, name='get_cookie'),

]


adminka = [
    path('', views.index, name="index"),
    path('tasks/<int:task_id>/', views.view_task, name='view_task'),
    path('tasks/new/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
]



urlpatterns = [
    re_path('about/', views.about),
    re_path('index1/', views.index1),
    re_path('name/', views.name,kwargs={"name": "ISAGI YOICHI"}),
    path('user/<str:username>/',views.user), 
    path('home/',views.home),
    path('new/', include(egoistnews)),
    path('redirection/', include(redirection)),
    path('adminka/', include(adminka)),
    path(
        'contact/', 
        TemplateView.as_view(
            template_name='contact.html', # Указываем, какой html-файл открыть
            extra_context={'phone': '+7 (777) 999-88-77'} # Передаем данные прямо здесь
        ), 
        name='contact'
    ),
    path('give/', views.give)
]
