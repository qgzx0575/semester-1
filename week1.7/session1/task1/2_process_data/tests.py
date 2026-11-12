from process_data import process_data

def tests():
    assert process_data([]) == None
    assert process_data([1]) == 1
    assert process_data([1,2,3]) == 6