# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
import jewish

def format_date(date, **options):
    return jewish.JewishDate.from_date(date)

class HebrewDatesPlugin(Plugin):
    name = 'Hebrew dates'
    description = u'Add your description here.'

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['jewish_date'] = format_date
