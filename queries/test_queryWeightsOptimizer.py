from unittest import TestCase

from mock import MagicMock

from parameters.parameters import Parameters
from queries.queryWeightsOptimizer import QueryWeightsOptimizer


class TestQueryWeightsOptimizer(TestCase):
    def setUp(self):
        self.parameters = Parameters()
        self.parameters.params["repo_dir"] = '../index/test_files/index'
        self.parameters.params["word2vec"] = {}
        self.parameters.params["word2vec"]["threshold"] = 0.6
        self.parameters.params["window_size"] = {}
        self.parameters.params["window_size"]["#od"] = 4
        self.parameters.params["window_size"]["#uw"] = 17
        self.parameters.params['feature_parameters'] = {}
        self.parameters.params['feature_parameters']['UnigramWeights'] = {
            "norm_term_count": {
            },
            "norm_document_count": {
            },
            "unigrams_cosine_similarity_with_orig": {
            }
        }
        self.parameters.params['feature_parameters']['UnorderedBigramWeights'] = {
            "uw_expression_norm_count": {
                "window_size": 17
            },
            "uw_expression_norm_document_count": {
                "window_size": 17
            }
        }
        self.parameters.params['feature_parameters']['OrderedBigramWeights'] = {
            "od_expression_norm_count": {
                "window_size": 17
            },
            "od_expression_norm_document_count": {
                "window_size": 17
            }
        }
        self.parameters.params['features_weights'] = {}
        self.parameters.params['features_weights']['UnigramWeights'] = {
            "norm_term_count": 0.33,
            "norm_document_count": 0.33,
            "unigrams_cosine_similarity_with_orig": 0.33
        }
        self.parameters.params['features_weights']['UnorderedBigramWeights'] = {
            "uw_expression_norm_count": 0.33,
            "uw_expression_norm_document_count": 0.33,
            "bigrams_cosine_similarity_with_orig": 0.33
        }
        self.parameters.params['features_weights']['OrderedBigramWeights'] = {
            "od_expression_norm_count": 0.33,
            "od_expression_norm_document_count": 0.33,
            "bigrams_cosine_similarity_with_orig": 0.33
        }
        self.parameters.params["word2vec"] = {"threshold": 0.6, "n_max": 5}

        self.query_weights_optimizer = QueryWeightsOptimizer(self.parameters)

    def test_update_nested_map(self):
        d = {'m': {'d': {'v': {'w': 1}}}}
        res = self.query_weights_optimizer.update_nested_dict(d, 10, ['m', 'd', 'v', 'w'])
        expected_res = {'m': {'d': {'v': {'w': 10}}}}
        self.assertEqual(res, expected_res)

        res = self.query_weights_optimizer.update_nested_dict(d, 10, ['m', 'd', 'v', 'z'])
        expected_res = {'m': {'d': {'v': {'w': 1, 'z': 10}}}}
        self.assertEqual(res, expected_res)

        res = self.query_weights_optimizer.update_nested_dict(d, 10, ['m', 'd', 'l'])
        expected_res = {'m': {'d': {'v': {'w': 1}, 'l': 10}}}
        self.assertEqual(res, expected_res)

    def test_obtain_best_parameter_set(self):
        self.parameters.params["optimization"] = [
            {"param_name": ["expansion_coefficient"], "initial_point": 0, "final_point": 1, "step_size": 0.1},
            {"param_name": ["word2vec", "threshold"], "initial_point": 0, "final_point": 1, "step_size": 0.1}
        ]
        self.parameters.params["optimized_parameters_file_name"] = "test_files/optimized_parameters.json"

        self.parameters.params["expansion_coefficient"] = 0.05
        query_weights_optimizer = QueryWeightsOptimizer(self.parameters)

        query_weights_optimizer.gen_queries = MagicMock(return_value=None)
        query_weights_optimizer.evaluate_queries = MagicMock(return_value=0.25)
        eval_res_dict = query_weights_optimizer.obtain_best_parameter_set()

        self.assertEqual(eval_res_dict, 0.25)