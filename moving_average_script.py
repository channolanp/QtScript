from collections import deque
import matplotlib.pyplot as plt

def main(config):
    """An example of a script that performs a moving average with option to
    debounce

    Args:
        config (dict): Config that matches the UI elements added to QtScript.

    Returns:
        None
    """
    '''
    Extract configurations, use these instead of something like...
    file_path = myfile.csv
    window = 50
    with_debounce = true
    debounce_trigger = 1.0
    debounce_window = 10
    '''
    file_path = config['Target File']
    window = config['Filter Window']
    with_debounce = config['Debounce Signal']
    debounce_trigger = config['Debounce Value']
    debounce_window = config['Debounce Window']

    data = []
    with open(file_path) as f:
        data = [float(value) for value in f.readlines()[1:]]
    filtered = filter(data,window)
    output = filtered
    if with_debounce:
        start_index = find_start(filtered,debounce_window,debounce_trigger)
        stop_index = find_end(filtered,debounce_window,debounce_trigger)
        output = filtered[start_index:stop_index]
    plt.plot(output)
    plt.show()

def filter(array, window):
    """A simple moving average filter

    I wrote this script for a quick real-life example as moving average filters
    are fairly common to mock a low pass filter. This is one method of handling
    low pass filters, which I've used due to better handling of live data.
    I understand that using convolution is probably faster in this case as it is
    post processing, but this was meant to be a quick example and I already knew
    how to do it this way.

    Args:
        array (list-like): The data to filter, can technically be any iterable
        of numeric values
        window (int): The filtering window size

    Returns:
        list: the filtered data set

    """
    q = deque()
    running_sum = 0
    moving_average = []
    for value in array:
        if len(q) > window:
            running_sum = running_sum - q.popleft()
        q.append(value)
        running_sum = running_sum + value
        moving_average.append(running_sum/len(q))
    return moving_average

def find_start(array, window, minimum):
    """Simple debounce function going left to right.

    Args:
        array (list-like): The data to parse, can technically be any iterable
        window (int): How many consecutive values to be a real trigger
        minimum (float): The minimum value to count towards the window above

    Returns:
        int: The index where the start position is

    """
    running_counter = 0
    for index in range(len(array)):
        if array[index] >= minimum:
            running_counter = running_counter + 1
        else:
            running_counter = 0
        if running_counter >= window:
            return index - window
    return -1

def find_end(array, window, minimum):
    """Simple debounce function going right to left.

    Args:
        array (list-like): The data to parse, can technically be any iterable
        window (int): How many consecutive values to be a real trigger
        minimum (float): The minimum value to count towards the window above

    Returns:
        int: The index where the end position is

    """
    running_counter = 0
    for index in reversed(range(len(array))):
        if array[index] >= minimum:
            running_counter = running_counter + 1
        else:
            running_counter = 0
        if running_counter >= window:
            return index + window
    return -1
