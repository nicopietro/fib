from platform import machine

from test_merge import test_merge_max_mapping, test_merge_max_mapping_case_2


def merge_max_mappings(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    if len(a) > len(b):
        merged = a.copy()
        other = b
    else:
        merged = b.copy()
        other = a
    for key in other:
        if key in merged:
            merged[key] = max(merged[key], other[key])
        else:
            merged[key] = other[key]
    return merged