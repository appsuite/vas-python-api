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


from vas.shared.Security import Security
from vas.util.LinkUtils import LinkUtils

class Type:
    __REL_SECURITY = 'security'

    __REL_SELF = 'self'

    def __init__(self, client, location):
        self._client = client
        self._initialize_attributes(client, location)

    @property
    def security(self):
        """The security configuration for this item or collection

        :rtype:     :class:`vas.shared.Security`
        :return:    The security configuration for this item or collection
        """

        return Security(self._client, self.__location_security)

    def _initialize_attributes(self, client, location):
        self._details = client.get(location)
        self._links = LinkUtils.get_links(client.get(location))

        self._location_self = self._links[self.__REL_SELF][0]
        self.__location_security = self._links[self.__REL_SECURITY][0]

    def __eq__(self, other):
        return self._location_self == other._location_self

    def __hash__(self):
        return hash(self._location_self)

    def __lt__(self, other):
        return self._location_self < other._location_self