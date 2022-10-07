from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('list/' , views.viewquestion , name='viewquestion'),
    path('detail/<int:id>',views.detailview, name='detailview'),
    path('' , views.index , name='index')
]