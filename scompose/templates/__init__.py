'''

Copyright (C) 2019 Vanessa Sochat.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

from scompose.logger import bot
from scompose.utils import get_installdir

import os

def get_template(name):
    '''get a template by name from this directory. If does not exist,
       return None.
    '''
    here = get_installdir()
    template = os.path.join(here, 'templates', name)
    if os.path.exists(template):
        return template
    bot.warning('%s does not exist.' % template)
