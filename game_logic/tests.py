import numpy as np

test_cases = [
    (np.array([0, 0, 0, 0]), np.array([0, 0, 0, 0]), np.array([4, 0])),
    (np.array([1, 2, 3, 4]), np.array([1, 2, 3, 4]), np.array([4, 0])),
    (np.array([1, 2, 3, 4]), np.array([4, 3, 2, 1]), np.array([0, 4])),
    (np.array([1, 1, 2, 2]), np.array([2, 2, 1, 1]), np.array([0, 4])),
    (np.array([0, 1, 2, 3]), np.array([4, 5, 5, 5]), np.array([0, 0])),
    (np.array([4, 4, 4, 4]), np.array([4, 4, 4, 4]), np.array([4, 0])),
    (np.array([1, 3, 5, 0]), np.array([0, 3, 1, 5]), np.array([1, 3])),
    (np.array([2, 2, 2, 3]), np.array([2, 3, 0, 1]), np.array([1, 1])),
    (np.array([1, 4, 4, 5]), np.array([4, 4, 1, 1]), np.array([1, 2])),
    (np.array([0, 1, 2, 3]), np.array([0, 2, 1, 3]), np.array([2, 2])),
    (np.array([0, 0, 1, 1]), np.array([0, 1, 0, 1]), np.array([2, 2])),
    (np.array([3, 2, 1, 0]), np.array([0, 1, 2, 3]), np.array([0, 4])),
    (np.array([1, 2, 2, 1]), np.array([2, 1, 1, 2]), np.array([0, 4])),
    (np.array([5, 5, 5, 5]), np.array([0, 0, 0, 0]), np.array([0, 0])),
    (np.array([1, 2, 3, 4]), np.array([5, 5, 5, 5]), np.array([0, 0])),
    (np.array([2, 3, 3, 2]), np.array([2, 2, 3, 3]), np.array([2, 2])),
    (np.array([4, 3, 2, 1]), np.array([1, 2, 3, 4]), np.array([0, 4])),
    (np.array([1, 1, 1, 2]), np.array([1, 1, 2, 2]), np.array([3, 0])),
    (np.array([2, 4, 4, 2]), np.array([2, 4, 2, 4]), np.array([2, 2])),
    (np.array([0, 3, 2, 5]), np.array([5, 2, 3, 0]), np.array([0, 4]))
]

# Example test function (replace 'your_provideFeedback_function' with your actual function name)
def test_provide_feedback(feed_back_function):
    for code, guess, expected_feedback in test_cases:
        feedback = feed_back_function(code, guess)
        assert np.array_equal(feedback, expected_feedback), f"Test failed for code: {code}, guess: {guess}. Feedback: {feedback}, Expected: {expected_feedback}"
    print("All tests passed!")

