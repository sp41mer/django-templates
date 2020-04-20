"""djangotemplates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import school.views.fb_views as function_views
import school.views.cb_views as class_based_views

urlpatterns = [
    # Function based views
    path('fb_create_school/', function_views.create_school),
    path('fb_delete_school/<int:pk>/', function_views.delete_school),
    path('fb_update_school/<int:pk>/', function_views.edit_school),
    path('fb_show_school/<int:pk>/', function_views.show_school),
    path('fb_all_schools/', function_views.all_schools),

    # Class based views
    path('cb_create_school/', class_based_views.CreateSchoolView.as_view()),
    path('cb_all_template/', class_based_views.AllSchoolsTemplateView.as_view()),
    path('cb_detail/<int:pk>/', class_based_views.SchoolDetailView.as_view()),
    path('cb_create/', class_based_views.SchoolCreateView.as_view()),
    path('cb_list/', class_based_views.SchoolsListView.as_view()),

    path('admin/', admin.site.urls),
]
