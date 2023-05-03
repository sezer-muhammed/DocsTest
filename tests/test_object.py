import pytest

from DocsTest.Objects import BaseObject


@pytest.mark.parametrize(
    'params, expected_values, expected_exception',
    [
        # Test case 1: Valid parameters
        ({
            'name': 'test',
            'object_type': 'test',
            'age': 1,
            'missing_age': 1,
            'position_x': 1.0,
            'position_y': 1.0,
            'position_z': 1.0,
            'rotation_x': 1.0,
            'rotation_y': 1.0,
            'rotation_z': 1.0,
            'scale_x': 1.0,
            'scale_y': 1.0,
            'scale_z': 1.0
        }, {
            'name': 'test',
            'object_type': 'test',
            'age': 1,
            'missing_age': 1,
            'position_x': 1.0,
            'position_y': 1.0,
            'position_z': 1.0,
            'rotation_x': 1.0,
            'rotation_y': 1.0,
            'rotation_z': 1.0,
            'scale_x': 1.0,
            'scale_y': 1.0,
            'scale_z': 1.0
        }, None),
        # Test case 2: Invalid parameters - string instead of int
        ({
            'age': 'invalid'
        }, {}, ValueError),
        # Test case 3: Invalid parameters - string instead of float
        ({
            'position_x': 'invalid'
        }, {}, ValueError),
    ],
    ids=['valid_parameters', 'invalid_age', 'invalid_position_x'])
def test_update(params, expected_values, expected_exception):
    # Create an instance of your object class
    obj = BaseObject()

    # Test update with the provided parameters
    if expected_exception:
        with pytest.raises(expected_exception):
            obj.update(params)
    else:
        obj.update(params)
        for key, value in expected_values.items():
            assert getattr(obj, key) == value
