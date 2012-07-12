# vFabric Administration Server API
# Copyright (c) 2012 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from unittest.case import TestCase
from vas.shared.Security import Security
from vas.tc_server.TcServerGroupApplication import TcServerGroupApplication
from vas.tc_server.TcServerNodeApplication import TcServerNodeApplication
from vas.tc_server.TcServerNodeInstance import TcServerNodeInstance
from vas.tc_server.TcServerNodeRevisions import TcServerNodeRevisions
from vas.test.StubClient import StubClient

class TestTcServerNodeApplication(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__application = TcServerNodeApplication(self.__client,
            'https://localhost:8443/tc-server/v1/nodes/0/instances/3/applications/5/')

    def test_attributes(self):
        self.assertEqual('/example', self.__application.context_path)
        self.assertEqual('localhost', self.__application.host)
        self.assertEqual('Example', self.__application.name)
        self.assertEqual('Catalina', self.__application.service)
        self.assertIsInstance(self.__application.group_application, TcServerGroupApplication)
        self.assertIsInstance(self.__application.node_instance, TcServerNodeInstance)
        self.assertIsInstance(self.__application.node_revisions, TcServerNodeRevisions)
        self.assertIsInstance(self.__application.security, Security)