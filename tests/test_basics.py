import unittest
import quantaq
import os
import sys
import pandas as pd

class SetupTestCase(unittest.TestCase):
    def setUp(self):
        # source the local dev token (only works on david's laptop)
        self.token = os.environ.get("QUANTAQ_APIKEY_DEV")
        self.api = quantaq.QuantAQ(token=self.token)

        # if testing on david's MBP, change the endpoint
        if sys.platform == "darwin":
            self.api.endpoint = "http://localhost:5000/api/"
    
    def tearDown(self):
        pass

    def test_manager(self):
        self.assertIsInstance(self.api, quantaq.QuantAQ)
        self.assertTrue(hasattr(self.api, "get_account"))
        self.assertTrue(hasattr(self.api, "get_devices"))
        self.assertEqual(self.api.endpoint, "http://localhost:5000/api/")

    def test_account(self):
        mngr = self.api
        self.assertEqual(self.api.endpoint, "http://localhost:5000/api/")

        account = mngr.get_account()
        self.assertIsInstance(account, quantaq.Account)
        self.assertIsNotNone(account.email)
        self.assertIsNotNone(account.username)
        self.assertIsNotNone(account.confirmed)
        self.assertIsNotNone(account.last_name)
        self.assertIsNotNone(account.first_name)
        self.assertIsNotNone(account.member_since)
    
    def test_device(self):
        mngr = self.api
        self.assertEqual(mngr.endpoint, "http://localhost:5000/api/")

        # return devices as json
        devices = mngr.get_devices(return_type="json")
        self.assertTrue(type(devices), list)

        # return devices as a dataframe
        devices = mngr.get_devices(return_type="dataframe")
        self.assertIsInstance(devices, pd.DataFrame)

        # return devices as objects
        devices = mngr.get_devices(return_type="object")
        for d in devices:
            self.assertIsInstance(d, quantaq.Device)
            self.assertIsNotNone(d.sn)
            self.assertIsNotNone(d.n_datapoints)
            self.assertIsNotNone(d.model)
            self.assertIsNotNone(d.url)

            d2 = quantaq.Device.get_object(sn=d.sn, token=self.api.token, endpoint=self.api.endpoint)
        
        # try updating a record
        city = d2.city
        self.assertNotEqual(city, "Delhi")
        d2.update(params=dict(city="Delhi"))
        self.assertEqual(d2.city, "Delhi")
        d2.update(params=dict(city=city))
        self.assertEqual(d2.city, city)

        # try posting a new device and then deleting the same device
        new_device = {
            'sn': "TMP-001",
            'model': "arisense_v200",
            'city': "Cambridge",
            'country': "US"
        }

        new = mngr.post_device(new_device)
        print (new)
        self.assertIsInstance(new, quantaq.Device)

        new.destroy()
    
    def test_data(self):
        mngr = self.api
        self.assertEqual(mngr.endpoint, "http://localhost:5000/api/")

        # get a device
        device = mngr.get_devices(return_type="object")
        device = device[0]
        self.assertIsInstance(device, quantaq.Device)

        # get normal data as json
        data = device.get_data(return_type='json', researcher=False)

        # get normal data as an object
        data = device.get_data(return_type='object', researcher=False)

        # get normal data as a dataframe
        data = device.get_data(return_type='dataframe', researcher=False)

        # get research data as json
        data = device.get_data(return_type='json', researcher=True)

        # get research data as an object
        data = device.get_data(return_type='object', researcher=True)

        # get research data as a dataframe
        data = device.get_data(return_type='dataframe', researcher=True)




