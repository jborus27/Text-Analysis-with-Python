import csv

def strip(text):
    '''strip a piece of text of any special characters'''
    characters = [',', '!', '-', '"', '.', '?', "'", ':', ';']
    text = text.lower()
    for character in text:
        if character in characters:
            text = text.replace(character, '')
    return text
def create_spreadsheet(dictionary):
    '''create a spreadsheet from a dictionary'''
    with open("dalloway_spread.csv", mode='w', newline='') as file:
        fieldnames = ['word', 'frequency']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for word in dictionary:
            writer.writerow({'word': word, 'frequency': dictionary.get(word)})
    print('success')
all_words = dict()
def count_frequency(text):
    '''count frequency of every word in a piece of text'''
    file = open(text)
    stopwords_names = open('stop.en.common-names.txt','r')
    stopwords_names1 = stopwords_names.read()
    stopwords = open('stop.en.smart.txt','r')
    stopwords1 = stopwords.read()
    for line in file:
        line = strip(line)
        words = line.split()
        for word in words:
            if word not in stopwords_names1 and word not in stopwords1:
                if word not in all_words:
                    all_words[word] = 1
                else:
                    all_words[word] +=1
count_frequency('dalloway.txt')
create_spreadsheet(all_words)
def find_greatest(dictionary):
    '''find the greatest occuring word in a given dictionary'''
    temp = 0
    for item in dictionary.keys():
        if dictionary.get(item) > temp:
                temp = dictionary.get(item)
                tempword = item
##    print(tempword + ' occurs ' + str(temp) + ' times.')
                
def count_occurences(text, target):
    '''count the occurences of a specific word in a piece of text'''
    file = open(text)
    count = 0
    for line in file:
        words = line.split()
        for word in words:
            if word.lower().strip() == target:
                count = count + 1
    file.close()
    return count

def count_occurences_pronouns(text):
    '''count the occurences of different groups of pronouns in a piece of text'''
    file = open(text)
    personal_list = ["I", "it", "we", "us", "our"]
    impersonal_list = ["he", "she", "they", "them", "him", "her", "his", "hers", "its", "theirs"]
    you_list = ["your", "you"]
    frequency = dict({'personal': 0, 'impersonal': 0, 'you': 0})
    for line in file:
        line = line.strip().lower()
        words = line.split()
        for word in words:
            if word in personal_list:
                frequency['personal'] += 1
            elif word in impersonal_list:
                frequency['impersonal'] += 1
            elif word in you_list:
                frequency['you'] += 1
    print(frequency)
    file.close()
    find_greatest(frequency)

def avg_word_length(text):
    '''find the average word length of a piece of text'''
    file = open(text)
    count = 0
    avg_len = 0
    for line in file:
        line = line.strip().lower()
        words = line.split()
        for word in words:
            avg_len = avg_len + len(word)
            count = count + 1
    file.close()
    avg_len = avg_len/count
    return avg_len

import csv
present = []
past = []
def create_list_of_verbs():
    '''create a list of all the most used verbs and the tenses they belong to'''
    verbs = open('most-common-verbs-english.csv')
    next(verbs)
    for i in range(995):
        line = verbs.readline()
        line = line.split(',')
        for i in range(len(line)):
            line[i] = line[i].replace('"', '')
            line[i] = line[i].replace('\n', '')
            line[i] = line[i].replace('-', '')
        present.append(line[1])
        present.append(line[0])
        past.append(line[3])
        past.append(line[4])
verb_list = dict()
create_list_of_verbs()

def find_time(text):
    '''find the most used tense in a text'''
    file = open(text)
    frequency = dict({'past': 0, 'present': 0, 'future': 0})
    for line in file:
        line = line.strip().lower()
        words = line.split()
        for word in words:
            if word == 'will':
                frequency['future'] += 1
            elif word in present:
                frequency['present'] += 1
            elif word in past:
                frequency['past'] += 1
##    frequency['present'] = frequency['present'] - frequency['future']
    print(frequency)
    file.close()
    find_greatest(frequency)

def mood_per_line(text):
    '''finds the mood in each line of a given text'''
    file = open(text)
    poswords = open('tone/negative.txt','r')
    poswords1 = poswords.read()
    negwords = open('tone/positive.txt','r')
    negwords1 = negwords.read()
    linetone = dict({'pos': 0, 'neg': 0})
    linefreq = dict({'positive': 0, 'negative': 0})
    for line in file:
        line = line.strip().lower()
        words = line.split()
        for word in words:
            if word in poswords1 and word in negwords1:
                linefreq['positive'] += 1
                linefreq['negative'] += 1
            elif word in poswords1 and word not in negwords1:
                linefreq['positive'] += 1
            elif word in negwords1 and word not in poswords1:
                linefreq['negative'] += 1
        linefreq['positive'] += linefreq['positive']
        linefreq['negative'] += linefreq['negative']
        if (int(linefreq['positive'])) < (int(linefreq['negative'])):
            linetone['neg'] += 1
        elif (int(linefreq['positive'])) > (int(linefreq['negative'])):
            linetone['pos'] += 1
    if (int(linetone['pos'])) < (int(linetone['neg'])):
        print('tone is negative')
    elif (int(linetone['pos'])) > (int(linetone['neg'])):
        print('tone is positive')
    print(linefreq)
    file.close()
