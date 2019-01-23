from index import sample_to_test
import unittest

class mytest(unittest.TestCase):
  def test_otherfilefunction(self):
    self.assertEqual(sample_to_test(), "sample") # this should pass
    self.assertEqual(sample_to_test(), "Sample") # this should not pass    

if __name__ == '__main__':
  unittest.main()
