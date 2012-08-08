from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quest.views.home', name='home'),
    # url(r'^quest/', include('quest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r"^quest/quest", "quest.views.quest", name="quest"),
    url(r"^quest/colab", "quest.views.quest_colab", name="quest-colab"),

    url(r"^quest/nutri", "quest.views.quest_nutri", name="quest-nutri"),
    url(r"^quest/pg", "quest.views.quest_pg", name="quest-pg"),
    url(r"^quest/tech", "quest.views.quest_tech", name="quest-tech"),

    url(r'^resp/$', 'quest.views.resp', name="resp"),
)