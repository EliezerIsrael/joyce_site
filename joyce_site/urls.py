from django.conf.urls import url
from django.http import HttpResponseRedirect

static_pages = [
    # "about",
    # "donate",
    # "strategy",
    # "supporters",
    # "team",
    # "help",
    # "connect",
    # "visualizations",
    # "jobs",
    # "terms",
    # "privacy-policy",
    # "coming-soon",
    # "shraga-silverstein",
    # "adin-even-israel-steinsaltz",
    # "william-davidson-talmud",
    # "linker",
    # "ios",
    # "mobile",
    # "sefaria-edition",
    # "sefaria-community-translation",
    # "contributed-to-sefaria",
    # "translation-guidelines",
    # "transliteration-guidelines",
    # "even-haezer-guidelines",
    # "random-walk-through-torah",
    # "educators",
    # "the-sefaria-story",
    # "aramaic-translation-contest",
]

# Semi Static Content
site_urlpatterns = [
    # url(r'^$', reader_views.home, name="home"),
    # url(r'^metrics/?$', reader_views.metrics),
    # url(r'^digitized-by-sefaria/?$', reader_views.digitized_by_sefaria),
    # url(r'^(%s)/?$' % "|".join(static_pages), reader_views.serve_static),
]

# Redirects to Forum, Wiki, etc
site_urlpatterns += [
    # url(r'^forum/?$', lambda x: HttpResponseRedirect('https://groups.google.com/forum/?fromgroups#!forum/sefaria')),
    # url(r'^wiki/?$', lambda x: HttpResponseRedirect('https://github.com/Sefaria/Sefaria-Project/wiki')),
    # url(r'^developers/?$', lambda x: HttpResponseRedirect('https://github.com/Sefaria/Sefaria-Project/wiki#developers')),
    # url(r'^request-a-text/?$', lambda x: HttpResponseRedirect('https://goo.gl/forms/ru33ivawo7EllQxa2')),
    # url(r'^request-a-training/?$', lambda x: HttpResponseRedirect(' https://docs.google.com/forms/d/1CJZHRivM2qFeF2AE2afpvE1m86AgJPCxUEFu5EG92F8/edit?usp=sharing_eil&ts=5a4dc5e0')),
    # url(r'^contribute/?$', lambda x: HttpResponseRedirect('https://github.com/Sefaria/Sefaria-Project/wiki/Guide-to-Contributing')),
    # url(r'^faq/?$', lambda x: HttpResponseRedirect('https://github.com/Sefaria/Sefaria-Project/wiki#frequently-asked-questions')),
    # url(r'^textmap/?$', lambda x: HttpResponseRedirect('/static/files/Sefaria-Text-Map-June-2016.pdf')),
    # url(r'^workshop/?$', lambda x: HttpResponseRedirect('/static/files/Sefaria_SummerMeeting_2016.pdf')),
    # url(r'^ideasforteaching/?$', lambda x: HttpResponseRedirect('/static/files/Sefaria_Teacher_Generated_Ideas_for_Your_Classroom.pdf')),
    # url(r'^gala/?$', lambda x: HttpResponseRedirect('https://www.501auctions.com/sefaria')),
    # url(r'^jfn?$', lambda x: HttpResponseRedirect('https://www.sefaria.org/sheets/60494')),
]