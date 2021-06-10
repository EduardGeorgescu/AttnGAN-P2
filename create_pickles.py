import pickle
import os

FILEPATH_DIR = "/home/edy/Desktop/RecipeQA-dataAugmentation/"
FILEPATH_SPLIT = FILEPATH_DIR + "RecipeQA_split/"
FILEPATH_SPLIT_TEXT = FILEPATH_SPLIT + "text/"

list_files = os.listdir(FILEPATH_SPLIT_TEXT)
list_files = [x.split(".txt")[0] for x in list_files]
list_files = [x for x in list_files if x[0] != '-']
list_files = sorted(list_files)

length_original = len(list_files)
print(length_original)

new_train_len = int(length_original * 8 / 10)
new_test_len = int(length_original - new_train_len)

print(new_train_len)
print(new_test_len)

new_train = list_files[:new_train_len]
new_test = list_files[-new_test_len:]

print(len(new_train))
print(len(new_test))

# # Check if we have any duplicates.
# for k in new_test:
#     if k in new_train:
#         print(True)

pickle.dump(new_train, open("new_train_recipeqa.pickle", "wb"), protocol=2)

pickle.dump(new_test, open("new_test_recipeqa.pickle", "wb"), protocol=2)


# prev_test = pickle.load(open("prev_test_filenames.pickle", "rb"))
#
# length_original = len(prev_test)
#
# print (length_original)
#
# new_train_len = (int) (length_original * 8 / 10)
# new_test_len = (int) (length_original - new_train_len)
#
# print (new_train_len)
# print (new_test_len)
#
# new_train = prev_test[:new_train_len]
# new_test = prev_test[-new_test_len:]
#
# print (len(new_train))
# print (len(new_test))
#
# # for k in new_test:
# #     if k in new_train:
# #         print (True)
# #
# # for k in new_test:
# #     print(k)

# pickle.dump(new_train, open("new_train_recipeqa.pickle", "wb"), protocol=2)
#
# pickle.dump(new_test, open("new_test_recipeqa.pickle", "wb"), protocol=2)
