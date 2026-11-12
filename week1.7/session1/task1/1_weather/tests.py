from weather import comfort_level

def test_cold():
    assert comfort_level(15) == "OK"