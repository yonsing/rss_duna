from django.contrib.syndication.views import Feed
from django.shortcuts import render
from rss_duna.feed.rss import PodcastFetch
from django.utils.feedgenerator import Atom1Feed
from django.utils.feedgenerator import Rss201rev2Feed
import datetime

class DunaEntriesFeed(Feed):
    feed_type = Rss201rev2Feed
    title = "Podcasts Radio Duna"
    link = "http://tahoe.webfactional.com/feed/"
    description = "RSS Programas radio Duna"
    subtitle = ""

    def __call__(self, request, programa, *args, **kwargs):
        """ Llama a la vista padre, pasandole como parametro 
            en nombre del programa de radio, a su vez este parametro
            llega desde la URL """
        self.programa = programa
        self.title = programa
        self.description = programa
        return super(DunaEntriesFeed, self).__call__(request, *args, **kwargs)
        
    def items(self):
        #print "Programa: [%s]" % self.programa
        # Se traen los 5 ultimos podcasts
        f = PodcastFetch(self.programa)
        return f.get_podcasts()[:5]
        #return NewsItem.objects.order_by('-pub_date')[:5]

    def item_link(self, item):
        return item.link

    def item_description(self, item):
        return item.description

    def item_title(self, item):
        return item.title

    def item_enclosure_url(self, item):
        return item.link

    def item_enclosure_mime_type(self, item):
        return "audio/mpeg"

    def item_pubdate(self, item):
        return item.date





def get_feed_rss(request, programa_id):
    f = DunaEntriesFeed()
    return f(request, programa_id)
    #return HttpResponse("Pagina de Prueba.")

def list_feeds(request):
    return render(request, "podcasts.html")

def home(request):
    return render(request, "home.html")


