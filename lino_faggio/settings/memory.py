from lino_faggio.settings.demo import *
SITE = Site(globals(),title = "Lino-Faggio (:memory:)") 
DATABASES['default']['NAME'] = ':memory:'
