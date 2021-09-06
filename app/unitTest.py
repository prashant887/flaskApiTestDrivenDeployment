import unittest
from webserver import app
import json


class MyTestCase(unittest.TestCase):
    test = app.test_client()

    def test_home(self):
        res = self.test.get("/", content_type='application/json')
        status_code = res.status_code
        data = res.json
        self.assertEqual(status_code, 200)
        self.assertEqual(data, 'Home')

    def test_getuser(self):
        res = self.test.get("/credentials", content_type='application/json')
        status_code = res.status_code
        data = res.json
        user = data.get('user')
        pwd = data.get('pwd')
        self.assertEqual(status_code, 200)
        self.assertEqual(user, 'admin')
        self.assertEqual(pwd, 'admin@123')

    def test_sch(self):
        data = {"day": "Sunday", "tm": 3}
        res = self.test.post("/consume", content_type='application/json', data=json.dumps(data))

        status_code = res.status_code
        data = res.json
        sts = data.get('sts')
        self.assertEqual(status_code, 200)
        self.assertEqual(sts, 'NoRun')

        data = {"day": "Monday", "tm": 4}
        res = self.test.post("/consume", content_type='application/json', data=json.dumps(data))

        status_code = res.status_code
        data = res.json
        sts = data.get('sts')
        self.assertEqual(status_code, 200)
        self.assertEqual(sts, 'Run')


if __name__ == '__main__':
    unittest.main()
