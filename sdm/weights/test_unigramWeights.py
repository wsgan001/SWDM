from unittest import TestCase

import sdm.weights.unigram_weights
from parameters.parameters import Parameters


class TestUnigramWeights(TestCase):
    def setUp(self):
        self.parameters = Parameters()
        self.parameters.params["repo_dir"] = '../../index/test_files/index'
        self.parameters.params['feature_parameters'] = {}
        self.parameters.params['feature_parameters']['UnigramWeights'] = {
            "norm_term_count": {
            },
            "norm_document_count": {
            },
            "unigrams_cosine_similarity_with_orig": {
            }
        }
        self.parameters.params['features_weights'] = {}
        self.parameters.params['features_weights']['UnigramWeights'] = {
            "norm_term_count": 0.33,
            "norm_document_count": 0.33,
            "unigrams_cosine_similarity_with_orig": 0.33
        }

    def test_compute_weight(self):
        unigram_nearest_neighbor = [('hello', 1), ('world', 0.65)]

        unigram_weights = sdm.weights.unigram_weights.UnigramWeights(self.parameters)

        term_dependent_feature_parameters = {
            "unigram_nearest_neighbor": unigram_nearest_neighbor,
        }
        res = unigram_weights.compute_weight("world", term_dependent_feature_parameters)
        expected_res = 0.21450000000000002
        self.assertEqual(res, expected_res)