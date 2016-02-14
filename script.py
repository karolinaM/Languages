import sys
import csv
import os

# @TODO: Add random function, so the input is not always the same

# @description Creates dictionary data structure.
# @param filename File name with all words. First column is word in foreign language and second column in known language (English)
# @param dictionary Dictionary withwords in foreign language (value), known language (key value)
def TestFirstColumn(filename, dictionary):
    with open(filename, 'rb') as csvfile:
        alldata = csv.reader(csvfile, delimiter=';')
        for row in alldata:
            dictionary[row[1]] = row[0]
    QuestionMe(dictionary)

# @description Shows dictionary key value and waits for the input and shows if the input is correct.
# @param dictionary Dictionary withwords in foreign language, known language
def QuestionMe(dictionary):
    while True:
        for word in dictionary.keys():
            checkThis = raw_input(str(word + ": "))
            print str(word + ": " + dictionary[word] + " --> " + str(checkThis==dictionary[word]))
        print "End of file"

def main():
    dictionary = {}
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    TestFirstColumn(str(sys.argv[1]), dictionary)


if __name__ == '__main__':
    main()
