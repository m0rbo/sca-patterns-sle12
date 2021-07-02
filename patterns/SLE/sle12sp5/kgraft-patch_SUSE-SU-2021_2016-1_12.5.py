#!/usr/bin/python
#
# Title:       Moderate Security Announcement for kgraft-patch SUSE-SU-2021:2016-1
# Description: Security fixes for SUSE Linux Kernel Live Patch 12 SP5
# Source:      Security Announcement Parser v1.6.1
# Modified:    2021 Jul 02
#
##############################################################################
# Copyright (C) 2021 SUSE LLC
##############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
#  Authors/Contributors:
#   Jason Record <jason.record@suse.com>
#
##############################################################################

import os
import Core
import SUSE

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "kgraft-patch"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2021-June/009047.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'kgraft-patch'
MAIN = ''
SEVERITY = 'Moderate'
TAG = 'SUSE-SU-2021:2016-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 12):
	if ( SERVER['DistroPatchLevel'] == 5 ):
		PACKAGES = {
			'libxml2-2': '2.9.4-46.46.1',
			'libxml2-2-32bit': '2.9.4-46.46.1',
			'libxml2-2-debuginfo': '2.9.4-46.46.1',
			'libxml2-2-debuginfo-32bit': '2.9.4-46.46.1',
			'libxml2-debugsource': '2.9.4-46.46.1',
			'libxml2-doc': '2.9.4-46.46.1',
			'libxml2-tools': '2.9.4-46.46.1',
			'libxml2-tools-debuginfo': '2.9.4-46.46.1',
			'python-libxml2': '2.9.4-46.46.1',
			'python-libxml2-debuginfo': '2.9.4-46.46.1',
			'python-libxml2-debugsource': '2.9.4-46.46.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

