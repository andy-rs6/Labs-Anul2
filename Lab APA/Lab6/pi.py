import time
import numpy as np
from mpmath import mp
import matplotlib.pyplot as plt

# Bailey–Borwein–Plouffe Algorithm
def bailey_borwein_plouffe_algorithm(n):
    mp.dps = n + 1
    pi_approximation = 0
    for k in range(n):
        pi_approximation += (1 / mp.mpf(16) ** k) * ((4 / (8 * k + 1)) - (2 / (8 * k + 4)) - (1 / (8 * k + 5)) - (1 / (8 * k + 6)))
    return pi_approximation

# Gauss-Legendre Algorithm
def gauss_legendre_algorithm(n):
    mp.dps = n + 1
    a = mp.mpf(1)
    b = 1 / mp.sqrt(2)
    t = 0.25
    p = 1

    # Perform the iterations
    for _ in range(n):
        a_new = (a + b) / 2
        b = mp.sqrt(a * b)
        t -= p * (a - a_new) ** 2
        a = a_new
        p *= 2
    # Calculate the approximate value of pi
    pi_approximation = (a + b) ** 2 / (4 * t)
    return pi_approximation

# Leibniz Algorithm
def leibniz_algorithm(n):
    pi = 0
    for i in range(n):
        current_term = (-1)**i / (2*i + 1)
        pi += current_term
    pi_approximation = pi * 4
    return pi_approximation


def empirical_analyze(values):
    algorithms = [bailey_borwein_plouffe_algorithm, gauss_legendre_algorithm, leibniz_algorithm, ]
    timings = [[] for _ in range(len(algorithms))]

    for n in values:
        for i, algorithm in enumerate(algorithms):
            start_time = time.time()
            pi = algorithm(n)
            end_time = time.time()
            timings[i].append(end_time - start_time)
            print(f"{algorithm.__name__} (n={n}): {pi}, time: {end_time - start_time:.6f} seconds")

        print(f"++++++++++++++++++++++++++++++++++++++")

    # Bar Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    bar_width = 0.2
    index = np.arange(len(values))

    for i, algorithm in enumerate(algorithms):
        ax.bar(index + i * bar_width, timings[i], bar_width, label=algorithm.__name__)

    ax.set_xlabel('Number of Decimal Places (n)')
    ax.set_ylabel('Execution Time (seconds)')
    ax.set_title('Performance Comparison')
    ax.set_xticks(index + bar_width * len(algorithms) / 2)
    ax.set_xticklabels(values)
    ax.legend()
    plt.tight_layout()
    plt.show()


# Get analysis
n_values = [300,700,1300,7000,10000]  # Example values for n
empirical_analyze(n_values)