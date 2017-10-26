from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views


app_name = 'condet'
urlpatterns = [
    url(r'^accounts/login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^degree/$', views.DashboardDegreeView.as_view(), name='index-dashboard-degree'),
    url(r'^api/chart/data/$', views.ChartData.as_view(), name='api-data'),
    url(r'^api/chart/data/degree/$', views.ChartDataDegree.as_view(), name='api-data-degree'),
    url(r'^researcher/(?P<pk>[0-9]+)/$', views.ResearcherView.as_view(), name='researcher_detail'),
    url(r'^researcher/$', views.ResearcherList.as_view(), name='researcher_list'),
    url(r'^researcher/add/$', views.ResearcherCreate.as_view(), name='researcher_create'),
    url(r'^researcher/(?P<pk>[0-9]+)/edit/$', views.ResearcherUpdate.as_view(), name='researcher_update'),
    url(r'^researcher/(?P<pk>[0-9]+)/delete/$', views.ResearcherDelete.as_view(), name='researcher_delete'),
    url(r'^researcher/(?P<researcher_id>[0-9]+)/courses/$', views.researcher_courses, name='researcher_courses'),
    url(r'^university/$', views.UniversityList.as_view(), name='university_list'),
    url(r'^university/add/$', views.UniversityCreate.as_view(), name='university_create'),
    url(r'^university/(?P<pk>[0-9]+)/$', views.UniversityDetail.as_view(), name='university_detail'),
    url(r'^university/(?P<pk>[0-9]+)/edit/$', views.UniversityUpdate.as_view(), name='university_update'),
    url(r'^university/(?P<pk>[0-9]+)/delete/$', views.UniversityDelete.as_view(), name='university_delete'),
    url(r'^course/$', views.CourseView.as_view(), name='course_list'),
    url(r'^course/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view(), name='course_detail'),
    url(r'^degree/(?P<pk>[0-9]+)/$', views.DegreeDetail.as_view(), name='degree_detail'),
    url(r'^degree/$', views.DegreeList.as_view(), name='degree_list'),
    url(r'^degree/add/$', views.DegreeCreate.as_view(), name='degree_create'),
    url(r'^degree/(?P<pk>[0-9]+)/edit/$', views.DegreeUpdate.as_view(), name='degree_update'),
    url(r'^degree/(?P<pk>[0-9]+)/delete/$', views.DegreeDelete.as_view(), name='degree_delete'),
    url(r'^posdegree/(?P<pk>[0-9]+)/$', views.PosDegreeDetail.as_view(), name='posdegree_detail'),
    url(r'^posdegree/$', views.PosDegreeList.as_view(), name='posdegree_list'),
    url(r'^posdegree/add/$', views.PosDegreeCreate.as_view(), name='posdegree_create'),
    url(r'^posdegree/(?P<pk>[0-9]+)/edit/$', views.PosDegreeUpdate.as_view(), name='posdegree_update'),
    url(r'^posdegree/(?P<pk>[0-9]+)/delete/$', views.PosDegreeDelete.as_view(), name='posdegree_delete'),
]
