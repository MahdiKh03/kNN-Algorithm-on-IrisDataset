import math
from statistics import mode
from random import sample
import pandas as pd

data = pd.read_csv("Iris.csv")
df = data.values.tolist()

training_data = sample(df, 100)
testing_data = [item for item in df if item not in training_data]

for i in range(len(testing_data)):
    testing_data[i][0] = i + 1

for i in range(len(training_data)):
    training_data[i][0] = i + 1

# print(training_data)
# print(testing_data)
status_list = []
for item in testing_data:
    sl = item[1]
    sw = item[2]
    pl = item[3]
    pw = item[4]

    def distance(x, y, z, t):
        return round(math.sqrt((x - sl) ** 2 + (y - sw) ** 2 + (z - pl) ** 2 + (t - pw) ** 2), 3)


    list_of_distances = [(item[0], distance(item[1], item[2], item[3], item[4])) for item in training_data]


    def find_nearest(k):
        global list_of_distances
        list_of_distances.sort(key=lambda x: x[1])
        return list_of_distances[:k]


    list_of_nearest_labels = [training_data[item[0] - 1][5] for item in find_nearest(10)]
    # print("")
    # print(mode(list_of_nearest_labels))
    if mode(list_of_nearest_labels) == item[5]:
        status_list.append(True)
        # print(f"True {item[0]}")
    else:
        status_list.append(False)
        # print(f"False {item[0]}")

print(f"Accuracy: {status_list.count(True) / len(testing_data) * 100}")
# print(status_list)


# Check single example

# sl = float(input("SepalLengthCm: "))
# sw = float(input("SepalWidthCm: "))
# pl = float(input("PetalLengthCm: "))
# pw = float(input("PetalWidthCm: "))

# def distance(x, y, z, t):
#     return round(math.sqrt((x - sl) ** 2 + (y - sw) ** 2 + (z - pl) ** 2 + (t - pw) ** 2), 3)
#
#
# list_of_distances = [(item[0], distance(item[1], item[2], item[3], item[4]), item[5]) for item in training_data]
#
#
# def find_nearest(k):
#     global list_of_distances
#     list_of_distances.sort(key=lambda x: x[1])
#     return list_of_distances[:k]
#
#
# list_of_nearest_labels = [training_data[item[0] - 1][5] for item in find_nearest(10)]
# print("")
# print(mode(list_of_nearest_labels))
# print(find_nearest(10))
