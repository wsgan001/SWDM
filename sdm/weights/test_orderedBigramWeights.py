from unittest import TestCase

import sdm.weights.ordered_bigram_weights
from parameters.parameters import Parameters


class TestOrderedBigramWeights(TestCase):
    def setUp(self):
        self.parameters = Parameters()
        self.parameters.params["repo_dir"] = '../../index/test_files/index'
        self.parameters.params['expansion_coefficient'] = 0.1
        self.parameters.params['feature_parameters'] = {}
        self.parameters.params['feature_parameters']['OrderedBigramWeights'] = {
            "od_expression_norm_count": {
                "window_size": 4
            },
            "od_expression_norm_document_count": {
                "window_size": 4
            }
        }
        self.parameters.params['features_weights'] = {}
        self.parameters.params['features_weights']['OrderedBigramWeights'] = {
            "od_expression_norm_count": 0.33,
            "od_expression_norm_document_count": 0.33,
            "bigrams_cosine_similarity_with_orig": 0.33
        }

    def test_compute_weight(self):
        unigram_nearest_neighbor_1 = [('hello', 1), ('world', 0.65)]
        unigram_nearest_neighbor_2 = [('how', 1), ('are', 0.8), ('you', 0.74)]

        ordered_bigram_weights = sdm.weights.ordered_bigram_weights.OrderedBigramWeights(self.parameters)

        term_dependent_feature_parameters = {
            "unigram_nearest_neighbor_1": unigram_nearest_neighbor_1,
            "unigram_nearest_neighbor_2": unigram_nearest_neighbor_2
        }
        res = ordered_bigram_weights.compute_weight("world are", term_dependent_feature_parameters)
        expected_res = 0.023925000000000005
        self.assertEqual(res, expected_res)
