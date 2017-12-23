import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE
    avg = np.mean(data)
    numerator = np.square(data - predictions).sum()
    denomirator = np.square(data - avg).sum()
    r_squared = 1 - (numerator/denomirator)

    return r_squared