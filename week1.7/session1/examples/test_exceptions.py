import pytest

# If you want to test for a specific exception message

def myfunc():
    raise ValueError("Exception 123 raised")

def test_match():
    with pytest.raises(ValueError) as excinfo:
        myfunc()
    assert str(excinfo.value) == "Exception 123 raised"

# If you want to check that an exact exception type is raised

def foo():
    raise RuntimeError

def test_foo_runtime_error():
    with pytest.raises(RuntimeError) as excinfo:
        foo()
    # Next line ensures that test can only pass if RuntimeError is
    # raised, and not an instance of one of its subclasses
    assert excinfo.type is RuntimeError
