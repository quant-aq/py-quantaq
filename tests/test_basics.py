import unittest
import quantaq
import os
import sys
import pandas as pd

class SetupTestCase(unittest.TestCase):
    def setUp(self):
        # source the local dev token (only works on david's laptop)
        self.token = os.environ.get("QUANTAQ_APIKEY_DEV")
        self.api = quantaq.legacy.QuantAQ(token=self.token)

        # if testing on david's MBP, change the endpoint
        if sys.platform == "darwin":
            self.api.endpoint = "http://localhost:5000/api/"
    
    def tearDown(self):
        pass

    def test_account(self):
        mngr = self.api
        self.assertEqual(mngr.endpoint, "http://localhost:5000/api/")

        # return the account as json
        account = mngr.get_account()
        self.assertIsNotNone(account["confirmed"])
        self.assertIsNotNone(account["username"])
        self.assertIsNotNone(account["email"])
    
    def test_devices(self):
        mngr = self.api
        self.assertEqual(mngr.endpoint, "http://localhost:5000/api/")

        # get devices as a list
        devices = mngr.get_devices()
        self.assertTrue(type(devices), list)

        # get devices as a dataframe
        devices = mngr.get_devices(return_type='dataframe')
        self.assertIsInstance(devices, pd.DataFrame)

        # try limiting to just one result
        devices = mngr.get_devices(params=dict(limit=1))
        self.assertEqual(len(devices), 1)

        # get just one device
        device = mngr.get_device(sn=devices[0]["sn"])
        self.assertIsNotNone(device["sn"])
        self.assertIsNotNone(device["url"])

        # update a device
        old_city = device["city"]
        new_city = "New City"

        device = mngr.update_device(sn=device["sn"], params=dict(city=new_city))
        self.assertEqual(device["city"], new_city)

        with self.assertRaises(NotImplementedError):
            mngr.add_device(params=dict())
        
        with self.assertRaises(NotImplementedError):
            mngr.delete_device(sn="")

    def test_calmodels(self):
       pass
    
    def test_data(self):
        mngr = self.api
        self.assertEqual(mngr.endpoint, "http://localhost:5000/api/")

        # get the devices
        devices = mngr.get_devices()
        sn = devices[0]["sn"]

        # get a list of all cleaned data in json format
        data = mngr.get_data(sn=sn, return_type='json', final_data=True)
        self.assertTrue(type(data), list)

        # get a list of all cleaned data in dataframe format
        data = mngr.get_data(sn=sn, return_type='dataframe', final_data=True)
        self.assertIsInstance(data, pd.DataFrame)

        # get a list of all raw data in json format
        data = mngr.get_data(sn=sn, return_type='json', final_data=False)
        self.assertTrue(type(data), list)

        # get a list of all raw data as a dataframe
        data = mngr.get_data(sn=sn, return_type='dataframe', final_data=False)
        self.assertIsInstance(data, pd.DataFrame)

        with self.assertRaises(NotImplementedError):
            mngr.add_data()

        with self.assertRaises(NotImplementedError):
            mngr.update_data("", 1)

        with self.assertRaises(NotImplementedError):
            mngr.delete_data("", 1)

    def test_logs(self):
        mngr = self.api
        self.assertEqual(mngr.endpoint, "http://localhost:5000/api/")

        # get a device
        devices = mngr.get_devices()
        sn = devices[0]["sn"]

        # get a list of all logs in json format
        data = mngr.get_logs(sn=sn, return_type='json')
        self.assertTrue(type(data), list)

        # get a list of all cleaned data in dataframe format
        data = mngr.get_logs(sn=sn, return_type='dataframe')
        self.assertIsInstance(data, pd.DataFrame)
    
    def test_metadata(self):
        pass
    
    def test_users(self):
        pass
