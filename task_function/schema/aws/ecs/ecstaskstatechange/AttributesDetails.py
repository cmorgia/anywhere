# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class AttributesDetails(object):


    _types = {
        'name': 'str',
        'value': 'str'
    }

    _attribute_map = {
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, name=None, value=None):  # noqa: E501
        self._name = None
        self._value = None
        self.discriminator = None
        self.name = name
        self.value = value


    @property
    def name(self):

        return self._name

    @name.setter
    def name(self, name):


        self._name = name


    @property
    def value(self):

        return self._value

    @value.setter
    def value(self, value):


        self._value = value

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
        if issubclass(AttributesDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AttributesDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

