#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    base_model = BaseModel()
    base_model1 = BaseModel()

    def test_instance(self):
        self.assertIsInstance(TestBaseModel.base_model, BaseModel)

    def test_id_uniq(self):
        self.assertNotEqual(TestBaseModel.base_model.id,
                            TestBaseModel.base_model1.id)

    def test_id_string(self):
        self.assertEqual(type(TestBaseModel.base_model.id), str)

    def test_to_dict(self):
        self.assertNotEqual(TestBaseModel.base_model.to_dict(),
                            TestBaseModel.base_model.__dict__)

    def test_created_at(self):
        self.assertNotEqual(TestBaseModel.base_model.created_at,
                            TestBaseModel.base_model1.created_at)
