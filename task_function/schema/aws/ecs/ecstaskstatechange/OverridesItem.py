# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.ecs.ecstaskstatechange.Environment import Environment  # noqa: F401,E501

class OverridesItem(object):


    _types = {
        'environment': 'list[Environment]',
        'memory': 'float',
        'name': 'str',
        'cpu': 'float',
        'command': 'list[str]'
    }

    _attribute_map = {
        'environment': 'environment',
        'memory': 'memory',
        'name': 'name',
        'cpu': 'cpu',
        'command': 'command'
    }

    def __init__(self, environment=None, memory=None, name=None, cpu=None, command=None):  # noqa: E501
        self._environment = None
        self._memory = None
        self._name = None
        self._cpu = None
        self._command = None
        self.discriminator = None
        self.environment = environment
        self.memory = memory
        self.name = name
        self.cpu = cpu
        self.command = command


    @property
    def environment(self):

        return self._environment

    @environment.setter
    def environment(self, environment):


        self._environment = environment


    @property
    def memory(self):

        return self._memory

    @memory.setter
    def memory(self, memory):


        self._memory = memory


    @property
    def name(self):

        return self._name

    @name.setter
    def name(self, name):


        self._name = name


    @property
    def cpu(self):

        return self._cpu

    @cpu.setter
    def cpu(self, cpu):


        self._cpu = cpu


    @property
    def command(self):

        return self._command

    @command.setter
    def command(self, command):


        self._command = command

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
        if issubclass(OverridesItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, OverridesItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

