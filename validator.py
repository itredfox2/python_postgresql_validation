#####################
# Imports           #
#####################

import datetime
import logging

#####################
# Logging           #
#####################

log_date = datetime.date.today()

log_file = "postgresql_validate_{}.log".format(log_date)

logging.basicConfig(format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s", level=logging.INFO, filename=log_file)

#####################
# Classes           #
#####################

class Validator:

    def check_int(self, field, value):
        '''checks if the field is an integer'''

        if isinstance(value, int):
            return True

        else:
            self.value_error(field, value)
            return False

    def check_float(self, field, value):
        '''checks if the field is an integer'''

        if isinstance(value, float):
            return True

        else:
            self.value_error(field, value)
            return Error

    def check_string(self, field, value, length):
        '''checks if the field length exceeds the expected length of characters'''

        if len(value) <= length:
            return True

        else:
            self.value_error(field, value)
            return False

    def value_error(self, field, value):
        '''logs as error if a value does not match the field specifications as listed in the database schema'''

        logging.error("invalid value detected for column {}: \'{}\'".format(field, value))
