from django.db import models


class Podcast(models.Model):

    PROGRAMAS_CHOICES = (
        (1, 'informacion-privilegiada'),
        (2, 'a-todos-nos-pasa-lo-mismo'),
        (3, 'terapia-chilensis'),
        (4, 'aire-fresco'),
        (5, 'duna-en-punto'),
        (6, 'edicion-limitada'),
        (7, 'efecto-invernadero'),
        (8, 'hablemos-en-off'),
        (9, 'notables'),
        (10, 'noticias-en-duna'),
    )

    link = models.CharField(max_length=300, unique=True)
    date = models.DateTimeField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    program = models.IntegerField(choices=PROGRAMAS_CHOICES)

    @classmethod
    def get_programa_id(cls, programa):
        for p in cls.PROGRAMAS_CHOICES:
            if p[1] == programa:
                return p[0]

    def __unicode__(self):
        return u"%s" % (self.title,)

