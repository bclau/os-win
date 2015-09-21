#  Copyright 2013 Cloudbase Solutions Srl
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslotest import base

from os_win.utils.compute import rdpconsoleutils


class RDPConsoleUtilsTestCase(base.BaseTestCase):
    def setUp(self):
        self._rdpconsoleutils = rdpconsoleutils.RDPConsoleUtils()
        super(RDPConsoleUtilsTestCase, self).setUp()

    def test_get_rdp_console_port(self):
        listener_port = self._rdpconsoleutils.get_rdp_console_port()

        self.assertEqual(self._rdpconsoleutils._DEFAULT_HYPERV_RDP_PORT,
                         listener_port)