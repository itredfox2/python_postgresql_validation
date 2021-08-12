#####################################################################################
#                                                                                   #
# Overview                                                                          #
#                                                                                   #
#    postgresql_validate.py --schema=postgresql_schema.json                         #
#                                                                                   #
# Description                                                                       #
#                                                                                   #
#    This script is used to validate the attributes of fields                       #
#    in a postgresql database, as specificed in the provided                        #
#    database schema.                                                               #
#                                                                                   #
# Implementation                                                                    #
#                                                                                   #
#    date        07-04-2021                                                         #
#    version     1.0.0                                                              #
#                                                                                   #
#####################################################################################

#####################
# Imports           #
#####################

import argparse
import collections
import datetime
import json
import logging
import psycopg2
import re

#####################
# Connection        #
#####################

db_name = ""
db_host = ""
db_port = ""
db_user = ""
db_pass = ""

#####################
# Arguments         #
#####################

parser = argparse.ArgumentParser()

parser.add_argument('--schema', '-s', required=True, help='database schema')

args = parser.parse_args()

#####################
# Logging           #
#####################

log_date = datetime.date.today()

log_file = "postgresql_validate_{}.log".format(log_date)

logging.basicConfig(format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s", level=logging.INFO, filename=log_file)

#####################
# Functions         #
#####################

def import_schema(file_name):
    '''imports database schema'''

    data = None

    try:
        with open(file_name) as contents:
		
            data = json.load(contents, object_pairs_hook=collections.OrderedDict)

    except (IOError) as E:
	
        print("Error: {}".format(E))
	
    return data

def create_connection():
    '''creates database connection'''

    connection = None

    try:
        logging.info("Opening connection to {}:{}".format(db_host, db_port))
	
        connection = psycopg2.connect(
    	    dbname        = db_name,
            host          = db_host,
            user          = db_user,
            password      = db_pass,
            port          = db_port
        )
	
        logging.info("Connection established.")

    except (Exception, psycopg2.Error) as E:
	
        logging.error(E)

    return connection

def execute_query(connection, query):
    '''executes database query'''

    results = None

    try:
        cursor = connection.cursor()
	
        cursor.execute(query)
	
        results = cursor.fetchall()
	
        cursor.close()

    except (Exception, psycopg2.Error) as E:
	
        logging.error(E)

    return results

def close_connection(connection):
    '''closes database connection'''

    logging.info("Closing connection to {}:{}".format(db_host, db_port))

    try:
        connection.close()
	
        logging.info("Connection closed.")

    except(Exception, psycopg2.Error) as E:
	
        logging.error(E)

def check_int(field, value):
    '''checks if the field is an integer'''

    if isinstance(value, int):
        pass

    else:
        value_error(field, value)

def check_string(field, value, length):
    '''checks if the field length exceeds the expected length of characters'''

    if len(value) <= length:
        pass

    else:
        value_error(field, value)

def check_timestamp(field, value):
    '''checks if the field has a timestamp value'''

    if isistance(value, datatime.datetime):
        pass

    else:
        value_error(field, value)

def value_error(field, value):
    '''logs as error if a value does not match the field specifications as listed in the database schema'''

    logging.error("invalid value detected for column {}: \'{}\'".format(field, value))

#####################
# Main              #
#####################

def main():

    logging.info("Starting validation of postgresql database.")

    db_conn = create_connection()

    schema = import_schema(args.schema)

    for table in schema:

        logging.info("Running checks for table {}".format(table))

        columns = list(schema[table])

        query "SELECT * FROM {} ;".format(table)

        results = execute_query(db_conn, query)

        for row_index, row in enumerate(results):

            for col_index, value in enumerate(list(row)):

                try:
                    col = columns[col_index]

                    if value is None:

                        if schema[table][col]["required"] == "yes":
				
                            value_error(col, value)

                    else:
			
                        if schema[table][col]["type"] == "int":
				
                            check_int(col, value)

                        elif schema[table][col]["type"] == "varchar":
				
                            length = int(schema[table][col]["length"])
			
                            check_string(col, value, length)

                        elif schema[table][col]["type"] == "timestamp":
				
                            check_timestamp(col, value)

                except (Exception, IndexError) as E:
			
                    logging.error(E)
		
                    pass

    close_connection(db_conn)

    logging.info("Validation complete.")

#####################
# Start             #
#####################

if __name__ == '__main__':
    main()

	
