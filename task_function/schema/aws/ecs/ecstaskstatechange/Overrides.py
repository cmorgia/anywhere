# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.ecs.ecstaskstatechange.OverridesItem import OverridesItem  # noqa: F401,E501

class Overrides(object):


    _types = {
        'containerOverrides': 'list[OverridesItem]'
    }

    _attribute_map = {
        'containerOverrides': 'containerOverrides'
    }

    def __init__(self, containerOverrides=None):  # noqa: E501
        self._containerOverrides = None
        self.discriminator = None
        self.containerOverrides = containerOverrides


    @property
    def containerOverrides(self):

        return self._containerOverrides

    @containerOverrides.setter
    def containerOverrides(self, containerOverrides):


        self._containerOverrides = containerOverrides

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
        if issubclass(Overrides, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Overrides):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

