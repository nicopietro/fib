from merge_dict import merge_max_mappings


def test_merge_max_mapping():
    dict1 = {'bananas': 7, 'apples': 3, 'pears': 14}
    dict2 = {'bananas': 3, 'apples': 6, 'grapes': 9}
    result = merge_max_mappings(dict1, dict2)
    assert result == {'bananas': 7, 'apples': 6, 'pears': 14, 'grapes': 9}

def test_merge_max_mapping_case_2():
    dict1 = {}
    dict2 = {'bananas': 3, 'apples': 6, 'grapes': 9}
    result = merge_max_mappings(dict1, dict2)
    assert result == {'bananas': 3, 'apples': 6, 'grapes': 9}