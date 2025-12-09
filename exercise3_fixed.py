import csv
import numpy as np
import matplotlib.pyplot as plt

def plot_data(csv_file_path: str):
    """
    This code plots the precision-recall curve based on data from a .csv file,
    where precision is on the x-axis and recall is on the y-axis.
    It it not so important right now what precision and recall means.

    :param csv_file_path: The CSV file containing the data to plot.

    FIXED: The axes were swapped - precision should be on x-axis, recall on y-axis
    """
    # load data
    results = []
    with open(csv_file_path) as result_csv:
        csv_reader = csv.reader(result_csv, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            results.append(row)
        results = np.stack(results)

    # plot precision-recall curve
    # FIXED: Column 0 is precision (x-axis), Column 1 is recall (y-axis)
    plt.plot(results[:, 0], results[:, 1])
    plt.ylim([-0.05, 1.05])
    plt.xlim([-0.05, 1.05])
    plt.xlabel('Precision')  # FIXED: Changed from 'Recall' to 'Precision'
    plt.ylabel('Recall')     # FIXED: Changed from 'Precision' to 'Recall'
    plt.show()


# Test the fixed function
if __name__ == "__main__":
    # Generate test data
    f = open("data_file.csv", "w")
    w = csv.writer(f)
    _ = w.writerow(["precision", "recall"])
    w.writerows([[0.013, 0.951],
                 [0.376, 0.851],
                 [0.441, 0.839],
                 [0.570, 0.758],
                 [0.635, 0.674],
                 [0.721, 0.604],
                 [0.837, 0.531],
                 [0.860, 0.453],
                 [0.962, 0.348],
                 [0.982, 0.273],
                 [1.0, 0.0]])
    f.close()
    
    plot_data('data_file.csv')
