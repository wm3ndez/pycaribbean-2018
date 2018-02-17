from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from blog.main.views import HomeView, Authors

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('authors/', Authors.as_view(), name='authors'),
    path('blog-1/', include('blog.blog1.urls')),
    path('blog-2/', include('blog.blog2.urls')),
    path('blog-3/', include('blog.blog3.urls')),
    path('blog-4/', include('blog.blog4.urls')),
    path('admin/', admin.site.urls),
    path(r'django-rq/', include('django_rq.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
