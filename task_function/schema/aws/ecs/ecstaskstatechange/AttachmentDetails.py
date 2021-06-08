# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.ecs.ecstaskstatechange.AttachmentDetails_details import AttachmentDetails_details  # noqa: F401,E501

class AttachmentDetails(object):


    _types = {
        'id': 'str',
        'type': 'str',
        'status': 'str',
        'details': 'AttachmentDetails_details'
    }

    _attribute_map = {
        'id': 'id',
        'type': 'type',
        'status': 'status',
        'details': 'details'
    }

    def __init__(self, id=None, type=None, status=None, details=None):  # noqa: E501
        self._id = None
        self._type = None
        self._status = None
        self._details = None
        self.discriminator = None
        self.id = id
        self.type = type
        self.status = status
        self.details = details


    @property
    def id(self):

        return self._id

    @id.setter
    def id(self, id):


        self._id = id


    @property
    def type(self):

        return self._type

    @type.setter
    def type(self, type):


        self._type = type


    @property
    def status(self):

        return self._status

    @status.setter
    def status(self, status):


        self._status = status


    @property
    def details(self):

        return self._details

    @details.setter
    def details(self, details):


        self._details = details

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
        if issubclass(AttachmentDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AttachmentDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

