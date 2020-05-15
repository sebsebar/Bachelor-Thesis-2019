import pandas as pd
import os
import numpy as np

path = os.getcwd()

newWords = ['obstinate', 'Word2']

total_df = pd.read_csv(path + '/WordList_total.txt', sep='\t')

newWords = total_df['Word'].tolist()
total_list = []

df_1 = pd.read_csv(path + '/1_WordList_ValHighAroHigh.csv')
df_2 = pd.read_csv(path + '/2_WordList_ValHighAroLow.csv')
df_3 = pd.read_csv(path + '/3_WordList_ValLowAroHigh.csv')
df_4 = pd.read_csv(path + '/4_WordList_ValLowAroLow.csv')

list_df = [df_1, df_2, df_3, df_4]

for word in newWords:
    present = False
    for eachIteration in list_df:
        for i in range(len(eachIteration)):
            wordInDf = eachIteration['Word'].iloc[i]
            if word == wordInDf:
                present = True
    if not present:
        total_list.append(word)

final_words = np.random.choice(np.asarray((total_list)), 60, replace=False)

final_df = pd.DataFrame({'Study': final_words[:50]})
final_df['Distractor'] = list(final_words[50:]) * 5
# 10 words that will form the 2AFC pair are repeated 5 times to align the df

final_df.to_csv(path + '/Training.txt', sep='\t')
