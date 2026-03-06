"""
Missile kinematics — 3-DOF point-mass model.
Speed/acceleration limits are redacted.
"""
import numpy as np
from typing import List


class Missile:
    def __init__(self, initial_position: List[float], initial_velocity: List[float]):
        self.position = np.array(initial_position, dtype=float)
        self.velocity = np.array(initial_velocity, dtype=float)
        self.acceleration = np.zeros(3, dtype=float)
        self.max_speed = [REDACTED]
        self.max_accel = [REDACTED]

    def update(self, dt: float, accel_cmd: np.ndarray) -> None:
        # [REDACTED] — saturation + integration
        raise NotImplementedError
