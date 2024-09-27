import unittest
from src.lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    def test_correct_answer(self):
        event = {
            'request': {
                'privateChallengeParameters': {'secretCode': 'internal_code'},
                'challengeAnswer': 'internal_code'
            },
            'response': {}
        }

        expected_response = {
            'request': {
                'privateChallengeParameters': {'secretCode': 'internal_code'},
                'challengeAnswer': 'internal_code'
            },
            'response': {
                'answerCorrect': True
            }
        }

        result = lambda_handler(event, None)
        self.assertEqual(result, expected_response)

    def test_incorrect_answer(self):
        event = {
            'request': {
                'privateChallengeParameters': {'secretCode': 'internal_code'},
                'challengeAnswer': 'wrong_code'
            },
            'response': {}
        }

        expected_response = {
            'request': {
                'privateChallengeParameters': {'secretCode': 'internal_code'},
                'challengeAnswer': 'wrong_code'
            },
            'response': {
                'answerCorrect': False
            }
        }

        result = lambda_handler(event, None)
        self.assertEqual(result, expected_response)

if __name__ == '__main__':
    unittest.main()