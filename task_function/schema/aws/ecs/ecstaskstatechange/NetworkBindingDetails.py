# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class NetworkBindingDetails(object):


    _types = {
        'bindIP': 'str',
        'protocol': 'str',
        'containerPort': 'float',
        'hostPort': 'float'
    }

    _attribute_map = {
        'bindIP': 'bindIP',
        'protocol': 'protocol',
        'containerPort': 'containerPort',
        'hostPort': 'hostPort'
    }

    def __init__(self, bindIP=None, protocol=None, containerPort=None, hostPort=None):  # noqa: E501
        self._bindIP = None
        self._protocol = None
        self._containerPort = None
        self._hostPort = None
        self.discriminator = None
        self.bindIP = bindIP
        self.protocol = protocol
        self.containerPort = containerPort
        self.hostPort = hostPort


    @property
    def bindIP(self):

        return self._bindIP

    @bindIP.setter
    def bindIP(self, bindIP):


        self._bindIP = bindIP


    @property
    def protocol(self):

        return self._protocol

    @protocol.setter
    def protocol(self, protocol):


        self._protocol = protocol


    @property
    def containerPort(self):

        return self._containerPort

    @containerPort.setter
    def containerPort(self, containerPort):


        self._containerPort = containerPort


    @property
    def hostPort(self):

        return self._hostPort

    @hostPort.setter
    def hostPort(self, hostPort):


        self._hostPort = hostPort

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
        if issubclass(NetworkBindingDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, NetworkBindingDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

