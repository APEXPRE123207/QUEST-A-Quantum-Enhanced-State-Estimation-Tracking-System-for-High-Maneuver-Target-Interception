from dataclasses import dataclass

@dataclass
class QNEATOptions:
    """Hyperparameters for the QNEAT algorithm."""
    population_size: int = [REDACTED]
    add_rot_prob: float = [REDACTED]
    add_cnot_prob: float = [REDACTED]
    weight_mutate_prob: float = [REDACTED]
    new_weight_prob: float = [REDACTED]
    weight_mutate_power: float = [REDACTED]
    crossover_rate: float = [REDACTED]
    compatibility_threshold: float = [REDACTED]
    c1: float = [REDACTED]
    c2: float = [REDACTED]
    c3: float = [REDACTED]
    species_elitism: int = [REDACTED]
    survival_rate: float = [REDACTED]

@dataclass
class SimOptions:
    """General simulation parameters."""
    dt: float = [REDACTED]
    total_time: int = [REDACTED]
    num_particles: int = [REDACTED]
    seed: int = [REDACTED]
    missile_max_speed: float = [REDACTED]
    missile_max_accel: float = [REDACTED]
    ess_resample_threshold_ratio: float = [REDACTED]
    fallback_window: int = [REDACTED]
    planning_horizon: int = [REDACTED]
    waypoint_step: float = [REDACTED]

@dataclass
class QAOAOptions:
    """QAOA parameters."""
    reps: int = [REDACTED]
    shots: int = [REDACTED]
    max_iterations: int = [REDACTED]
    w1: float = [REDACTED]
    w2: float = [REDACTED]
    P: int = [REDACTED]
