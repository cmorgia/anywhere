# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.ecs.ecstaskstatechange.AttachmentDetails import AttachmentDetails  # noqa: F401,E501
from schema.aws.ecs.ecstaskstatechange.AttributesDetails import AttributesDetails  # noqa: F401,E501
from schema.aws.ecs.ecstaskstatechange.ContainerDetails import ContainerDetails  # noqa: F401,E501
from schema.aws.ecs.ecstaskstatechange.Overrides import Overrides  # noqa: F401,E501

class ECSTaskStateChange(object):


    _types = {
        'overrides': 'Overrides',
        'executionStoppedAt': 'datetime',
        'memory': 'str',
        'attachments': 'list[AttachmentDetails]',
        'attributes': 'list[AttributesDetails]',
        'pullStartedAt': 'datetime',
        'taskArn': 'str',
        'startedAt': 'datetime',
        'createdAt': 'datetime',
        'clusterArn': 'str',
        'connectivity': 'str',
        'platformVersion': 'str',
        'containerInstanceArn': 'str',
        'launchType': 'str',
        'group': 'str',
        'updatedAt': 'datetime',
        'stopCode': 'str',
        'pullStoppedAt': 'datetime',
        'connectivityAt': 'datetime',
        'startedBy': 'str',
        'cpu': 'str',
        'version': 'float',
        'stoppingAt': 'datetime',
        'stoppedAt': 'datetime',
        'taskDefinitionArn': 'str',
        'stoppedReason': 'str',
        'containers': 'list[ContainerDetails]',
        'desiredStatus': 'str',
        'lastStatus': 'str',
        'availabilityZone': 'str'
    }

    _attribute_map = {
        'overrides': 'overrides',
        'executionStoppedAt': 'executionStoppedAt',
        'memory': 'memory',
        'attachments': 'attachments',
        'attributes': 'attributes',
        'pullStartedAt': 'pullStartedAt',
        'taskArn': 'taskArn',
        'startedAt': 'startedAt',
        'createdAt': 'createdAt',
        'clusterArn': 'clusterArn',
        'connectivity': 'connectivity',
        'platformVersion': 'platformVersion',
        'containerInstanceArn': 'containerInstanceArn',
        'launchType': 'launchType',
        'group': 'group',
        'updatedAt': 'updatedAt',
        'stopCode': 'stopCode',
        'pullStoppedAt': 'pullStoppedAt',
        'connectivityAt': 'connectivityAt',
        'startedBy': 'startedBy',
        'cpu': 'cpu',
        'version': 'version',
        'stoppingAt': 'stoppingAt',
        'stoppedAt': 'stoppedAt',
        'taskDefinitionArn': 'taskDefinitionArn',
        'stoppedReason': 'stoppedReason',
        'containers': 'containers',
        'desiredStatus': 'desiredStatus',
        'lastStatus': 'lastStatus',
        'availabilityZone': 'availabilityZone'
    }

    def __init__(self, overrides=None, executionStoppedAt=None, memory=None, attachments=None, attributes=None, pullStartedAt=None, taskArn=None, startedAt=None, createdAt=None, clusterArn=None, connectivity=None, platformVersion=None, containerInstanceArn=None, launchType=None, group=None, updatedAt=None, stopCode=None, pullStoppedAt=None, connectivityAt=None, startedBy=None, cpu=None, version=None, stoppingAt=None, stoppedAt=None, taskDefinitionArn=None, stoppedReason=None, containers=None, desiredStatus=None, lastStatus=None, availabilityZone=None):  # noqa: E501
        self._overrides = None
        self._executionStoppedAt = None
        self._memory = None
        self._attachments = None
        self._attributes = None
        self._pullStartedAt = None
        self._taskArn = None
        self._startedAt = None
        self._createdAt = None
        self._clusterArn = None
        self._connectivity = None
        self._platformVersion = None
        self._containerInstanceArn = None
        self._launchType = None
        self._group = None
        self._updatedAt = None
        self._stopCode = None
        self._pullStoppedAt = None
        self._connectivityAt = None
        self._startedBy = None
        self._cpu = None
        self._version = None
        self._stoppingAt = None
        self._stoppedAt = None
        self._taskDefinitionArn = None
        self._stoppedReason = None
        self._containers = None
        self._desiredStatus = None
        self._lastStatus = None
        self._availabilityZone = None
        self.discriminator = None
        self.overrides = overrides
        self.executionStoppedAt = executionStoppedAt
        self.memory = memory
        self.attachments = attachments
        self.attributes = attributes
        self.pullStartedAt = pullStartedAt
        self.taskArn = taskArn
        self.startedAt = startedAt
        self.createdAt = createdAt
        self.clusterArn = clusterArn
        self.connectivity = connectivity
        self.platformVersion = platformVersion
        self.containerInstanceArn = containerInstanceArn
        self.launchType = launchType
        self.group = group
        self.updatedAt = updatedAt
        self.stopCode = stopCode
        self.pullStoppedAt = pullStoppedAt
        self.connectivityAt = connectivityAt
        self.startedBy = startedBy
        self.cpu = cpu
        self.version = version
        self.stoppingAt = stoppingAt
        self.stoppedAt = stoppedAt
        self.taskDefinitionArn = taskDefinitionArn
        self.stoppedReason = stoppedReason
        self.containers = containers
        self.desiredStatus = desiredStatus
        self.lastStatus = lastStatus
        self.availabilityZone = availabilityZone


    @property
    def overrides(self):

        return self._overrides

    @overrides.setter
    def overrides(self, overrides):


        self._overrides = overrides


    @property
    def executionStoppedAt(self):

        return self._executionStoppedAt

    @executionStoppedAt.setter
    def executionStoppedAt(self, executionStoppedAt):


        self._executionStoppedAt = executionStoppedAt


    @property
    def memory(self):

        return self._memory

    @memory.setter
    def memory(self, memory):


        self._memory = memory


    @property
    def attachments(self):

        return self._attachments

    @attachments.setter
    def attachments(self, attachments):


        self._attachments = attachments


    @property
    def attributes(self):

        return self._attributes

    @attributes.setter
    def attributes(self, attributes):


        self._attributes = attributes


    @property
    def pullStartedAt(self):

        return self._pullStartedAt

    @pullStartedAt.setter
    def pullStartedAt(self, pullStartedAt):


        self._pullStartedAt = pullStartedAt


    @property
    def taskArn(self):

        return self._taskArn

    @taskArn.setter
    def taskArn(self, taskArn):


        self._taskArn = taskArn


    @property
    def startedAt(self):

        return self._startedAt

    @startedAt.setter
    def startedAt(self, startedAt):


        self._startedAt = startedAt


    @property
    def createdAt(self):

        return self._createdAt

    @createdAt.setter
    def createdAt(self, createdAt):


        self._createdAt = createdAt


    @property
    def clusterArn(self):

        return self._clusterArn

    @clusterArn.setter
    def clusterArn(self, clusterArn):


        self._clusterArn = clusterArn


    @property
    def connectivity(self):

        return self._connectivity

    @connectivity.setter
    def connectivity(self, connectivity):


        self._connectivity = connectivity


    @property
    def platformVersion(self):

        return self._platformVersion

    @platformVersion.setter
    def platformVersion(self, platformVersion):


        self._platformVersion = platformVersion


    @property
    def containerInstanceArn(self):

        return self._containerInstanceArn

    @containerInstanceArn.setter
    def containerInstanceArn(self, containerInstanceArn):


        self._containerInstanceArn = containerInstanceArn


    @property
    def launchType(self):

        return self._launchType

    @launchType.setter
    def launchType(self, launchType):


        self._launchType = launchType


    @property
    def group(self):

        return self._group

    @group.setter
    def group(self, group):


        self._group = group


    @property
    def updatedAt(self):

        return self._updatedAt

    @updatedAt.setter
    def updatedAt(self, updatedAt):


        self._updatedAt = updatedAt


    @property
    def stopCode(self):

        return self._stopCode

    @stopCode.setter
    def stopCode(self, stopCode):


        self._stopCode = stopCode


    @property
    def pullStoppedAt(self):

        return self._pullStoppedAt

    @pullStoppedAt.setter
    def pullStoppedAt(self, pullStoppedAt):


        self._pullStoppedAt = pullStoppedAt


    @property
    def connectivityAt(self):

        return self._connectivityAt

    @connectivityAt.setter
    def connectivityAt(self, connectivityAt):


        self._connectivityAt = connectivityAt


    @property
    def startedBy(self):

        return self._startedBy

    @startedBy.setter
    def startedBy(self, startedBy):


        self._startedBy = startedBy


    @property
    def cpu(self):

        return self._cpu

    @cpu.setter
    def cpu(self, cpu):


        self._cpu = cpu


    @property
    def version(self):

        return self._version

    @version.setter
    def version(self, version):


        self._version = version


    @property
    def stoppingAt(self):

        return self._stoppingAt

    @stoppingAt.setter
    def stoppingAt(self, stoppingAt):


        self._stoppingAt = stoppingAt


    @property
    def stoppedAt(self):

        return self._stoppedAt

    @stoppedAt.setter
    def stoppedAt(self, stoppedAt):


        self._stoppedAt = stoppedAt


    @property
    def taskDefinitionArn(self):

        return self._taskDefinitionArn

    @taskDefinitionArn.setter
    def taskDefinitionArn(self, taskDefinitionArn):


        self._taskDefinitionArn = taskDefinitionArn


    @property
    def stoppedReason(self):

        return self._stoppedReason

    @stoppedReason.setter
    def stoppedReason(self, stoppedReason):


        self._stoppedReason = stoppedReason


    @property
    def containers(self):

        return self._containers

    @containers.setter
    def containers(self, containers):


        self._containers = containers


    @property
    def desiredStatus(self):

        return self._desiredStatus

    @desiredStatus.setter
    def desiredStatus(self, desiredStatus):


        self._desiredStatus = desiredStatus


    @property
    def lastStatus(self):

        return self._lastStatus

    @lastStatus.setter
    def lastStatus(self, lastStatus):


        self._lastStatus = lastStatus


    @property
    def availabilityZone(self):

        return self._availabilityZone

    @availabilityZone.setter
    def availabilityZone(self, availabilityZone):


        self._availabilityZone = availabilityZone

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
        if issubclass(ECSTaskStateChange, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ECSTaskStateChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

