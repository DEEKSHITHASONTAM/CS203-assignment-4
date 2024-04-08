# Gaussian Distribution Sampler

This Python script generates random samples from a Gaussian distribution within a specified interval `[a, b]`.

## Dependencies

- NumPy
- Matplotlib
- SciPy

Make sure you have these libraries installed. You can install them using `pip`:

```bash
pip install numpy matplotlib scipy
```
## Usage

1. **Navigate to the directory containing the script:**

    ```bash
    cd CS203-assignment-4
    ```

2. **Run the script:**

    ```bash
    python cs203_assignment-4.py
    ```

3. **Follow the prompts to enter the parameters:**

    - Mean (mu) of the Gaussian distribution.
    - Standard deviation (sigma) of the Gaussian distribution.
    - Lower bound (a) of the interval [a, b].
    - Upper bound (b) of the interval [a, b].

5. The script will generate random samples from the Gaussian distribution and plot a histogram.

## Explanation

1. **`inverse_cdf_gaussian(x, mu, sigma, a, b)`**

    This function calculates the inverse cumulative distribution function (CDF) of the Gaussian distribution. It takes the following parameters:
    
    - `x`: Probability value.
    - `mu`: Mean of the Gaussian distribution.
    - `sigma`: Standard deviation of the Gaussian distribution.
    - `a`: Lower bound of the interval [a, b].
    - `b`: Upper bound of the interval [a, b].

2. **`gaussian_sampler(mu, sigma, a, b, num_samples=10000)`**

    This function generates random samples from a Gaussian distribution within the interval [a, b]. It uses the inverse CDF method to transform uniform samples to Gaussian samples. It takes the following parameters:
    
    - `mu`: Mean of the Gaussian distribution.
    - `sigma`: Standard deviation of the Gaussian distribution.
    - `a`: Lower bound of the interval [a, b].
    - `b`: Upper bound of the interval [a, b].
    - `num_samples`: Number of samples to generate (default is 10,000).

3. **Running the Script**

    When you run the script, you'll be prompted to enter the mean, standard deviation, and the interval [a, b]. After entering the parameters, the script will generate random samples from the Gaussian distribution and plot a histogram showing the distribution of the samples.
