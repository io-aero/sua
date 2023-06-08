"""test_vector3d module.

This module contains pytest tests for the vector3d class in the vector3d module.
It covers various aspects of the vector3d class, including magnitude calculation,
normalization, dot product, cross product, rotation, and translation.

To run the tests, execute `pytest` in the same directory.
"""

from math import isclose

import pytest

from sua import vector3d


def test_cross_product_1():
    """Test the cross product calculation between two Vector3D objects."""
    vector1 = vector3d.Vector3D(1, 2, 3)
    vector2 = vector3d.Vector3D(4, 5, 6)
    cross_product = vector1.cross_product(vector2)
    assert isclose(cross_product.x_comp, -3)
    assert isclose(cross_product.y_comp, 6)
    assert isclose(cross_product.z_comp, -3)


def test_cross_product_2():
    """Test the cross product calculation between two Vector3D objects."""
    vector1 = vector3d.Vector3D(3, 5, -7)
    vector2 = vector3d.Vector3D(2, -6, 4)
    cross_product = vector1.cross_product(vector2)
    assert isclose(cross_product.x_comp, -22)
    assert isclose(cross_product.y_comp, -26)
    assert isclose(cross_product.z_comp, -28)


def test_dot_product():
    """Test the dot product calculation between two Vector3D objects."""
    vector1 = vector3d.Vector3D(1, 2, 3)
    vector2 = vector3d.Vector3D(4, 5, 6)
    assert isclose(vector1.dot_product(vector2), 32)


def test_magnitude():
    """Test the magnitude calculation of a Vector3D object."""
    vector = vector3d.Vector3D(3, 4, 5)
    assert isclose(vector.magnitude(), 7.071067811865476)


def test_normalize():
    """Test the normalization of a Vector3D object."""
    vector = vector3d.Vector3D(3, 4, 5)
    normalized = vector.normalize()
    assert isclose(normalized.magnitude(), 1.0)
    assert isclose(normalized.x_comp, 0.4242640687119285)
    assert isclose(normalized.y_comp, 0.565685424949238)
    assert isclose(normalized.z_comp, 0.7071067811865475)


def test_rotate():
    """Test the rotation of a Vector3D object."""
    vector = vector3d.Vector3D(1, 0, 0)
    vector.rotate(90, "y")
    assert isclose(vector.x_comp, 0)
    assert isclose(vector.y_comp, 0)
    assert isclose(vector.z_comp, -1)

    vector.rotate(45, "z")
    assert isclose(vector.x_comp, 0.7071067811865476)
    assert isclose(vector.y_comp, -0.7071067811865475)
    assert isclose(vector.z_comp, -1)

    with pytest.raises(ValueError):
        vector.rotate(90, "invalid_axis")


def test_translate():
    """Test the translation of a Vector3D object."""
    vector = vector3d.Vector3D(1, 2, 3)
    vector.translate(4, 5, 6)
    assert vector.x_comp == 5
    assert vector.y_comp == 7
    assert vector.z_comp == 9
