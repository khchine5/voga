# -*- coding: UTF-8 -*-
# Copyright 2012-2016 Luc Saffre
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

from lino_voga import SETUP_INFO


class Site(Site):
    version = SETUP_INFO['version']
    verbose_name = "Lino Voga"
    url = SETUP_INFO['url']

    #~ help_url = "http://lino.saffre-rumma.net/az/index.html"

    migration_class = 'lino_voga.migrate.Migrator'

    userdocs_prefix = 'voga.'

    user_profiles_module = 'lino_voga.projects.roles'

    demo_fixtures = 'std minimal_ledger demo demo_bookings buche voga demo2'.split()

    languages = 'en de et'

    show_internal_field_names = True

    default_build_method = "wkhtmltopdf"

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.gfks'
        # yield 'lino.modlib.system'
        yield 'lino.modlib.users'
        yield 'lino.modlib.countries'
        yield 'lino_voga.lib.contacts'
        yield 'lino_xl.lib.lists'
        yield 'lino_xl.lib.beid'

        yield 'lino_voga.lib.cal'
        yield 'lino_voga.lib.products'
        # yield 'lino_xl.lib.extensible'
        yield 'lino_voga.lib.rooms'

        yield 'lino_voga.lib.courses'

        # yield 'lino_xl.lib.products'
        # yield 'lino_cosi.lib.accounts'
        # yield 'lino_cosi.lib.ledger'
        # yield 'lino_cosi.lib.vat'
        #~ yield 'lino_cosi.lib.declarations'
        #~ yield 'lino_cosi.lib.sales'
        # yield 'lino_cosi.lib.auto.sales'
        yield 'lino_cosi.lib.finan'
        yield 'lino_cosi.lib.sepa'

        # yield 'lino_voga.lib.courses'

        #~ yield 'lino_xl.lib.households'
        yield 'lino_xl.lib.notes'
        yield 'lino.modlib.uploads'
        #~ yield 'lino_xl.lib.cal'

        yield 'lino_xl.lib.outbox'
        yield 'lino_xl.lib.excerpts'
        #~ yield 'lino_xl.lib.pages'
        #~ yield 'lino_cosi.lib.courses'
        yield 'lino_voga.lib.voga'

        yield 'lino.modlib.export_excel'
        yield 'lino_xl.lib.extensible'
        yield 'lino.modlib.wkhtmltopdf'
        yield 'lino_xl.lib.appypod'

    def get_admin_main_items(self, ar):
        yield self.modules.courses.DraftCourses
        yield self.modules.courses.ActiveCourses

    def setup_plugins(self):
        """
        Change the default value of certain plugin settings.
       
        """
        self.plugins.extensible.configure(calendar_start_hour=9)
        self.plugins.extensible.configure(calendar_end_hour=21)
        self.plugins.vat.configure(default_vat_class='exempt')
        self.plugins.ledger.configure(start_year=2015)
        super(Site, self).setup_plugins()
