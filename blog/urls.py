from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^logout/','app_blog.views.viewLogout'),
     url(r'^login/','app_blog.views.viewLogin'),
     url(r'^accounts/login/','app_blog.views.viewLogin'),
     url(r'^registerAgree/','app_blog.views.registerAgree'),
     url(r'^$','app_blog.views.viewYearPosts'),
     url(r'^tinymce/', include('tinymce.urls')),
     url(r'^ckeditor/',include('ckeditor.urls')),
     url(r'^post/(?P<post>\d{1,8})','app_blog.views.viewPost'),
     url(r'^posts/year/(?P<year>\d\d\d\d)', 'app_blog.views.viewYearPosts'),
     url(r'^comment/(?P<post>\d{1,8})','app_blog.views.putComment'),
     url(r'^requestMeals/','requestMeals.views.viewRequestsMeals'),
     )#+ static(settings.TINYMCE_JS_URL, document_root=settings.TINYMCE_JS_ROOT)

