"""test_vector3d module.

This module contains pytest tests for the vector3d class in the vector3d module.
It covers various aspects of the vector3d class, including magnitude calculation,
normalization, dot product, cross product, rotation, and translation.

To run the tests, execute `pytest` in the same directory.
"""

from math import isclose

import pytest

from src.sua import vector3d


def test_cross_product_1():
    """Test the cross product calculation between two Vector3D objects."""
    vector1 = vector3d.Vector3D(1, 2, 3)
    vector2 = vector3d.Vector3D(4, 5, 6)
    cross_product = vector1.cross_product(vector2)
    assert isclose(cross_product.x, -3)
    assert isclose(cross_product.y, 6)
    assert isclose(cross_product.z, -3)


def test_cross_product_2():
    """Test the cross product calculation between two Vector3D objects."""
    vector1 = vector3d.Vector3D(3, 5, -7)
    vector2 = vector3d.Vector3D(2, -6, 4)
    cross_product = vector1.cross_product(vector2)
    assert isclose(cross_product.x, -22)
    assert isclose(cross_product.y, -26)
    assert isclose(cross_product.z, -28)


def test_cross_product_3():
    """Test the cross product calculation between two Vector3D objects."""
    vector1 = vector3d.Vector3D(3, 1, 1)
    vector2 = vector3d.Vector3D(-2, 5, 1)
    cross_product = vector1.cross_product(vector2)
    assert isclose(cross_product.x, -4)
    assert isclose(cross_product.y, -5)
    assert isclose(cross_product.z, 17)


def test_cross_product_4():
    """Test the cross product calculation between two Vector3D objects."""
    vector1 = vector3d.Vector3D(1, 2, 3)
    vector2 = vector3d.Vector3D(3, 2, 1)
    cross_product = vector1.cross_product(vector2)
    assert isclose(cross_product.x, -4)
    assert isclose(cross_product.y, 8)
    assert isclose(cross_product.z, -4)


def test_cross_product_5():
    """Test the cross product calculation between two Vector3D objects."""
    vector1 = vector3d.Vector3D(1, 0, 0)
    vector2 = vector3d.Vector3D(0, 0, 1)
    cross_product = vector1.cross_product(vector2)
    assert isclose(cross_product.x, 0)
    assert isclose(cross_product.y, -1)
    assert isclose(cross_product.z, 0)


def test_dot_product_1():
    """Test the dot product calculation between two Vector3D objects."""
    vector1 = vector3d.Vector3D(1, 2, 3)
    vector2 = vector3d.Vector3D(4, 5, 6)
    assert isclose(vector1.dot_product(vector2), 32)


def test_dot_product_2():
    """Test the dot product calculation between two Vector3D objects."""
    vector1 = vector3d.Vector3D(1, 2, 3)
    vector2 = vector3d.Vector3D(3, 4, 5)
    assert isclose(vector1.dot_product(vector2), 26)


def test_magnitude_1():
    """Test the magnitude calculation of a Vector3D object."""
    vector = vector3d.Vector3D(3, 4, 5)
    assert isclose(vector.magnitude(), 7.071067811865476)


def test_magnitude_2():
    """Test the magnitude calculation of a Vector3D object."""
    vector = vector3d.Vector3D(3, 2, -1)
    assert isclose(vector.magnitude(), 3.7416573867739413)


def test_normalize_0():
    """Test the normalization of a Vector3D object."""
    vector = vector3d.Vector3D(0, 0, 0)
    normalized = vector.normalize()
    assert isclose(normalized.magnitude(), 0)
    assert isclose(normalized.x, 0)
    assert isclose(normalized.y, 0)
    assert isclose(normalized.z, 0)


def test_normalize_1():
    """Test the normalization of a Vector3D object."""
    vector = vector3d.Vector3D(3, 4, 5)
    normalized = vector.normalize()
    assert isclose(normalized.magnitude(), 1.0)
    assert isclose(normalized.x, 0.4242640687119285)
    assert isclose(normalized.y, 0.565685424949238)
    assert isclose(normalized.z, 0.7071067811865475)


def test_normalize_2():
    """Test the normalization of a Vector3D object."""
    vector = vector3d.Vector3D(-1, -1, -1)
    normalized = vector.normalize()
    assert isclose(normalized.magnitude(), 1.0)
    assert isclose(normalized.x, -0.57735026919)
    assert isclose(normalized.y, -0.57735026919)
    assert isclose(normalized.z, -0.57735026919)


def test_rotate_1():
    """Test the rotation of a Vector3D object."""
    vector = vector3d.Vector3D(1, 0, 0)
    vector.rotate(90, "y")
    assert isclose(vector.x, 6.123233995736766e-17)
    assert isclose(vector.y, 0)
    assert isclose(vector.z, -1)


def test_rotate_2():
    """Test the rotation of a Vector3D object."""
    vector = vector3d.Vector3D(1, 0, 0)
    with pytest.raises(ValueError):
        vector.rotate(90, "invalid_axis")


def test_rotate_3():
    """Test the rotation of a Vector3D object."""
    vector = vector3d.Vector3D(1, 0, 0)
    vector.rotate(45, "z")
    assert isclose(vector.x, 0.7071067811865476)
    assert isclose(vector.y, 0.7071067811865476)
    assert (vector.z, 0)


def test_rotate_4():
    """Test the rotation of a Vector3D object."""
    vector = vector3d.Vector3D(1, 0, 0)
    vector.rotate(450, "x")
    assert isclose(vector.x, 1)
    assert isclose(vector.y, 0)
    assert isclose(vector.z, 0)


def test_translate_1():
    """Test the translation of a Vector3D object."""
    vector = vector3d.Vector3D(1, 2, 3)
    vector.translate(4, 5, 6)
    assert vector.x == 5
    assert vector.y == 7
    assert vector.z == 9


def test_translate_2():
    """Test the translation of a Vector3D object."""
    vector = vector3d.Vector3D(1, 2, 3)
    vector.translate(-1, -2, -3                     )
    assert vector.x == 0
    assert vector.y == 0
    assert vector.z == 0


def test_translate_3():
    """Test the translation of a Vector3D object."""
    vector = vector3d.Vector3D(-1, -2, -3)
    vector.translate(-4, -5, -6)
    assert vector.x == -5
    assert vector.y == -7
    assert vector.z == -9
