import sys
import csv
import os

# @TODO: Add random function, so the input is not always the same

# @description Creates dictionary data structure.
# @param filename File name with all words. First column is word in foreign language and second column in known language (English)
# @param dictionary Dictionary withwords in foreign language (value), known language (key value)
def TestFirstColumn(filename, dictionary):
    again = {}
    with open(filename, 'rb') as csvfile:
        alldata = csv.reader(csvfile, delimiter=';')
        for row in alldata:
            dictionary[row[1]] = row[0]
    again = QuestionMe(dictionary)
    while len(again) != 0:
        again = QuestionMe(again)

# @description Shows dictionary key value and waits for the input and shows if the input is correct.
# @param dictionary Dictionary withwords in foreign language, known language
def QuestionMe(dictionary):
    again = {}
    for word in dictionary.keys():
        checkThis = raw_input(str(word + ": "))
        print str(word + ": " + dictionary[word] + " --> " + str(checkThis.lower()==dictionary[word].lower()))
        if checkThis.lower() != dictionary[word].lower():
            again[word] = dictionary[word]
    print "End of dictionary [" + str(len(again)) + " / " + str(len(dictionary)) + "]"
    return again

def main():
    dictionary = {}
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    while True:
        TestFirstColumn(str(sys.argv[1]), dictionary)
        print "Full dictionary starts again"


if __name__ == '__main__':
    main()
