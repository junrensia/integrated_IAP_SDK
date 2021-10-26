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
from ICA_SDK.models.lane_by_read_sequencing_stats_response import LaneByReadSequencingStatsResponse  # noqa: E501
from ICA_SDK.rest import ApiException

class TestLaneByReadSequencingStatsResponse(unittest.TestCase):
    """LaneByReadSequencingStatsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LaneByReadSequencingStatsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.lane_by_read_sequencing_stats_response.LaneByReadSequencingStatsResponse()  # noqa: E501
        if include_optional :
            return LaneByReadSequencingStatsResponse(
                lane_number = 56, 
                read_number = 56, 
                tile_count = 56, 
                density = 1.337, 
                density_deviation = 1.337, 
                percent_pf = 1.337, 
                percent_pf_deviation = 1.337, 
                phasing = 1.337, 
                pre_phasing = 1.337, 
                reads = 56, 
                reads_pf = 56, 
                percent_gt_q30 = 1.337, 
                percent_gt_q30_last10_cycles = 1.337, 
                _yield = 1.337, 
                min_cycle_called = 56, 
                max_cycle_called = 56, 
                percent_aligned = 1.337, 
                percent_aligned_deviation = 1.337, 
                error_rate = 1.337, 
                error_rate_deviation = 1.337, 
                error_rate35 = 1.337, 
                error_rate35_deviation = 1.337, 
                error_rate50 = 1.337, 
                error_rate50_deviation = 1.337, 
                error_rate75 = 1.337, 
                error_rate75_deviation = 1.337, 
                error_rate100 = 1.337, 
                error_rate100_deviation = 1.337, 
                intensity_cycle1 = 1.337, 
                intensity_cycle1_deviation = 1.337, 
                min_cycle_error = 56, 
                max_cycle_error = 56, 
                phasing_slope = 1.337, 
                phasing_offset = 1.337, 
                pre_phasing_slope = 1.337, 
                pre_phasing_offset = 1.337, 
                percent_no_calls = 1.337, 
                cluster_density = 1.337, 
                occupancy = 1.337
            )
        else :
            return LaneByReadSequencingStatsResponse(
        )

    def testLaneByReadSequencingStatsResponse(self):
        """Test LaneByReadSequencingStatsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
