"""
compare_ctpf_vs_qctpf.py — Side-by-Side Trajectory Comparison

Runs both CTPF and QCTPF on identical scenarios and plots
their trajectories in 3D for direct performance comparison.
"""

import numpy as np
import matplotlib.pyplot as plt

from trial_run_ctpf import run_ctpf_guidance
from trial_run import run_qctpf_guidance_viewer


def run_comparison():
    print("Running Classical CTPF...")
    target_ctpf, missile_ctpf = run_ctpf_guidance(return_traj=True)

    print("Running QCTPF...")
    target_qctpf, missile_qctpf = run_qctpf_guidance_viewer(return_traj=True)

    # [REDACTED] — 3D plot formatting and visualization
    raise NotImplementedError


if __name__ == "__main__":
    run_comparison()
