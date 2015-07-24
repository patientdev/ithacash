import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'PRODUCTION_DB_PASSWORD'), 'r') as password_file:
    PRODUCTION_DATABASE_PASSWORD = password_file.read()

