"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from polls import views as polls_views
from django.contrib import admin
from rest_framework import routers
from UserProfile import views as profile_views
from rest_framework.routers import DefaultRouter
from UserProfile.views import UserViewSet, ProfileViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')
router.register(r'profile', ProfileViewSet, base_name='profile')
urlpatterns = router.urls
login_page = UserViewSet.as_view({'post': 'login'})
profile = ProfileViewSet.as_view({'post': 'make'})

urlpatterns+= [
    #path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    #path('api-auth/', include('django-rest-framework.urls')),
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('accounts/update/', profile_views.edit_user, name='account_update'),
    #path('login', profile_views.Login.as_view(), name='login'),
    #path('logout', profile_views.Logout.as_view(), name='delete'),
    #path('user', profile_views.User.as_view(), name='user'),

]

urlpatterns += i18n_patterns(
     #path('polls/', include('polls.urls')),
    #path('polls/translationspage/', polls_views.login, name='page'),
    #prefix_default_language= False
)



#urlpatterns = [
#    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
#        home_files, name='home-files'),
#]

#urlpatterns += i18n_patterns(
#    url(r'^$', home, name='home'),
#    url(r'^admin/', include(admin.site.urls)),
#)