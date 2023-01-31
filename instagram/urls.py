from django.urls import include, path
from rest_framework.routers import DefaultRouter
from instagram import views
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('example', views.ExampleView.as_view(), name='example'),
    path('example_view', views.example_view, name='example_view')
    # path('post/', views.PostViewSet.as_view(), name='post'),
    # path('post/<int:pk>', views.PostDetailView.as_view(), name='post'),
    # path('static_html_view', views.static_html_view, name='static_html_view'),
    # path('hello/', views.hello, name='hello'),
    # path('post/<int:pk>', views.PostViewSet.as_view({'get': 'retrieve'}), name='post'),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
