// main.rs

mod vector3d;

use std::f64::EPSILON;
use vector3d::Vector3D;

#[test]
fn test_cross_product_1() {
    let vector1 = Vector3D::new(1.0, 2.0, 3.0);
    let vector2 = Vector3D::new(4.0, 5.0, 6.0);
    let cross_product = vector1.cross_product(&vector2);
    assert!((cross_product.x - (-3.0)).abs() < EPSILON);
    assert!((cross_product.y - 6.0).abs() < EPSILON);
    assert!((cross_product.z - (-3.0)).abs() < EPSILON);
}

#[test]
fn test_cross_product_2() {
    let vector1 = Vector3D::new(3.0, 5.0, -7.0);
    let vector2 = Vector3D::new(2.0, -6.0, 4.0);
    let cross_product = vector1.cross_product(&vector2);
    assert!((cross_product.x - (-22.0)).abs() < EPSILON);
    assert!((cross_product.y - (-26.0)).abs() < EPSILON);
    assert!((cross_product.z - (-28.0)).abs() < EPSILON);
}

#[test]
fn test_cross_product_3() {
    let vector1 = Vector3D::new(3.0, 1.0, 1.0);
    let vector2 = Vector3D::new(-2.0, 5.0, 1.0);
    let cross_product = vector1.cross_product(&vector2);
    assert!((cross_product.x - (-4.0)).abs() < EPSILON);
    assert!((cross_product.y - (-5.0)).abs() < EPSILON);
    assert!((cross_product.z - 17.0).abs() < EPSILON);
}

#[test]
fn test_cross_product_4() {
    let vector1 = Vector3D::new(1.0, 2.0, 3.0);
    let vector2 = Vector3D::new(3.0, 2.0, 1.0);
    let cross_product = vector1.cross_product(&vector2);
    assert!((cross_product.x - (-4.0)).abs() < EPSILON);
    assert!((cross_product.y - 8.0).abs() < EPSILON);
    assert!((cross_product.z - (-4.0)).abs() < EPSILON);
}

#[test]
fn test_cross_product_5() {
    let vector1 = Vector3D::new(1.0, 0.0, 0.0);
    let vector2 = Vector3D::new(0.0, 0.0, 1.0);
    let cross_product = vector1.cross_product(&vector2);
    assert!((cross_product.x - 0.0).abs() < EPSILON);
    assert!((cross_product.y - (-1.0)).abs() < EPSILON);
    assert!((cross_product.z - 0.0).abs() < EPSILON);
}

#[test]
fn test_cross_product_6() {
    let vector1 = Vector3D::new(0.0, 0.0, 0.0);
    let vector2 = Vector3D::new(0.0, 0.0, 1.0);
    let cross_product = vector1.cross_product(&vector2);
    assert!((cross_product.x - 0.0).abs() < EPSILON);
    assert!((cross_product.y - 0.0).abs() < EPSILON);
    assert!((cross_product.z - 0.0).abs() < EPSILON);
}

#[test]
fn test_dot_product_1() {
    let vector1 = Vector3D::new(1.0, 2.0, 3.0);
    let vector2 = Vector3D::new(4.0, 5.0, 6.0);
    assert!((vector1.dot_product(&vector2) - 32.0).abs() < EPSILON);
}

#[test]
fn test_dot_product_2() {
    let vector1 = Vector3D::new(1.0, 2.0, 3.0);
    let vector2 = Vector3D::new(3.0, 4.0, 5.0);
    assert!((vector1.dot_product(&vector2) - 26.0).abs() < EPSILON);
}

#[test]
fn test_dot_product_3() {
    let vector1 = Vector3D::new(0.0, 0.0, 0.0);
    let vector2 = Vector3D::new(3.0, 4.0, 5.0);
    assert!((vector1.dot_product(&vector2) - 0.0).abs() < EPSILON);
}

#[test]
fn test_magnitude_1() {
    let vector = Vector3D::new(3.0, 4.0, 5.0);
    assert!((vector.magnitude() - 7.071067811865476).abs() < EPSILON);
}

#[test]
fn test_magnitude_2() {
    let vector = Vector3D::new(3.0, 2.0, -1.0);
    assert!((vector.magnitude() - 3.7416573867739413).abs() < EPSILON);
}

