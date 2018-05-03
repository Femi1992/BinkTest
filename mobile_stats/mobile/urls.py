from django.conf.urls import url
from . import views
from.views import stats_list

app_name = 'mobile'

urlpatterns = [
    #url(r'^$',views.StatsListView.as_view(), name='list'), list view not being used at the moment
    url(r'^create/$',views.CreateStatView.as_view(), name='create'),
    url(r'^$',views.stats_list, name='list'),
]