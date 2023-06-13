// use std::f64::consts::{cos, sin, FRAC_PI_180};
use std::f64;

/// Represents a 3D vector with x, y, and z components.
#[derive(Debug)]
pub struct Vector3D {
    pub x: f64,
    pub y: f64,
    pub z: f64,
}

impl Vector3D {
    /// Creates a new `Vector3D` instance with the given x, y, and z components.
    pub fn new(x: f64, y: f64, z: f64) -> Vector3D {
        Vector3D { x, y, z }
    }

    /// Calculates the cross product of this vector with another vector.
    ///
    /// The cross product is a binary operation on two vectors in three-dimensional space.
    /// It results in a vector that is perpendicular to both vectors.
    ///
    /// # Arguments
    ///
    /// * `other` - The other vector.
    ///
    /// # Returns
    ///
    /// The cross product of the two vectors.
    pub fn cross_product(&self, other: &Vector3D) -> Vector3D {
        let cross_x = self.y * other.z - self.z * other.y;
        let cross_y = self.z * other.x - self.x * other.z;
        let cross_z = self.x * other.y - self.y * other.x;

        Vector3D::new(cross_x, cross_y, cross_z)
    }

    /// Calculates the dot product of this vector with another vector.
    ///
    /// The dot product, or inner product, of two vectors is the sum of the products
    /// of corresponding components. Equivalently, it is the product of their magnitudes,
    /// times the cosine of the angle between them. The dot product of a vector with itself
    /// is the square of its magnitude.
    ///
    /// # Arguments
    ///
    /// * `other` - The other vector.
    ///
    /// # Returns
    ///
    /// The dot product of the two vectors.
    pub fn dot_product(&self, other: &Vector3D) -> f64 {
        self.x * other.x + self.y * other.y + self.z * other.z
    }

    /// Calculates the magnitude (length) of the vector.
    ///
    /// The magnitude of a vector is the length of the vector.
    ///
    /// # Returns
    ///
    /// The magnitude of the vector.
    pub fn magnitude(&self) -> f64 {
        (self.x.powi(2) + self.y.powi(2) + self.z.powi(2)).sqrt()
    }

    /// Normalizes the vector (converts it to a unit vector).
    ///
    /// A normalized vector maintains its direction but its length becomes 1.
    /// The resulting vector is often called a unit vector. A vector is
    /// normalized by dividing the vector by its own length.
    ///
    /// # Returns
    ///
    /// The normalized vector as a new `Vector3D` object.
    pub fn normalize(&self) -> Vector3D {
        let magnitude = self.magnitude();

        if magnitude == 0.0 {
            return Vector3D::new(0.0, 0.0, 0.0);
        }

        Vector3D::new(self.x / magnitude, self.y / magnitude, self.z / magnitude)
    }

    /// Rotates the vector around a specified axis.
    ///
    /// # Arguments
    ///
    /// * `angle` - The rotation angle in degrees.
    /// * `axis` - The axis of rotation ('x', 'y', or 'z'). Default is the 'x' axis.
    pub fn rotate(&mut self, angle: f64, axis: &str) {
        let rad_angle = f64::to_radians(angle);

        match axis.to_lowercase().as_str() {
            "x" => {
                let new_y = self.y * f64::cos(rad_angle) - self.z * f64::sin(rad_angle);
                let new_z = self.y * f64::sin(rad_angle) + self.z * f64::cos(rad_angle);
                self.y = new_y;
                self.z = new_z;
            }
            "y" => {
                let new_x = self.x * f64::cos(rad_angle) + self.z * f64::sin(rad_angle);
                let new_z = -self.x * f64::sin(rad_angle) + self.z * f64::cos(rad_angle);
                self.x = new_x;
                self.z = new_z;
            }
            "z" => {
                let new_x = self.x * f64::cos(rad_angle) - self.y * f64::sin(rad_angle);
                let new_y = self.x * f64::sin(rad_angle) + self.y * f64::cos(rad_angle);
                self.x = new_x;
                self.y = new_y;
            }
            _ => {
                panic!("Invalid axis. Must be 'x', 'y', or 'z'.");
            }
        }
    }

    /// Translates the vector by the specified offsets.
    ///
    /// Translation by a vector refers to the movement of one or more points of a
    /// space in a particular direction by a specified amount.
    ///
    /// # Arguments
    ///
    /// * `x_offset` - The offset along the x-axis.
    /// * `y_offset` - The offset along the y-axis.
    /// * `z_offset` - The offset along the z-axis.
    pub fn translate(&mut self, x_offset: f64, y_offset: f64, z_offset: f64) {
        self.x += x_offset;
        self.y += y_offset;
        self.z += z_offset;
    }
}
