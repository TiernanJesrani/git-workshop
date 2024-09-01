from .series import Series

class DataFrame:
    """
    A class to represent a DataFrame, which is a collection of Series.
    """

    def __init__(self, data: list[Series]):
        """
        Initialize the DataFrame with a list of Series.

        :param data: A list of Series objects.
        """
        self.data = data
        self.columns = [series.name for series in data]
        self._validate()


    def _validate(self):
        """
        Validate that the series names are unique and all series have the same length.
        """
        # Check if all series have the same length
        if len(set(len(series.data) for series in self.data)) != 1:
            raise ValueError("All Series in the DataFrame must have the same length.")
        # Check if column names are unique
        if len(self.columns) != len(set(self.columns)):
            raise ValueError("Column names must be unique.")


    def __repr__(self) -> str:
        """Return a string representation of the DataFrame."""
        column_str = " | ".join(self.columns)
        rows_str = "\n".join(" | ".join(map(str, row)) for row in zip(*[series.data for series in self.data]))
        return f"{column_str}\n{rows_str}"


    def shape(self) -> tuple[int, int]:
        """
        Return the shape of the DataFrame (rows, columns).
        """
        return (len(self.data[0].data), len(self.columns))


    def head(self, n: int = 5) -> DataFrame:
        """
        Returns a new DataFrame with the first n rows.

        :param n: Number of rows to return.
        :return: A new DataFrame with the first n rows.
        """
        
        # TODO: Person 1 - Implement this function


    def tail(self, n: int = 5) -> DataFrame:
        """
        Returns a new DataFrame with the last n rows.

        :param n: Number of rows to return.
        :return: A new DataFrame with the last n rows.
        """
        # TODO: Person 2 - Implement this function


    def add_column(self, series: Series) -> None:
        """
        Add a new Series (column) to the DataFrame.

        This operation is done in-place.

        :param series: The Series object to add as a new column.
        """
        # TODO: Person 1 - Implement this function


    def drop_column(self, column_name: str) -> None:
        """
        Drop a column from the DataFrame.

        This operation is done in-place.

        :param column_name: The name of the column to drop.
        """
        # TODO: Person 2 - Implement this function


    def get_column(self, column_name: str) -> Series:
        """
        Returns the Series for a specific column.

        :param column_name: The name of the column to retrieve.
        :return: The Series object for the specified column.
        """
        # TODO: Person 1 - Implement this function


    def set_column(self, column_name: str, values: list[float]) -> None:
        """
        Set the data for a specific column.

        This operation is done in-place.

        :param column_name: The name of the column to set.
        :param values: A list of data to set for the specified column.
        """
        # TODO: Person 2 - Implement this function


    def remove_duplicates(self) -> None:
        """
        Removes duplicate rows from the DataFrame.

        This operation is done in-place.
        """
        # TODO: Person 1 & 2 - Implement this function
        # Either code together or have one person code and the other review
        # If coding together, use pair programming & co-author the commit (git commit -m "message" -m "Co-authored-by: name <email>")
        # If reviewing, leave comments on what you think can be improved
        seen = set()
        unique_rows = []
        
        rows = zip(*[series.data for series in self.data])
        
        for row in rows:
            if row not in seen:
                seen.add(row)
                unique_rows.append(row)
        
        # Update the series data with unique rows
        for series in self.data:
            series.data = [row[self.data.index(series)] for row in unique_rows]

    def combine_columns(self, col1: str, col2: str, new_col: str, operation: callable) -> None:
        """
        Combines two columns in the DataFrame based on a specified operation.

        This operation is done in-place.

        :param col1: The name of the first column.
        :param col2: The name of the second column.
        :param new_col: The name of the new column to create.
        :param operation: A function that takes two arguments and returns a value (e.g., addition, multiplication).
        """
        # TODO: Person 1 & 2 - Implement this function
        # Either code together or have one person code and the other review
        # ...

            # Retrieve the two series to combine
        series1 = next(series for series in self.data if series.name == col1)
        series2 = next(series for series in self.data if series.name == col2)
        
        if len(series1.data) != len(series2.data):
            raise ValueError(f"Columns '{col1}' and '{col2}' must have the same length.")
        
        new_data = [operation(val1, val2) for val1, val2 in zip(series1.data, series2.data)]
        new_series = Series(name=new_col, data=new_data)
        
        self.data.append(new_series)
        self.columns.append(new_col)


    def concatenate_vertically(self, other: DataFrame) -> None:
        """
        Concatenates another DataFrame to the current DataFrame vertically (adding rows).

        This operation is done in-place.

        :param other: Another DataFrame object to concatenate vertically.
        """
        # TODO: Person 1 - Implement this function
        for i in range(len(self.data)) :
            self.data[i].extend(other.data[i].data)

    def concatenate_horizontally(self, other: DataFrame) -> None:
        """
        Concatenates another DataFrame to the current DataFrame horizontally (adding columns).

        This operation is done in-place.

        :param other: Another DataFrame object to concatenate horizontally.
        """
        self.data.extend(other.data)
        self.columns.extend(other.data)
        # TODO: Person 2 - Implement this function


    def remove_na(self) -> DataFrame:
        """Return DataFrame that has all rows containing NaN values removed.
        NaN means Not a Number and is when values are missing or undefined.

        This operation is NOT done in-place.
        """
        # TODO: Person 1 - Implement this function

    def replace_na(self, value: float) -> DataFrame:
        """Return DataFrame that replaces NaN with the specific value.
        NaN means Not a Number and is when values are missing or undefined.

        This operation is NOT done in-place.

        :param value: New value that replaces NaN."""
        # TODO: Person 2 - Implement this function

    def apply(self, func, column: str = None) -> DataFrame:
        """
        Applies a function to a specific column or all elements in the DataFrame.

        This operation is NOT done in-place.

        :param func: A function to apply to each element.
        :param column: Name of the column to apply the function to (optional).
        """
        # TODO: Person 1 & 2 - Implement this function
        # Either code together or have one person code and the other review
        # ...
