import numpy as np

class HopfieldNetwork:
    def __init__(self, size):
        self.size = size
        self.weights = np.zeros((size, size))

    def train(self, patterns):
        """
        Train the Hopfield network using Hebbian learning.
        Each pattern should be a numpy array of -1 and 1 values.
        """
        for pattern in patterns:
            pattern = pattern.reshape(self.size, 1)
            self.weights += pattern @ pattern.T
        np.fill_diagonal(self.weights, 0)  # No self-connection
        self.weights /= len(patterns)      # Normalize weights

    def recall(self, pattern, steps=5):
        """
        Recall a pattern from memory.
        Uses asynchronous updates for a number of steps.
        """
        pattern = pattern.copy()
        for _ in range(steps):
            for i in range(self.size):
                raw_input = np.dot(self.weights[i], pattern)
                pattern[i] = 1 if raw_input >= 0 else -1
        return pattern

    def energy(self, pattern):
        """
        Compute the energy of the current pattern.
        """
        return -0.5 * pattern.T @ self.weights @ pattern

def print_pattern(pattern, shape):
    """
    Print the pattern in a grid using █ for 1 and space for -1.
    """
    reshaped = pattern.reshape(shape)
    for row in reshaped:
        print(''.join(['█' if val == 1 else ' ' for val in row]))
    print()

# --- Example usage ---
if __name__ == "__main__":
    # Define training patterns (3x3 grid, use -1 and 1 only)
    pattern1 = np.array([1, -1, 1,
                         -1, 1, -1,
                         1, -1, 1])
    
    pattern2 = np.array([-1, 1, -1,
                         1, -1, 1,
                         -1, 1, -1])

    patterns = [pattern1, pattern2]

    # Create Hopfield network with 9 neurons
    hopfield_net = HopfieldNetwork(size=9)
    hopfield_net.train(patterns)

    # Define a noisy version of pattern1
    noisy_pattern = np.array([1, -1, -1,
                              -1, 1, -1,
                              1, 1, 1])

    print("Noisy Input Pattern:")
    print_pattern(noisy_pattern, (3, 3))

    # Recover the pattern
    recovered = hopfield_net.recall(noisy_pattern, steps=5)

    print("Recovered Pattern:")
    print_pattern(recovered, (3, 3))

    # Optional: print energy of recovered pattern
    print("Energy of recovered pattern:", hopfield_net.energy(recovered))
