import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def inverse_cdf_gaussian(x, mu, sigma, a, b):
    # Calculate the inverse CDF using the cumulative distribution function of the Gaussian distribution
    cdf_a = norm.cdf(a, mu, sigma)
    cdf_b = norm.cdf(b, mu, sigma)
    return norm.ppf(cdf_a + x * (cdf_b - cdf_a), mu, sigma)

def gaussian_sampler(mu, sigma, a, b, num_samples=10000):
    # Generate random numbers from a uniform distribution in the interval [a, b]
    uniform_samples = np.random.uniform(norm.cdf(a, mu, sigma), norm.cdf(b, mu, sigma), num_samples)
    
    # Transform the uniform samples using the inverse CDF to obtain samples from the Gaussian distribution
    return inverse_cdf_gaussian(uniform_samples, mu, sigma, a, b)

# Get Gaussian distribution parameters from user
mu = float(input("Enter the mean (mu) of the Gaussian distribution: "))
sigma = float(input("Enter the standard deviation (sigma) of the Gaussian distribution: "))

# Get interval [a, b] from user
a = float(input("Enter the lower bound of the interval [a, b]: "))
b = float(input("Enter the upper bound of the interval [a, b]: "))

# Generate samples
samples = gaussian_sampler(mu, sigma, a, b)

# Plot histogram
plt.hist(samples, bins=50, density=True, alpha=0.6, color='g')
plt.title('Histogram of Gaussian Distribution Sampler')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.grid(True)
plt.show()
