import importlib
importlib.import_module(index)
import unittest

def sample_function():
  return "hello"

class mytest(unittest.TestCase):
  def test1(self):
    self.assertEqual("hello", "hello")
  def test2(self):
    self.assertEqual(index.sample_to_test(), "sample")

if __name__ == '__main__':
  unittest.main()
