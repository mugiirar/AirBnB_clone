import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
import models
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        # Test if "create" command creates a new instance of BaseModel
        self.console.do_create("BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(models.storage.all()["BaseModel." + output])

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        # Test if "show" command displays the correct instance
        obj = models.BaseModel()
        obj_id = obj.id
        self.console.do_show(f"BaseModel {obj_id}")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(str(obj), output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        # Test if "destroy" command deletes the correct instance
        obj = models.BaseModel()
        obj_id = obj.id
        self.console.do_destroy(f"BaseModel {obj_id}")
        self.assertIsNone(models.storage.all().get(f"BaseModel.{obj_id}"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        # Test if "all" command lists all instances
        self.console.do_all("BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertIn("BaseModel", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        # Test if "update" command updates an instance
        obj = models.BaseModel()
        obj_id = obj.id
        self.console.do_update(f"BaseModel {obj_id} name John")
        self.assertEqual(obj.name, "John")

if __name__ == '__main__':
    unittest.main()

