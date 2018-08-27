import loader
import network

training_data, validation_data, test_data = loader.load_data_wrapper()
net = network.Network([784, 20, 10])

tr_data = list(training_data)
te_data = list(test_data)

# row = tr_data[49990][0]
# j=0

# print("")
# print("")
# for i in row:
#     char = 1 if (i > 0.5) else 0
#     print(char, end="")
#     j+=1
#     if (j % 28 == 0):
#         print("")

# print("")
# print("")
# quit()
net.SGD(tr_data, 30, 10, 3.0, test_data=te_data)