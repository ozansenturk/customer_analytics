import unittest
from flask import current_app
from app import create_app
from app.api import cohort
import os
import pandas as pd

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_reduce_online_dataset(self):

        filename = os.path.join(current_app.config['UPLOAD_FOLDER'], "online.csv")

        retention = pd.read_csv(filename)

        retention = retention.iloc[:1000,]

        filename_reduced = os.path.join(
            current_app.config['UPLOAD_FOLDER'], "online_reduced.csv")
        retention.to_csv(filename_reduced, encoding='utf-8')

        self.assertTrue(retention is not None, "retention should not be null")

    def test_calculate_retention(self):

        filename = os.path.join(current_app.config['UPLOAD_FOLDER'], "online.csv")

        retention = cohort.calculate_retention(filename
                                               ,"InvoiceDate")
        self.assertTrue(retention is not None, "retention should not be null")

