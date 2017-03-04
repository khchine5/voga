# -*- coding: UTF-8 -*-
# Copyright 2012-2017 Luc Saffre
# This file is part of Lino Voga.
#
# Lino Voga is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Lino Voga is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with Lino Voga.  If not, see
# <http://www.gnu.org/licenses/>.

from lino.projects.std.settings import *

from lino.api import _

from lino_voga import SETUP_INFO


class Site(Site):
    version = SETUP_INFO['version']
    verbose_name = "Lino Voga"
    url = SETUP_INFO['url']

    #~ help_url = "http://lino.saffre-rumma.net/az/index.html"

    migration_class = 'lino_voga.lib.voga.migrate.Migrator'

    # userdocs_prefix = 'voga.'

    user_types_module = 'lino_voga.lib.voga.user_types'
    workflows_module = 'lino_xl.lib.cal.workflows.voga'
    custom_layouts_module = 'lino_voga.lib.voga.layouts'

    demo_fixtures = 'std minimal_ledger demo demo_bookings payments voga checkdata demo2'.split()

    languages = 'en de et'

    show_internal_field_names = True

    # default_build_method = "wkhtmltopdf"
    default_build_method = "appypdf"
    auto_configure_logger_names = 'schedule atelier django lino lino_xl lino_voga'

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        # yield 'lino.modlib.gfks'
        # yield 'lino.modlib.system'
        yield 'lino.modlib.users'
        yield 'lino_xl.lib.countries'
        yield 'lino_voga.lib.contacts'
        yield 'lino_xl.lib.lists'
        yield 'lino_xl.lib.beid'

        yield 'lino.modlib.plausibility'

        yield 'lino_voga.lib.cal'
        yield 'lino_voga.lib.products'
        yield 'lino_voga.lib.rooms'
        yield 'lino_voga.lib.sales'
        yield 'lino_voga.lib.invoicing'

        yield 'lino_voga.lib.courses'

        # yield 'lino_xl.lib.products'
        # yield 'lino_xl.lib.accounts'
        # yield 'lino_xl.lib.ledger'
        # yield 'lino_xl.lib.vat'
        #~ yield 'lino_cosi.lib.declarations'
        #~ yield 'lino_xl.lib.sales'
        # yield 'lino_cosi.lib.auto.sales'
        yield 'lino_xl.lib.finan'
        yield 'lino_xl.lib.sepa'

        # yield 'lino_voga.lib.courses'

        #~ yield 'lino_xl.lib.households'
        yield 'lino_xl.lib.notes'
        yield 'lino.modlib.uploads'
        #~ yield 'lino_xl.lib.cal'

        yield 'lino_xl.lib.outbox'
        yield 'lino_xl.lib.excerpts'
        #~ yield 'lino_xl.lib.pages'
        #~ yield 'lino_xl.lib.courses'
        yield 'lino_voga.lib.voga'

        yield 'lino.modlib.export_excel'
        yield 'lino_xl.lib.extensible'
        yield 'lino.modlib.wkhtmltopdf'  # obsolete
        yield 'lino.modlib.weasyprint'
        yield 'lino_xl.lib.appypod'
        yield 'lino.modlib.changes'

    def do_site_startup(self):
        super(Site, self).do_site_startup()

        from lino.modlib.changes.models import watch_changes as wc

        wc(self.models.contacts.Partner)
        wc(self.models.contacts.Person, master_key='partner_ptr')
        wc(self.models.contacts.Company, master_key='partner_ptr')
        wc(self.models.courses.Pupil, master_key='partner_ptr')

    def unused_get_dashboard_items(self, user):
        """Defines the story to be displayed on the admin main page.

        """
        yield self.actors.courses.MyCoursesGiven
        yield self.actors.courses.StatusReport

    def setup_plugins(self):
        """
        Change the default value of certain plugin settings.
       
        """
        if self.is_installed('extensible'):
            self.plugins.extensible.configure(calendar_start_hour=9)
            self.plugins.extensible.configure(calendar_end_hour=21)
        self.plugins.vat.configure(default_vat_class='exempt')
        self.plugins.ledger.configure(start_year=2015)
        super(Site, self).setup_plugins()

    def setup_quicklinks(self, user, tb):
        super(Site, self).setup_quicklinks(user, tb)
        tb.add_action(self.actors.courses.Pupils)
        tb.add_action(
            self.actors.courses.Pupils.insert_action,
            label=_("New {}").format(
                self.models.courses.Pupil._meta.verbose_name))

        
