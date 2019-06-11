"""Predicting Solar Intensity Using Weather Data

June 2019
Alex Kim and Dane Stocks

This module defines common utility functions, especially regarding data
cleaning and structuring.
"""
import numpy as np


def read_data(data_paths):
    """Read the data files and combine them into a single dataset.

    Args:
        data_paths (list): Strings of the paths to the data files.

    Returns:
        A single NumPy array consisting of the data from all datasets
    """
    # Read the first data file
    first_path = data_paths[0]
    full_data = np.genfromtxt(first_path, delimiter=',', skip_header=2,
            names=True)

    # Append all remaining data files
    num_files = len(data_paths)
    for i in range(1, num_files):
        path = data_paths[i]
        new_data = np.genfromtxt(path, delimiter=',', skip_header=2,
                names=True)
        full_data = np.hstack((full_data, new_data))

    return full_data


def trim_vars(data):
    """Trim extraneous variables and observations from the data.

    Args:
        data (ndarray): The full unprocessed dataset

    Returns:
        The full dataset with extraneous variables and observations
        trimmed off.
    """
    # Remove all columns with names in `rm_vars`
    rm_vars = ['DHI', 'DNI', 'Clearsky_DHI', 'Clearsky_DNI',
            'Clearsky_GHI', 'Fill_Flag']
    var_names = list(data.dtype.names)
    keep_vars = [_ for _ in var_names if _ not in rm_vars]
    data_trimmed = data[:, keep_vars]
    return data_trimmed


def generate_ids(data):
    """Generate a unique ID for each row of the data. Each ID encodes
    the date and time of the solar intensity measurement.
    """
    pass


def recode_time(data):
    """Recode the 'Hour' column to encapsulate both the hour and the
    minute, and then remove the 'Minute' column.

    Args:
        data (ndarray): The full unprocessed dataset

    Returns:
        The full dataset with extraneous variables and observations
    """
    # Recode 'Hour'
    data['Hour'] = data['Hour'] + data['Minute'] / 60

    # Remove 'Minute'
    var_names = list(data.dtype.names)
    keep_vars = [_ for _ in var_names if _ != 'Minute']
    data_trimmed = data[:, keep_vars]
    return data_trimmed


def featurize(data, n_time_points):
    """
    """
    pass


def cluster_transform():
    """Transform the data for k-means clustering.

    This function generates a transformed dataset where each row
    corresponds to a day, and each column corresponds to a time during
    the day (48 columns total). The cells are populated with solar
    intensity values. All predictor variables (weather data) are ignored
    here.

    Args:

    Returns:
    """


def split_data():
    """
    """
    pass


def read_and_preprocess():
    """
    """
    data_paths = ['data/105130_36.17_-115.14_2016.csv',
            'data/105130_36.17_-115.14_2017.csv']
    dat = read_data(data_paths)
    dat = trim_vars(dat)

    return dat


if __name__ == "__main__":
    pass
