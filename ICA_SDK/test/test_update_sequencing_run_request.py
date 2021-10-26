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

import ICA_SDK
from ICA_SDK.models.update_sequencing_run_request import UpdateSequencingRunRequest  # noqa: E501
from ICA_SDK.rest import ApiException

class TestUpdateSequencingRunRequest(unittest.TestCase):
    """UpdateSequencingRunRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateSequencingRunRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.update_sequencing_run_request.UpdateSequencingRunRequest()  # noqa: E501
        if include_optional :
            return UpdateSequencingRunRequest(
                run_name = '0', 
                description = '0', 
                prep_kit_info = ICA_SDK.models.sequencing_run_prep_kit_info.SequencingRunPrepKitInfo(
                    library_prep_kit_names = '0', 
                    num_samples = 56, 
                    lanes = [
                        ICA_SDK.models.lane_prep_kit_info.LanePrepKitInfo(
                            lane_number = 56, 
                            kits = [
                                ICA_SDK.models.library_prep_kit_and_index_adapter_kit_name.LibraryPrepKitAndIndexAdapterKitName(
                                    library_prep_kit_name = '0', 
                                    index_adapter_kit_name = '0', )
                                ], )
                        ], ), 
                flow_cell_barcode = '0', 
                input_container_identifier = '0', 
                consumables = None, 
                sample_sheet_name = '0', 
                is_favorite = True, 
                acl = [
                    '0'
                    ]
            )
        else :
            return UpdateSequencingRunRequest(
        )

    def testUpdateSequencingRunRequest(self):
        """Test UpdateSequencingRunRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
