from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    # Admin URLs
    path('admin', views.admin, name="admin"),
    path('admin_login', views.admin_login, name="admin_login"),
    path('details', views.admin_dashboard, name="admin_dashboard"),  # Added name

    # Faculty URLs
    path('faculty', views.fac_login, name="faculty"),
    path('fac_login', views.fac_login, name="fac_login"),
    path('entry', views.fac_dashboard, name="fac_dashboard"),
    path('goback_facdash', views.goback_facdash, name="goback_facdash"),

    # Detail submission URLs
    path('detail_enter', views.detail_enter, name="detail_enter"),
    path('submit_details', views.detail_enter, name="submit_details"),

    path('sdp_submit_details', views.detail1_enter, name="sdp_submit_details"),
    path('detail1_enter', views.detail1_enter, name="detail1_enter"),

    path('it_detail_enter', views.it_detail_enter, name="it_detail_enter"),
    path('it_submit_details', views.it_detail_enter, name="it_submit_details"),

    # Filters
    path('handle_filters', views.handle_filters, name="handle_filters"),
    path('it_handle_filters', views.it_handle_filters, name="it_handle_filters"),
    path('handle1_filters', views.handle1_filters, name="handle1_filters"),

    # SDP Attended approvals
    path('approve_sdp_attended/<int:pk>/', views.approve_sdp_attended, name="approve_sdp_attended"),
    path('reject_sdp_attended/<int:pk>/', views.reject_sdp_attended, name="reject_sdp_attended"),

    # SDP Organised approvals
    path('approve_sdp_organised/<int:pk>/', views.approve_sdp_organised, name="approve_sdp_organised"),
    path('reject_sdp_organised/<int:pk>/', views.reject_sdp_organised, name="reject_sdp_organised"),

    # Invited Talk approvals
    path('approve_invited_talk/<int:pk>/', views.approve_invited_talk, name="approve_invited_talk"),
    path('reject_invited_talk/<int:pk>/', views.reject_invited_talk, name="reject_invited_talk"),
]
