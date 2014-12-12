from django.conf.urls import patterns, include, url
from django.contrib import admin
from eecourses.viewsets import CourseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/courses', CourseViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eecun.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(R'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
