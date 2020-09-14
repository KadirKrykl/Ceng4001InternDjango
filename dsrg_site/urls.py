"""dsrg_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#Index
from website.views import index
#News
from website.views import news_list, news_list_filter_group, news_details
#Profiles
from website.views import profiles_list, profiles_details
#Project
from website.views import project_details, project_list, project_list_filter_group
#Research
from website.views import research_list, research_details, research_list_filter_group
#Publication
from website.views import publication_list
#Resource
from website.views import resource_list

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

news_patterns = ([
    path('', news_list, name='news'),
    path('<str:slug>', news_list_filter_group, name='news_group'),
    path('detail/<str:slug>',news_details, name='detail'),
], 'news')

profiles_patterns = ([
    path('', profiles_list, name='profiles'),
    path('<str:slug>',profiles_details, name='detail'),
], 'profiles')

project_patterns = ([
    path('', project_list, name='project'),
    path('<str:slug>', project_list_filter_group, name='project_group'),
    path('detail/<str:slug>',project_details, name='detail'),
], 'project')


research_patterns = ([
    path('', research_list, name='research'),
    path('<str:slug>', research_list_filter_group, name='research_group'),
    path('detail/<str:slug>',research_details, name='detail'),
], 'research')

publication_patterns = ([
    path('', publication_list, name='publication'),
], 'publication')

resource_patterns = ([
    path('', resource_list, name='resource'),
], 'resource')

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('',view=index, name='home'),
    path('news/', include(news_patterns, namespace='news')),
    path('people/', include(profiles_patterns, namespace='profiles')),
    path('project/', include(project_patterns, namespace='project')),
    path('research/', include(research_patterns, namespace='research')),
    path('publication/', include(publication_patterns, namespace='publication')),
    path('resource/', include(resource_patterns, namespace='resource')),
)