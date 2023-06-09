# Copyright (c) 2022-2023 IO-Aero. All rights reserved. Use of this
# source code is governed by the IO-Aero License, that can
# be found in the LICENSE.md file.

"""Vector3d module.

This module defines the Vector3D class, which represents a 3D vector
with x, y, and z components. It provides various methods for performing
common operations on 3D vectors, such as calculating the magnitude,
dot product, cross product, normalization, rotation, and translation.

Classes:
    Vector3D: Represents a 3D vector with x, y, and z components.

Examples:
    v = Vector3D(1, 2, 3)

    magnitude = v.magnitude()

    normalized = v.normalize()

    dot_product = v.dot_product(other_vector)

    cross_product = v.cross_product(other_vector)

    v.rotate(45, 'z')

    v.translate(2, 3, 4)
"""

from math import cos
from math import radians
from math import sin


# ------------------------------------------------------------------
# Class Vector3D.
# ------------------------------------------------------------------
class Vector3D:
    """Represents a 3D vector.

    Attributes:
        x (float): The x-component of the vector.
        y (float): The y-component of the vector.
        z (float): The z-component of the vector.
    """

    # ------------------------------------------------------------------
    # Object constructor.
    # ------------------------------------------------------------------
    # pylint: disable-next=invalid-name
    def __init__(self, x: float, y: float, z: float):
        """Initializes a 3D vector with given x, y, and z components.

        Args:

            x: The x-component of the vector.
            y: The y-component of the vector.
            z: The z-component of the vector.
        """
        # pylint: disable-next=invalid-name
        self.x = x
        # pylint: disable-next=invalid-name
        self.y = y
        # pylint: disable-next=invalid-name
        self.z = z

    # ------------------------------------------------------------------
    # Cross product.
    # ------------------------------------------------------------------
    def cross_product(self, other: "Vector3D") -> "Vector3D":
        """Calculates the cross product of this vector with another vector.

        Cross product is a binary operation on two vectors in three-dimensional
        space. It results in a vector that is perpendicular to both vectors.
        The Vector product of two vectors, a and b, is denoted by a × b. Its
        resultant vector is perpendicular to a and b. Vector products are also
        called cross products.

        Args:
            other (Vector3D): The other vector.

        Returns:
            Vector3D: The cross product of the two vectors.
        """
        cross_x = self.y * other.z - self.z * other.y
        cross_y = self.z * other.x - self.x * other.z
        cross_z = self.x * other.y - self.y * other.x

        return Vector3D(cross_x, cross_y, cross_z)

    # ------------------------------------------------------------------
    # Dot product.
    # ------------------------------------------------------------------
    def dot_product(self, other: "Vector3D") -> float:
        """Calculates the dot product of this vector with another vector.

        The dot product, or inner product, of two vectors, is the sum of the
        products of corresponding components. Equivalently, it is the product
        of their magnitudes, times the cosine of the angle between them. The
        dot product of a vector with itself is the square of its magnitude.

        Args:
            other (Vector3D): The other vector.

        Returns:
            float: The dot product of the two vectors.
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    # ------------------------------------------------------------------
    # Magnitude.
    # ------------------------------------------------------------------
    def magnitude(self) -> float:
        """Calculates the magnitude (length) of the vector.

        The magnitude of a vector is the length of the vector.

        Returns:
            float: The magnitude of the vector.
        """
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    # ------------------------------------------------------------------
    # Normalize.
    # ------------------------------------------------------------------
    def normalize(self) -> "Vector3D":
        """Normalizes the vector (converts it to a unit vector).

        A normalized vector maintains its direction but its Length becomes 1.
        The resulting vector is often called a unit vector. A vector is
        normalized by dividing the vector by its own Length.

        Returns:
            The normalized vector as a new Vector3D object.
        """
        magnitude = self.magnitude()

        if magnitude == 0:
            return Vector3D(0, 0, 0)

        return Vector3D(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
        )

    # ------------------------------------------------------------------
    # Rotate.
    # ------------------------------------------------------------------
    def rotate(self, angle: float, axis: str = "x") -> None:
        """Rotates the vector around a specified axis.

        Args:
            angle (float): The rotation angle in degrees.
            axis (str): The axis of rotation ('x', 'y', or 'z'). Default is the
                        'x' axis.
        """
        print(
            "wwe old x="
            + str(self.x)
            + " old y="
            + str(self.y)
            + " old z="
            + str(self.z)
            + " angle="
            + str(angle)
            + " axis="
            + axis
        )

        rad_angle = radians(angle)

        axis_lower = axis.lower()

        if axis_lower == "x":
            new_y = self.y * cos(rad_angle) - self.z * sin(rad_angle)
            new_z = self.y * sin(rad_angle) + self.z * cos(rad_angle)
            self.y = new_y
            self.z = new_z
        elif axis_lower == "y":
            new_x = self.x * cos(rad_angle) + self.z * sin(rad_angle)
            new_z = -self.x * sin(rad_angle) + self.z * cos(rad_angle)
            self.x = new_x
            self.z = new_z
        elif axis_lower == "z":
            new_x = self.x * cos(rad_angle) - self.y * sin(rad_angle)
            new_y = self.x * sin(rad_angle) + self.y * cos(rad_angle)
            self.x = new_x
            self.y = new_y
        else:
            raise ValueError("Invalid axis. Must be 'x', 'y', or 'z'.")

        print(
            "wwe new x="
            + str(self.x)
            + " new y="
            + str(self.y)
            + " new z="
            + str(self.z)
        )

    # ------------------------------------------------------------------
    # Translate.
    # ------------------------------------------------------------------
    def translate(self, x_offset: float, y_offset: float, z_offset: float) -> None:
        """Translates the vector by the specified offsets.

        Translation by a vector refers to the movement of one or more points
        of a space in a particular direction by a specified amount.

        Args:
            x_offset (float): The offset along the x-axis.
            y_offset (float): The offset along the y-axis.
            z_offset (float): The offset along the z-axis.
        """
        self.x += x_offset
        self.y += y_offset
        self.z += z_offset
