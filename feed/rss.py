#!/usr/bin/python

import re
from xml.etree.ElementTree import fromstring
import datetime
import urllib
from models import Podcast
import logging

log = logging.getLogger('rss_duna.rss')

URL_DUNA = 'http://www.duna.cl/podcasts/?magazine=%s'


class PodcastFetch(object):

    def __init__(self, programa):
        log.debug("[PodcastFetch] programa: %s, hora: %s" % (programa, datetime.datetime.now()))
        self.programa = programa
        self.programa_id = Podcast.get_programa_id(programa)
        self.podcasts = None
        self._get_podcasts()

    def get_podcasts(self):
        return self.podcasts

    def _get_file(self, ruta):
        f = open(ruta, "r")
        html = f.read()
        return html

    def _get_html(self, url):
        return urllib.urlopen(url).read()
    
    def _get_html_procesado(self, html):
        m = re.search(r'<ul class="podcasts-list">.*?</ul>', html, re.DOTALL)
        return m.group(0)

    def _get_list_podcasts(self, xml):
        tree = fromstring(xml)
        lis = tree.findall('li')
        podcasts = []
        for p in lis:
            titulo = p.find('span/strong').text
            link = p.find('a').attrib['href']
            url = p.find('span/a').attrib['href']
            url_titulo = p.find('span/a').text
            busca_fecha = re.match('.*(\d\d\d\d)/(\d\d)/(\d\d).*', url)

            anio = int(busca_fecha.group(1))
            mes = int(busca_fecha.group(2))
            dia = int(busca_fecha.group(3))

            nombre_archivo = link.split('/')[-1]
            fecha = datetime.date(anio, mes, dia)

            titulo = "%s" % (titulo,)

            podcast = Podcast()
            podcast.title = titulo
            podcast.date = fecha
            podcast.link = link
            podcast.description = url_titulo

            podcasts.append(self._get_p(podcast))

        return podcasts

    def _get_p(self, podcast):
        try:
            p = Podcast.objects.get(link=podcast.link)
        except Podcast.DoesNotExist:
            log.debug('[_get_p] se agrega nuevo podcast: %s' % (podcast.link,))
            podcast.date = datetime.datetime.now()
            podcast.program = self.programa_id
            podcast.save()
            p = podcast

        return p

    def _get_podcasts(self):
        url = URL_DUNA % (self.programa,)
        html = self._get_html(url)
        xml = self._get_html_procesado(html)
        self.podcasts = self._get_list_podcasts(xml)

if __name__ == "__main__":
    f = PodcastFetch("informacion-privilegiada")
    print f.get_podcasts()

    #print get_podcasts("informacion-privilegiada")
