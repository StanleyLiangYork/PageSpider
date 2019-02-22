from utilities.database_utilities import create_database
import os


def test_create_database():
    os.chdir(os.path.dirname(__file__))
    path = os.path.join(os.getcwd(), "words.db")
    create_database(database_path=path)