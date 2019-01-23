from index import sample_to_test
import unittest

class mytest(unittest.TestCase):
  def test_1_otherfilefunction(self):
    self.assertEqual(sample_to_test(), "sample") # this should pass
  def test_2_otherfilefunction(self):
    self.assertNotEqual(sample_to_test(), "Sample") # this should pass    

if __name__ == '__main__':
  unittest.main()
