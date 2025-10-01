#lab 08
#jules borusiewicz
#11/21/2024

#Q1
def print_first_line():
    '''print the first line in the training document'''
    file = open('training.txt')
    print(file.readline())
    file.close()

#Q2
def count_lines(filename):
    '''counts the lines in a given file'''
    file = open(str(filename))
    count = 0
    line = file.readline()
    while line != '':
        count = count + 1
        line = file.readline()
    file.close()
    return count
    print(filename + ' has ' + str(count) + ' lines.')
    file.close()
##count_lines('training.txt')


#Q4
def get_rating(line):
    '''gets the rating of a full review'''
    res = int(line[0])
    return res
def test_get_rating():
    '''tests the get rating function'''
    assert get_rating('4 I laughed, I cried, it was better than cats.') == 4
    assert get_rating('0 Two thumbs down.') == 0
    print('get_rating passed tests')
##test_get_rating()
#Q5
def get_review(line):
    '''gets the review portion of a full review'''
    res = line[2:]
    return res
#Q6
def test_get_review():
    '''tests the get review function'''
    assert get_review('4 I laughed, I cried, it was better than cats.') == 'I laughed, I cried, it was better than cats.'
    assert get_review('0 Two thumbs down.') == 'Two thumbs down.'
    print('get_review passed tests')
##print(get_review('4 I laughed, I cried, it was better than cats.'))
##test_get_review()
#Q7
def remove_punctuation(text):
    """Return a copy of the given text with all characters other than alphabetic and
    space characters removed."""
    valid_chars = []
    for c in text:
        if c.isalpha() or c == ' ':
            valid_chars.append(c)
    new_text = ''.join(valid_chars)
    return new_text
def clean_review(review):
    res = review.strip()
    res = remove_punctuation(res)
    res = res.lower()
    return res
##print(clean_review(' TWo thuMbs dowN '))
def test_clean_review():
    assert clean_review(
        'I lauGHed I CrieD') == 'i laughed i cried', 'review text is not all lowercase'
    assert clean_review(
        ' Two ThumBS DowN ') == 'two thumbs down', 'spaces at start and end not removed'
    assert clean_review(
        ' This "1" wasn`t BAD!!!! ') == 'this  wasnt bad', 'non alphabetic characters not removed'
    print('clean_review passed tests')
##test_clean_review()

#Q8
def average_rating_v1(filename):
    count = int(count_lines(filename))
    f = open(filename)
    ratings = []
    for i in range(count):
        line = f.readline()
        temprating = get_rating(line)
        ratings.append(temprating)
    count2=0
    res=0
    for i in range(len(ratings)):
        res = res + int(ratings[i])
    res = res/len(ratings)
    f.close()
    return res
def test_average_rating_v1():
    assert round(average_rating_v1('toy.txt'), 4) == 2.8, 'failed on toy.txt'
    assert round (average_rating_v1('training.txt'), 4) == 2.0627, 'failed on training.txt'
    print('test_average_rating_v1 passed tests')
##test_average_rating_v1()

#Q9
def count_occurrences(filename, target):
    f = open(filename)
    count = int(count_lines(filename))
    res = 0
    instance = 0
    for i in range(count):
        line = clean_review(f.readline())
        if target in line:
            res = res + 1
    return res
##print(count_occurrences('toy.txt', 'wonderful'))
def test_count_occurrences():
    assert count_occurrences('toy.txt', 'wonderful') == 3
    assert count_occurrences('toy.txt', 'to') == 2
    assert count_occurrences('toy.txt', 'asdfghjk') == 0
    assert count_occurrences('toy.txt', 'imax') == 1
    assert count_occurrences('training.txt', 'awesome') == 2
    print('count_occurrences passed tests')
##test_count_occurrences()

#Q10
def average_rating_v2(filename):
    f=open(filename)
    count=int(count_lines(filename))
    res = 0
    ratings = []
    for i in range(count):
        line = clean_review(f.readline())
        rating = 0
        if 'wonderful' in line:
                temprating = get_rating(line)
                ratings.append(temprating)
    for i in range(len(ratings)):
        res = res + int(ratings)
    res = res/len(ratings)
    f.close()
    return res
def test_average_rating_v2():
    assert round(average_rating_v1('toy.txt'), 4) == 2.8, 'failed on toy.txt'
    assert round(average_rating_v1('training.txt'), 4) == 2.0627, 'failed on training.txt'
    print('test_average_rating_v2 passed tests')
##test_average_rating_v2()

#Q11
def average_rating(filename,target):
    f=open(filename)
    ratings = []
    for line in f:
        review = clean_review(line)
        if target in review:
            temprating = get_rating(line)
            ratings.append(temprating)
    res = 0
    for i in range(len(ratings)):
        res = res + int(ratings[i])
    res = res/len(ratings)
    f.close()
    return res
    
def test_average_rating():
    assert round(average_rating('toy.txt', 'wonderful'), 4) == 3.6667
    assert round(average_rating('training.txt', 'wonderful'), 4) == 3.4167
    assert round(average_rating('training.txt', 'awesome'), 4) == 4.0000
    assert round(average_rating('training.txt', 'boring'), 4) == 1.1429
    assert round(average_rating('training.txt', 'really'), 4) == 1.7557
    print('test_average_rating passed tests')
test_average_rating()
