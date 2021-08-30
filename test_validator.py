#####################
# Imports           #
#####################

import unittest
from validator import Validator

#####################
# Classes           #
#####################

class TestValidator(unittest.TestCase):

    def test_check_int(self):
        '''checks if the field is an integer'''

        # Assume
        field = "daily_limit"
        value = 10
        validator = Validator()

        # Action
        result = validator.check_int(field, value)

        # Assert
        self.assertTrue(result)

    def test_check_float(self):
        '''checks if the field is a float'''

        # Assume
        field = "percent_change"
        value = 10.0
        validator = Validator()

        # Action
        result = validator.check_float(field, value)

        # Assert
        self.assertTrue(result)

    def test_check_string(self):
        '''checks if the field is a string'''

        # Assume
        field = "symbol"
        value = "AAPL"
        validator = Validator()

        # Action
        result = validator.check_string(field, value, 10)

        # Assert
        self.assertTrue(result)
        
