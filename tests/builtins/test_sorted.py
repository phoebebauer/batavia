from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class SortedTests(TranspileTestCase):
    pass


class BuiltinSortedFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["sorted"]

    not_implemented = [
        'test_bool',
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_dict',
        'test_float',
        'test_frozenset',
        'test_int',
        'test_none',
        'test_set',
        'test_str',
        'test_tuple',
    ]
