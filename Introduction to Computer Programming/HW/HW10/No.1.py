import matplotlib.pyplot as plt

def pie_chart(data):
    grouped_data = {}
    for item in data:
        if item in grouped_data:
            grouped_data[item] += 1
        else:
            grouped_data[item] = 1

    values = grouped_data.values()

    plt.pie(values, startangle=140)
    plt.axis('equal')
    plt.show()

pie_chart([3, 1, 3, 3, 2, 3, 3, 2, 3, 2, 4, 3, 3, 3, 3, 4, 3, 4, 3, 3, 3, 4, 3])