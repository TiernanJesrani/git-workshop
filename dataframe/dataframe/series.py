from collections import Counter
class Series:
    """
    A class to represent a Series, a one-dimensional column (array) with a name.
    """

    def __init__(self, data: list[float], name: str):
        """
        Initialize the Series with data and a name.

        :param data: A list of numerical data.
        :param name: The name of the series (e.g., column name).
        """
        self.data = data
        self.name = name


    def __repr__(self) -> str:
        """Return a string representation of the Series."""
        return f"Series(name={self.name}, data={self.data})"


    def sum(self) -> float:
        """Return the sum of the data in the series."""
        return sum(self.data)
        # TODO: Person 3 - Implement this function


    def max(self) -> float:
        """Return the maximum value in the series."""
        return max(self.data)
        # TODO: Person 4 - Implement this function


    def min(self) -> float:
        """Return the minimum value in the series."""
        return min(self.data)
        # TODO: Person 3 - Implement this function


    def mean(self) -> float:
        """Return the mean of the data in the series."""
        # TODO: Person 4 - Implement this function

    def mode(self) -> float:
        """Return the mode of the data in the series."""
        data_counts = Counter(self.data)  # Count the frequency of each element
        max_count = max(data_counts.values())  # Find the maximum frequency
        modes = [k for k, v in data_counts.items() if v == max_count]  # Find all elements with max frequency
    
        if len(modes) == 1:
            return modes[0]  # Return the single mode value
        else:
            return modes 
        # TODO: Person 3 - Implement this function

    def unique_val(self) -> list:
        """Return the unique values in the series."""
        # TODO: Person 4 - Implement this function

    def contains(self, value: float) -> bool:
        """
        Return if the series contains the value.

        :param value: The specific value being checked.
        """

        return value in self.data
        # TODO: Person 3 - Implement this function

    def replace(self, current_val: float, new_val: float) -> Series:
        """Return a new Series with a specific current value replaced with a new value.

        :param current_val: The current value. 
        :param new_value: The new value that will replace current value.
        """
        # TODO: Person 4 - Implement this function

    def apply(self, func) -> Series:
        """
        Apply a mapping function to each element in the series and return a new Series.

        :param func: A function to apply to each element.
        :return: A new Series with the function applied.
        """

        new_data = [func(x) for x in self.data]
        return Series(new_data, self.name)
        # TODO: Person 3 - Implement this function
