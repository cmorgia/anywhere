# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.ecs.ecstaskstatechange.NetworkBindingDetails import NetworkBindingDetails  # noqa: F401,E501
from schema.aws.ecs.ecstaskstatechange.NetworkInterfaceDetails import NetworkInterfaceDetails  # noqa: F401,E501

class ContainerDetails(object):


    _types = {
        'image': 'str',
        'imageDigest': 'str',
        'networkInterfaces': 'list[NetworkInterfaceDetails]',
        'networkBindings': 'list[NetworkBindingDetails]',
        'memory': 'str',
        'memoryReservation': 'str',
        'taskArn': 'str',
        'name': 'str',
        'exitCode': 'float',
        'cpu': 'str',
        'containerArn': 'str',
        'lastStatus': 'str',
        'runtimeId': 'str',
        'reason': 'str',
        'gpuIds': 'list[str]'
    }

    _attribute_map = {
        'image': 'image',
        'imageDigest': 'imageDigest',
        'networkInterfaces': 'networkInterfaces',
        'networkBindings': 'networkBindings',
        'memory': 'memory',
        'memoryReservation': 'memoryReservation',
        'taskArn': 'taskArn',
        'name': 'name',
        'exitCode': 'exitCode',
        'cpu': 'cpu',
        'containerArn': 'containerArn',
        'lastStatus': 'lastStatus',
        'runtimeId': 'runtimeId',
        'reason': 'reason',
        'gpuIds': 'gpuIds'
    }

    def __init__(self, image=None, imageDigest=None, networkInterfaces=None, networkBindings=None, memory=None, memoryReservation=None, taskArn=None, name=None, exitCode=None, cpu=None, containerArn=None, lastStatus=None, runtimeId=None, reason=None, gpuIds=None):  # noqa: E501
        self._image = None
        self._imageDigest = None
        self._networkInterfaces = None
        self._networkBindings = None
        self._memory = None
        self._memoryReservation = None
        self._taskArn = None
        self._name = None
        self._exitCode = None
        self._cpu = None
        self._containerArn = None
        self._lastStatus = None
        self._runtimeId = None
        self._reason = None
        self._gpuIds = None
        self.discriminator = None
        self.image = image
        self.imageDigest = imageDigest
        self.networkInterfaces = networkInterfaces
        self.networkBindings = networkBindings
        self.memory = memory
        self.memoryReservation = memoryReservation
        self.taskArn = taskArn
        self.name = name
        self.exitCode = exitCode
        self.cpu = cpu
        self.containerArn = containerArn
        self.lastStatus = lastStatus
        self.runtimeId = runtimeId
        self.reason = reason
        self.gpuIds = gpuIds


    @property
    def image(self):

        return self._image

    @image.setter
    def image(self, image):


        self._image = image


    @property
    def imageDigest(self):

        return self._imageDigest

    @imageDigest.setter
    def imageDigest(self, imageDigest):


        self._imageDigest = imageDigest


    @property
    def networkInterfaces(self):

        return self._networkInterfaces

    @networkInterfaces.setter
    def networkInterfaces(self, networkInterfaces):


        self._networkInterfaces = networkInterfaces


    @property
    def networkBindings(self):

        return self._networkBindings

    @networkBindings.setter
    def networkBindings(self, networkBindings):


        self._networkBindings = networkBindings


    @property
    def memory(self):

        return self._memory

    @memory.setter
    def memory(self, memory):


        self._memory = memory


    @property
    def memoryReservation(self):

        return self._memoryReservation

    @memoryReservation.setter
    def memoryReservation(self, memoryReservation):


        self._memoryReservation = memoryReservation


    @property
    def taskArn(self):

        return self._taskArn

    @taskArn.setter
    def taskArn(self, taskArn):


        self._taskArn = taskArn


    @property
    def name(self):

        return self._name

    @name.setter
    def name(self, name):


        self._name = name


    @property
    def exitCode(self):

        return self._exitCode

    @exitCode.setter
    def exitCode(self, exitCode):


        self._exitCode = exitCode


    @property
    def cpu(self):

        return self._cpu

    @cpu.setter
    def cpu(self, cpu):


        self._cpu = cpu


    @property
    def containerArn(self):

        return self._containerArn

    @containerArn.setter
    def containerArn(self, containerArn):


        self._containerArn = containerArn


    @property
    def lastStatus(self):

        return self._lastStatus

    @lastStatus.setter
    def lastStatus(self, lastStatus):


        self._lastStatus = lastStatus


    @property
    def runtimeId(self):

        return self._runtimeId

    @runtimeId.setter
    def runtimeId(self, runtimeId):


        self._runtimeId = runtimeId


    @property
    def reason(self):

        return self._reason

    @reason.setter
    def reason(self, reason):


        self._reason = reason


    @property
    def gpuIds(self):

        return self._gpuIds

    @gpuIds.setter
    def gpuIds(self, gpuIds):


        self._gpuIds = gpuIds

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
        if issubclass(ContainerDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ContainerDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