#[test]
fn test_magnitude_3() {
    let vector = Vector3D::new(0.0, 0.0, 0.0);
    assert!((vector.magnitude() - 0.0).abs() < EPSILON);
}

#[test]
fn test_normalize_0() {
    let vector = Vector3D::new(0.0, 0.0, 0.0);
    let normalized = vector.normalize();
    assert!((normalized.magnitude() - 0.0).abs() < EPSILON);
    assert!((normalized.x - 0.0).abs() < EPSILON);
    assert!((normalized.y - 0.0).abs() < EPSILON);
    assert!((normalized.z - 0.0).abs() < EPSILON);
}

#[test]
fn test_normalize_1() {
    let vector = Vector3D::new(3.0, 4.0, 5.0);
    let normalized = vector.normalize();
    assert!((normalized.magnitude() - 1.0).abs() < EPSILON);
    assert!((normalized.x - 0.4242640687119285).abs() < EPSILON);
    assert!((normalized.y - 0.565685424949238).abs() < EPSILON);
    assert!((normalized.z - 0.7071067811865475).abs() < EPSILON);
}

#[test]
fn test_normalize_2() {
    let vector = Vector3D::new(-1.0, -1.0, -1.0);
    let normalized = vector.normalize();
    assert!((normalized.magnitude() - 1.0).abs() < EPSILON);
    assert!((normalized.x - (-0.57735026919)).abs() < EPSILON);
    assert!((normalized.y - (-0.57735026919)).abs() < EPSILON);
    assert!((normalized.z - (-0.57735026919)).abs() < EPSILON);
}

#[test]
fn test_rotate_1() {
    let mut vector = Vector3D::new(1.0, 0.0, 0.0);
    vector.rotate(90.0, "y");
    assert!((vector.x - 6.123233995736766e-17).abs() < EPSILON);
    assert!((vector.y - 0.0).abs() < EPSILON);
    assert!((vector.z - (-1.0)).abs() < EPSILON);
}

#[test]
#[should_panic]
fn test_rotate_2() {
    let mut vector = Vector3D::new(1.0, 0.0, 0.0);
    vector.rotate(90.0, "invalid_axis");
}

#[test]
fn test_rotate_3() {
    let mut vector = Vector3D::new(1.0, 0.0, 0.0);
    vector.rotate(45.0, "z");
    assert!((vector.x - 0.7071067811865476).abs() < EPSILON);
    assert!((vector.y - 0.7071067811865476).abs() < EPSILON);
    assert!((vector.z - 0.0).abs() < EPSILON);
}

#[test]
fn test_rotate_4() {
    let mut vector = Vector3D::new(1.0, 0.0, 0.0);
    vector.rotate(450.0, "x");
    assert!((vector.x - 1.0).abs() < EPSILON);
    assert!((vector.y - 0.0).abs() < EPSILON);
    assert!((vector.z - 0.0).abs() < EPSILON);
}

#[test]
fn test_rotate_5() {
    let mut vector = Vector3D::new(0.0, 0.0, 0.0);
    vector.rotate(90.0, "y");
    assert!((vector.x - 0.0).abs() < EPSILON);
    assert!((vector.y - 0.0).abs() < EPSILON);
    assert!((vector.z - 0.0).abs() < EPSILON);
}

#[test]
fn test_rotate_6() {
    let mut vector = Vector3D::new(0.0, 0.0, 1.0);
    vector.rotate(0.0, "x");
    assert!((vector.x - 0.0).abs() < EPSILON);
    assert!((vector.y - 0.0).abs() < EPSILON);
    assert!((vector.z - 1.0).abs() < EPSILON);
}

#[test]
fn test_rotate_7() {
    let mut vector = Vector3D::new(0.0, 0.0, 1.0);
    vector.rotate(0.0, "y");
    assert!((vector.x - 0.0).abs() < EPSILON);
    assert!((vector.y - 0.0).abs() < EPSILON);
    assert!((vector.z - 1.0).abs() < EPSILON);
}

#[test]
fn test_rotate_8() {
    let mut vector = Vector3D::new(0.0, 0.0, 1.0);
    vector.rotate(0.0, "z");
    assert!((vector.x - 0.0).abs() < EPSILON);
    assert!((vector.y - 0.0).abs() < EPSILON);
    assert!((vector.z - 1.0).abs() < EPSILON);
}
