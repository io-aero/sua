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


class Vector3D:
    """Represents a 3D vector.

    Attributes:
        x_comp (float): The x-component of the vector.
        y_comp (float): The y-component of the vector.
        z_comp (float): The z-component of the vector.
    """

    def __init__(self, x_comp: float, y_comp: float, z_comp: float):
        """Initializes a 3D vector with given x, y, and z components.

        Args:

            x_comp: The x-component of the vector.
            y_comp: The y-component of the vector.
            z_comp: The z-component of the vector.
        """
        self.x_comp = x_comp
        self.y_comp = y_comp
        self.z_comp = z_comp

    def cross_product(self, other: "Vector3D") -> "Vector3D":
        """Calculates the cross product of this vector with another vector.

        Args:
            other (Vector3D): The other vector.

        Returns:
            Vector3D: The cross product of the two vectors.
        """
        cross_x = self.y_comp * other.z_comp - self.z_comp * other.y_comp
        cross_y = self.z_comp * other.x_comp - self.x_comp * other.z_comp
        cross_z = self.x_comp * other.y_comp - self.y_comp * other.x_comp
        return Vector3D(cross_x, cross_y, cross_z)

    def dot_product(self, other: "Vector3D") -> float:
        """Calculates the dot product of this vector with another vector.

        Args:
            other (Vector3D): The other vector.

        Returns:
            float: The dot product of the two vectors.
        """
        return (
            self.x_comp * other.x_comp
            + self.y_comp * other.y_comp
            + self.z_comp * other.z_comp
        )

    def magnitude(self) -> float:
        """Calculates the magnitude (length) of the vector.

        Returns:
            float: The magnitude of the vector.
        """
        return (self.x_comp**2 + self.y_comp**2 + self.z_comp**2) ** 0.5

    def normalize(self) -> "Vector3D":
        """Normalizes the vector (converts it to a unit vector).

        Returns:
            The normalized vector as a new Vector3D object.
        """
        magnitude = self.magnitude()
        if magnitude == 0:
            return Vector3D(0, 0, 0)
        return Vector3D(
            self.x_comp / magnitude,
            self.y_comp / magnitude,
            self.z_comp / magnitude,
        )

    def rotate(self, angle: float, axis: str) -> None:
        """Rotates the vector around a specified axis.

        Args:
            angle (float): The rotation angle in degrees.
            axis (str): The axis of rotation ('x', 'y', or 'z').
        """
        rad_angle = radians(angle)
        if axis == "x":
            new_y = self.y_comp * cos(rad_angle) - self.z_comp * sin(rad_angle)
            new_z = self.y_comp * sin(rad_angle) + self.z_comp * cos(rad_angle)
            self.y_comp = new_y
            self.z_comp = new_z
        elif axis == "y":
            new_x = self.x_comp * cos(rad_angle) + self.z_comp * sin(rad_angle)
            new_z = -self.x_comp * sin(rad_angle) + self.z_comp * cos(rad_angle)
            self.x_comp = new_x
            self.z_comp = new_z
        elif axis == "z":
            new_x = self.x_comp * cos(rad_angle) - self.y_comp * sin(rad_angle)
            new_y = self.x_comp * sin(rad_angle) + self.y_comp * cos(rad_angle)
            self.x_comp = new_x
            self.y_comp = new_y
        else:
            raise ValueError("Invalid axis. Must be 'x', 'y', or 'z'.")

    def translate(self, x_offset: float, y_offset: float, z_offset: float) -> None:
        """Translates the vector by the specified offsets.

        Args:
            x_offset (float): The offset along the x-axis.
            y_offset (float): The offset along the y-axis.
            z_offset (float): The offset along the z-axis.
        """
        self.x_comp += x_offset
        self.y_comp += y_offset
        self.z_comp += z_offset
