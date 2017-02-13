import os
import sys
import glob
import numpy
import shutil
import operator
import patoolib
import matplotlib.pyplot as plt
from pprint import pprint


def get_config():
    return {
        'archive_formats': [
            'zip',
            'tar',
            'rar',
        ],
        'text_formats': [
            'txt',
        ],
        'top_num': 20,  # change the number here to see top n
        'tmp_path': './tmp/',
    }


def sanitize_path(path):
    """
    sanitize path string
    :param path:
    :return:
    """
    return os.path.abspath(path)


def validate_path(path):
    """
    path validator
    :param path:
    :return:
    """
    try:
        return sanitize_path(path)
    except:
        exit("Invalid path.")


def trim_string_to_words(string):
    """
    remove special character from string
    :param string:
    :return:
    """
    string = string.replace('_', ' ')  # convert underscore _ to space
    return ''.join(char for char in string if char.isalpha() or char == ' ')


def stat_word(array_words, dictionary):
    """
    add occurrence of word to dictionary
    :param array_words:
    :param dictionary:
    :return:
    """
    for word in array_words:
        word = word.lower()  # string in lower case
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1


def scan_file(file, dictionary):
    """
    scans text in a txt file and populate a dictionary
    :param file:
    :param dictionary:
    :return:
    """
    with open(file, 'rU') as f:
        for line in f:
            array_words = trim_string_to_words(line).split()
            if array_words:
                stat_word(array_words, dictionary)


def scan_text_files_in_directory(path, dictionary):
    """
    search and scan text files in directory and stat into dictionary
    :param path:
    :param dictionary:
    :return:
    """
    global config
    text_formats = config['text_formats']

    if not text_formats:
        exit("No text file format specified.")

    # do for each supported text formats
    for extension in text_formats:
        text_path = sanitize_path('%s%s%s' % (path, '/**/*.', extension))
        file_list = glob.glob(text_path, recursive=True)
        print('%s %d \".%s\" %s' % ('Found:', len(file_list), extension, 'files in specified directory.'))

        # scan each text file
        for file_handle in file_list:
            print("%s %s" % ('Scanning', file_handle))
            try:
                scan_file(file_handle, dictionary)
            except:
                print("Unable to scan %s" % file_handle)


def draw_histogram(dictionary):
    """
    draws histogram of the top (config['top_num'])(sorted by highest value from hi to lo) entries
    :param dictionary:
    :return:
    """
    global config

    print("\nDrawing Histogram for the top %d frequently used words." % config['top_num'])

    # init x,y axis
    x = []
    y = []

    # slice top num of entries
    i = 1
    for k, v in dictionary:
        if i > config['top_num']:
            break
        i += 1
        x.append(k)
        y.append(v)
        #print(k, v)

    # horizontal plot starts from bottom
    x.reverse()
    y.reverse()
    #print(x, y)

    # set ticks
    x_ticks = numpy.arange(len(x))

    # bar graph config
    plt.barh(x_ticks, y, height=0.8, align="center", tick_label=x)
    plt.title("Top %d frequently used words." % config['top_num'])
    plt.xlabel("Frequency")

    # show graph
    plt.show()


def extract_archives(path):
    """
    extract files in archives to temp folder
    :param path:
    :return:
    """
    global config
    archive_formats = config['archive_formats']

    if not archive_formats:
        exit("No archive file format specified.")

    # do for each supported text formats
    for extension in archive_formats:
        path = sanitize_path('%s%s%s' % (path, '/**/*.', extension))
        file_list = glob.glob(path, recursive=True)
        print('%s %d \".%s\" %s' % ('\nFound:', len(file_list), extension, 'files in specified directory.'))

        if not file_list:
            continue

        # extract each archives
        for file_handle in file_list:
            patoolib.extract_archive(file_handle, outdir=config['tmp_path'])


def clean_tmp():
    """
    rm tmp folder
    :return:
    """
    global config
    if not os.path.isdir(sanitize_path(config['tmp_path'])):
        return
    shutil.rmtree(sanitize_path(config['tmp_path']))


# main
if __name__ == '__main__':

    # input
    try:
        in_path = validate_path(sys.argv[1])
    except:
        exit("Please specify the path, example usage: python text_scanner.py res/simple ")
    print('%s %s' % ('\nScanning Directory: ', in_path))

    # config
    config = get_config()

    # init dictionary
    base_dictionary = {}

    # scan text files in input directory
    scan_text_files_in_directory(in_path, base_dictionary)

    # extract archives
    extract_archives(in_path)

    # scan temp folder
    print('%s %s' % ('\nScanning extracted files in: ', sanitize_path(config['tmp_path'])))
    scan_text_files_in_directory(sanitize_path(config['tmp_path']), base_dictionary)

    # clean up archives
    clean_tmp()

    # post process dictionary
    sorted_dictionary = sorted(base_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    # pprint(sorted_dictionary)

    # draw graph
    draw_histogram(sorted_dictionary)



