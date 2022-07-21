from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('months/', views.months, name='months'),
    path('months_add/', views.MonthAddView.as_view(), name='Month-add'),
    path('months/update/<str:pk>',
         views.MonthUpdateView.as_view(), name='Month-Update'),
    path('months/delete/<str:pk>', views.MonthDelete.as_view(), name='Month-Del'),
    path('years/', views.yearView, name='years'),
    path('years/add', views.YearAddView.as_view(), name='years-add'),
    path('years/update/<str:pk>',
         views.YearUpdateView.as_view(), name='years-update'),
    path('years/delete/<str:pk>',
         views.YearDeleteView.as_view(), name='years-delete'),
    path('invests/', views.investView, name='invests')
]
