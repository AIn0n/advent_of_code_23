from ranges import Range

def test_constructor_start_end_len_parameters():
    r = Range(79, 14)
    
    assert r.start == 79
    assert r._len == 14
    assert r.end == 92

