def test_coord_plane(coord1, coord2, x_coord expected):
    from coord_place import line_test 
    answer = line_test(coord1, coord2, x_coord)
    assert answer == expected 
    
   