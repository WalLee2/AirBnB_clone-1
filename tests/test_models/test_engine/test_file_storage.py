#!/usr/bin/python3
import unittest
import os.path
from datetime import datetime
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.__init__ import storage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class Test_FileStorage(unittest.TestCase):
    """
    Test the file storage class
    """

    def setUp(self):
        """Test storage"""
        self.cli = HBNBCommand()
        self.store = FileStorage()
        test_args = {'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900)}
        self.model = BaseModel(test_args)

        self.test_len = 0
        if os.path.isfile("file.json"):
            self.test_len = len(self.store.all())

#    def tearDown(self):
#        import os
#        if os.path.isfile("file.json"):
#            os.remove('file.json')

    def test_all(self):
        """Test all storages"""
        self.assertEqual(len(self.store.all()), self.test_len)

    def test_new(self):
        """test new storages"""
        self.assertEqual(len(self.store.all()), self.test_len)
        self.model.save()
        self.assertEqual(len(self.store.all()), self.test_len + 1)
        a = BaseModel()
        a.save()
        self.assertEqual(len(self.store.all()), self.test_len + 2)

        self.cli.do_destroy("BaseModel f519fb40-1f5c-458b-945c-2ee8eaaf4900")
        self.cli.do_destroy("BaseModel " + a.id)

    def test_save(self):
        """Test saving into storage"""
        self.test_len = len(self.store.all())
        a = BaseModel()
        a.save()
        self.assertEqual(len(self.store.all()), self.test_len + 1)
        b = User()
        self.assertNotEqual(len(self.store.all()), self.test_len + 2)
        b.save()
        self.assertEqual(len(self.store.all()), self.test_len + 2)

        self.cli.do_destroy("BaseModel " + a.id)
        self.cli.do_destroy("User " + b.id)

    def test_reload(self):
        pass

if __name__ == "__main__":
    unittest.main()
