import pytest

# Create your tests here.
def test_example():
  assert 1 == 1

def test_assert_json():
  assert {
    "result": [{"name": "nhat"},2,3]
  } == {
    "result": [{"name": "nhat"},2,3]
  }
