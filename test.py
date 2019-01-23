import unittest

def sample_function():
  return "hello"

class mytest(unittest.TestCase):
  def sampletest(self):
    self.assertTrue(sample_function(), "hello")
    self.assertEqual("hello", "hello")

if __name__ == '__main__':
  unittest.main()
