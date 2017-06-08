from unittest import TestCase

import features.collection
from parameters.parameters import Parameters

__author__ = 'Saeid Balaneshin-kordan'
__email__ = "saeid@wayne.edu"
__date__ = 11 / 21 / 16


class TestCollection(TestCase):
    def setUp(self):
        self.parameters = Parameters()
        self.parameters.params["repo_dir"] = '../index/test_files/index'
        self.features = features.collection.Collection(self.parameters)
        self.feature_parameters = {
            "uw_expression_count": {
                "window_size": 17
            },
            "od_expression_count": {
                "window_size": 4
            },
            "uw_expression_document_count": {
                "window_size": 4
            },
            "od_expression_document_count": {
                "window_size": 4
            },
        }

    def test_uw_expression_count(self):
        self.assertEqual(self.features.uw_expression_count("SAMPSON Dog",
                                                           self.feature_parameters["uw_expression_count"]), 2)

    def test_od_document_expression_count(self):
        self.assertEqual(self.features.od_expression_document_count(
            "SAMPSON True", self.feature_parameters["od_expression_document_count"]), 1)

    def test_uw_document_expression_count(self):
        self.assertEqual(self.features.uw_expression_document_count(
            "SAMPSON True", self.feature_parameters["uw_expression_document_count"]), 1)

    def test_term_count(self):
        self.assertEqual(self.features.term_count("dog", {}), 2)

    def test_document_count(self):
        self.assertEqual(self.features.document_count("dog", {}), 1)

    def test_uw_expression_norm_count(self):
        self.assertEqual(self.features.uw_expression_norm_count(
            "SAMPSON Dog", self.feature_parameters["uw_expression_count"]), 5.497168225293202)

    def test_od_expression_norm_document_count(self):
        self.assertEqual(self.features.od_expression_norm_document_count(
            "SAMPSON True", self.feature_parameters["od_expression_document_count"]), 0.40546510810816444)

    def test_uw_document_expression_norm_count(self):
        self.assertEqual(self.features.uw_expression_norm_document_count(
            "SAMPSON True", self.feature_parameters["uw_expression_document_count"]), 0.40546510810816444)

    def test_norm_term_count(self):
        self.assertEqual(self.features.norm_term_count("dog", {}), 5.497168225293202)

    def test_norm_document_count(self):
        self.assertEqual(self.features.norm_document_count("dog", {}), 0.40546510810816444)
