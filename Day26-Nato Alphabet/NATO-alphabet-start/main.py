# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd
Data_csv = pd.read_csv("nato_phonetic_alphabet.csv")
New_dict = {Names.letter: Names.code for (index,Names) in Data_csv.iterrows()}



Word = input("Enter a word: ")
words = []


try:
    for letter in Word:
        new_letter = letter.capitalize()
        words.append(New_dict[new_letter])
except KeyError:
    print("Please type a word")
else:
    print(words)







