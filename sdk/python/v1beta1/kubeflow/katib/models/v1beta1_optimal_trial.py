# coding: utf-8

"""
    Katib

    Swagger description for Katib  # noqa: E501

    OpenAPI spec version: v1beta1-0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from kubeflow.katib.models.v1beta1_observation import V1beta1Observation  # noqa: F401,E501
from kubeflow.katib.models.v1beta1_parameter_assignment import V1beta1ParameterAssignment  # noqa: F401,E501


class V1beta1OptimalTrial(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'best_trial_name': 'str',
        'observation': 'V1beta1Observation',
        'parameter_assignments': 'list[V1beta1ParameterAssignment]'
    }

    attribute_map = {
        'best_trial_name': 'bestTrialName',
        'observation': 'observation',
        'parameter_assignments': 'parameterAssignments'
    }

    def __init__(self, best_trial_name=None, observation=None, parameter_assignments=None):  # noqa: E501
        """V1beta1OptimalTrial - a model defined in Swagger"""  # noqa: E501

        self._best_trial_name = None
        self._observation = None
        self._parameter_assignments = None
        self.discriminator = None

        self.best_trial_name = best_trial_name
        if observation is not None:
            self.observation = observation
        self.parameter_assignments = parameter_assignments

    @property
    def best_trial_name(self):
        """Gets the best_trial_name of this V1beta1OptimalTrial.  # noqa: E501

        BestTrialName is the name of the best trial.  # noqa: E501

        :return: The best_trial_name of this V1beta1OptimalTrial.  # noqa: E501
        :rtype: str
        """
        return self._best_trial_name

    @best_trial_name.setter
    def best_trial_name(self, best_trial_name):
        """Sets the best_trial_name of this V1beta1OptimalTrial.

        BestTrialName is the name of the best trial.  # noqa: E501

        :param best_trial_name: The best_trial_name of this V1beta1OptimalTrial.  # noqa: E501
        :type: str
        """
        if best_trial_name is None:
            raise ValueError("Invalid value for `best_trial_name`, must not be `None`")  # noqa: E501

        self._best_trial_name = best_trial_name

    @property
    def observation(self):
        """Gets the observation of this V1beta1OptimalTrial.  # noqa: E501

        Observation for this trial  # noqa: E501

        :return: The observation of this V1beta1OptimalTrial.  # noqa: E501
        :rtype: V1beta1Observation
        """
        return self._observation

    @observation.setter
    def observation(self, observation):
        """Sets the observation of this V1beta1OptimalTrial.

        Observation for this trial  # noqa: E501

        :param observation: The observation of this V1beta1OptimalTrial.  # noqa: E501
        :type: V1beta1Observation
        """

        self._observation = observation

    @property
    def parameter_assignments(self):
        """Gets the parameter_assignments of this V1beta1OptimalTrial.  # noqa: E501

        Key-value pairs for hyperparameters and assignment values.  # noqa: E501

        :return: The parameter_assignments of this V1beta1OptimalTrial.  # noqa: E501
        :rtype: list[V1beta1ParameterAssignment]
        """
        return self._parameter_assignments

    @parameter_assignments.setter
    def parameter_assignments(self, parameter_assignments):
        """Sets the parameter_assignments of this V1beta1OptimalTrial.

        Key-value pairs for hyperparameters and assignment values.  # noqa: E501

        :param parameter_assignments: The parameter_assignments of this V1beta1OptimalTrial.  # noqa: E501
        :type: list[V1beta1ParameterAssignment]
        """
        if parameter_assignments is None:
            raise ValueError("Invalid value for `parameter_assignments`, must not be `None`")  # noqa: E501

        self._parameter_assignments = parameter_assignments

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(V1beta1OptimalTrial, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1OptimalTrial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
