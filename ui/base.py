# -*- coding: utf-8 -*-
##
## Copyright © 2012 Saeed Rasooli <saeed.gnu@gmail.com> (ilius)
## This file is part of PyGlossary project, http://sourceforge.net/projects/pyglossary/
##
## This program is a free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3, or (at your option)
## any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License along
## with this program. Or on Debian systems, from /usr/share/common-licenses/GPL
## If not, see <http://www.gnu.org/licenses/gpl.txt>.

from os.path import join

from .paths import srcDir, rootDir
from pyglossary.glossary import *

def fread(path):
    with open(path) as fp:
        return fp.read()

logo = join(rootDir, 'res', 'pyglossary.png')
aboutText = fread(join(rootDir, 'about'))
licenseText = fread(join(rootDir, 'license'))
authors = fread(join(rootDir, 'AUTHORS')).split('\n')


class UIBase(object):
    prefSavePath = [
        confPath,
        join(srcDir, 'rc.py')
    ]
    prefKeys = (
        'noProgressBar',## command line
        'save',
        'ui_autoSetFormat',
        'ui_autoSetOutputFileName',
        'lower',
        'utf8Check',
        'enable_alts',
        ## Reverse Options:
        'reverse_matchWord',
        'reverse_showRel',
        'reverse_saveStep',
        'reverse_minRel',
        'reverse_maxNum',
        'reverse_includeDefs',
    )
    def pref_load(self, **options):
        rc_code = fread(join(srcDir, 'rc.py'))
        data = {}
        exec(
            rc_code,
            None,
            data,
        )
        if data['save']==0 and os.path.exists(self.prefSavePath[0]): # save is defined in rc.py
            try:
                fp = open(self.prefSavePath[0])
            except:
                log.exception('error while loading save file %s'%self.prefSavePath[0])
            else:
                exec(fp.read(), None, data)
            finally:
                fp.close()
        for key in self.prefKeys:
            self.pref[key] = data[key]
        for key, value in options.items():
            if key in self.prefKeys:
                self.pref[key] = value
        return True




