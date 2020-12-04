# coding: utf-8

"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import illumina_iap_sdk
from illumina_iap_sdk.models.delivery_target import DeliveryTarget  # noqa: E501
from illumina_iap_sdk.rest import ApiException

class TestDeliveryTarget(unittest.TestCase):
    """DeliveryTarget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeliveryTarget
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = illumina_iap_sdk.models.delivery_target.DeliveryTarget()  # noqa: E501
        if include_optional :
            return DeliveryTarget(
                aws_sns_topic = illumina_iap_sdk.models.delivery_target_aws_sns_topic.DeliveryTargetAwsSnsTopic(
                    topic_arn = '0', ), 
                aws_sqs_queue = illumina_iap_sdk.models.delivery_target_aws_sqs_queue.DeliveryTargetAwsSqsQueue(
                    queue_url = '0', ), 
                workflow_run_launch = illumina_iap_sdk.models.delivery_target_workflow_run_launch.DeliveryTargetWorkflowRunLaunch(
                    id = '0', 
                    version = '0', 
                    name = '0', 
                    input = illumina_iap_sdk.models.input.input(), )
            )
        else :
            return DeliveryTarget(
        )

    def testDeliveryTarget(self):
        """Test DeliveryTarget"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
