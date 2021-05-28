"""
Tests for the measure module.
"""

import numpy as np
import pytest

import molecool

def test_calculate_distance():
    """Test that calculate_distance function calculates what we expect."""
    
    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance

@pytest.mark.xfail
def test_calculate_angle():
   """Test the calculate_angle function"""

   r1 = np.array([1, 0, 0])
   r2 = np.array([0, 0, 0])
   r3 = np.array([0, 1, 0])

   expected_value = 120

   calculated_value = molecool.calculate_angle(r1, r2, r3, degrees=True)
   assert expected_value == calculated_value

@pytest.mark.skip
def test_calculate_angle_60():
    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 1, 0])
    r3 = np.array([1, 0, 0])

    expected_angle = 60

    calculated_angle = molecool.calculate_angle(r1, r2, r3, degrees=True)

    assert pytest.approx(expected_angle) == calculated_angle

@pytest.mark.parametrize("r1, r2, r3, expected_angle", [
    (np.array([1, 0, 0]), np.array([0, 0, 0]), np.array([0, 1, 0]), 90),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60),
])
def test_calculate_angle_many(r1, r2, r3, expected_angle):
    calculated_angle = molecool.calculate_angle(r1, r2, r3, degrees=True)
    assert pytest.approx(calculated_angle) == expected_angle