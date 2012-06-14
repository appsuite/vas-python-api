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


from vas.VFabricAdministrationServerError import VFabricAdministrationServerError
from vas.shared.Type import Type
from vas.util.LinkUtils import LinkUtils

class CollectionType(Type):
    def __init__(self, client, location, collection_key):
        self.__collection_key = collection_key
        super(CollectionType, self).__init__(client, location)

    def delete(self, item):
        """Delete an item from this collection

        .. note:: The contents of this collection are synchronized with the server after the operation is completed.

        :type item:     type of object contained in this collection
        :param item:    The item to delete
        """

        self._client.delete(item._location_self)
        self._initialize_attributes(self._client, self._location_self)

    def _create_item(self, location):
        raise VFabricAdministrationServerError('_create_item(self, location) method is unimplemented')

    def _initialize_attributes(self, client, location):
        super(CollectionType, self)._initialize_attributes(client, location)

    def __iter__(self):
        return iter([self._create_item(self_location) for self_location in
                     LinkUtils.get_collection_self_links(self._details, self.__collection_key)])
