#!/usr/bin/python3
"""
Tests for State Class
"""
import os
import pep8
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Test for State Class
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup State Class
        """
        cls.state = State()
        cls.state.name = "Cundinamarca"

    @classmethod
    def teardown(cls):
        """
        Delete State Class
        """
        del cls.state
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_State(self):
        """
        Check pep8
        """
        psg = pep8.StyleGuide(quiet=True)
        model = "models/state.py"
        tests = "tests/test_models/test_state.py"
        results = psg.check_files([model, tests])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        Check documentation
        """
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.__init__.__doc__)

    def test_attributes(self):
        """
        Check State attributes
        """
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue(hasattr(State, "name"))
        self.assertEqual(type(self.state.name), str)

    def test_methods(self):
        """
        Check State and Basemodel methods
        """
        self.assertTrue(hasattr(State, "__init__"))
        self.assertTrue(hasattr(State, "__str__"))
        self.assertTrue(hasattr(State, "save"))
        self.assertTrue(hasattr(State, "to_dict"))

    def test_init(self):
        """
        Check object as instance of State
        """
        self.assertTrue(isinstance(self.state, State))

    def test_str(self):
        """
        Check string representation of State object
        """
        ste_str = str(self.state)
        self.assertEqual(True, "[State] ({})".format(self.state.id) in ste_str)
        self.assertEqual(True, "name" in ste_str)
        self.assertEqual(True, "created_at" in ste_str)
        self.assertEqual(True, "updated_at" in ste_str)
        self.assertEqual(True, "datetime.datetime" in ste_str)

    def test_save(self):
        """
        Check save method
        """
        self.state.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """
        Check dictionary method
        """
        state_dict = self.state.to_dict()
        self.assertEqual(self.state.__class__.__name__, 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)
        self.assertEqual(type(state_dict), dict)

if __name__ == "__main__":
    unittest.main()
