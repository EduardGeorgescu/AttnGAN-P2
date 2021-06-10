import json
import nltk
from nltk.corpus import stopwords

from shutil import copyfile


def main():
    # Possible types: train, val, test.
    CRT_TYPE = "val"
    FILEPATH_DIR = "/home/edy/Desktop/RecipeQA-dataAugmentation/"
    FILEPATH_JSON = FILEPATH_DIR + "RecipeQA/" + CRT_TYPE + ".json"
    FILEPATH_IMAGES = FILEPATH_DIR + "RecipeQA/images-qa/" + CRT_TYPE + "/images-qa/"

    FILEPATH_SPLIT = FILEPATH_DIR + "RecipeQA_split/"
    FILEPATH_SPLIT_IMAGES = FILEPATH_SPLIT + "images/"
    FILEPATH_SPLIT_TEXT = FILEPATH_SPLIT + "text/"

    with open(FILEPATH_JSON, 'r', encoding='utf8', errors='ignore') as f:
        data = json.load(f)

    count = 0
    recipe_set = set()
    answer_set = set()
    tasks_set = set()
    question_set = set()

    for i in data['data']:
        answer = i['answer']
        task = i['task']

        # if task != "visual_ordering":
        if task == "textual_cloze":
            # print('\n\n')
            # print("Recipe id:", i['recipe_id'])
            for j in range(len(i['context'])):

                # print("Body:", i['context'][j]['body'])
                # print("Task:", task)
                crt_text = i['context'][j]['body']
                for image_name in i['context'][j]['images']:
                    # Errors in the dataset.
                    image_name = image_name.replace("*easy*", "_easy_")

                    path_image_src = FILEPATH_IMAGES + image_name
                    print("Image path src:", path_image_src)

                    path_image_dst = FILEPATH_SPLIT_IMAGES + image_name
                    print("Image path dst:", path_image_dst)

                    path_text_dst = FILEPATH_SPLIT_TEXT + image_name.split(".jpg")[0] + ".txt"
                    print("Text path dst:", path_text_dst)
                    print("\n")

                    # Write the text descriptions.
                    with open(path_text_dst, "a") as out:
                        out.write(crt_text)

                    # Copy the images.
                    copyfile(path_image_src, path_image_dst)

            # print("Answer:", i['choice_list'][answer])

            count += 1
            recipe_set.add(i['recipe_id'])
            answer_set.add(i['choice_list'][answer])
            # question_set.add(i['question_text'])

            tasks_set.add(task)

            # break

    print("\n\n\n")
    print("TYPE:", CRT_TYPE)
    print("Total number:", count)
    print("Recipe set size:", len(recipe_set))
    print("Answer set size:", len(answer_set))

    # print("Questions set:", question_set)
    print("Tasks set:", tasks_set)


if __name__ == "__main__":
    main()
