# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class NetworkInterfaceDetails(object):


    _types = {
        'privateIpv4Address': 'str',
        'ipv6Address': 'str',
        'attachmentId': 'str'
    }

    _attribute_map = {
        'privateIpv4Address': 'privateIpv4Address',
        'ipv6Address': 'ipv6Address',
        'attachmentId': 'attachmentId'
    }

    def __init__(self, privateIpv4Address=None, ipv6Address=None, attachmentId=None):  # noqa: E501
        self._privateIpv4Address = None
        self._ipv6Address = None
        self._attachmentId = None
        self.discriminator = None
        self.privateIpv4Address = privateIpv4Address
        self.ipv6Address = ipv6Address
        self.attachmentId = attachmentId


    @property
    def privateIpv4Address(self):

        return self._privateIpv4Address

    @privateIpv4Address.setter
    def privateIpv4Address(self, privateIpv4Address):


        self._privateIpv4Address = privateIpv4Address


    @property
    def ipv6Address(self):

        return self._ipv6Address

    @ipv6Address.setter
    def ipv6Address(self, ipv6Address):


        self._ipv6Address = ipv6Address


    @property
    def attachmentId(self):

        return self._attachmentId

    @attachmentId.setter
    def attachmentId(self, attachmentId):


        self._attachmentId = attachmentId

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NetworkInterfaceDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, NetworkInterfaceDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

