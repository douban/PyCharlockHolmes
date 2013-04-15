#!/usr/bin/env python

# Test PyCharlockHolmes
#

from charlockholmes import detect

TEST_FILES = {
    "py": [
        "file/test.py",
        {'confidence': 43, 'type': 'text', 'language': 'en', 'encoding': 'ISO-8859-1'}
    ],
    "py1": [
        "file/test1.py",
        {'confidence': 80, 'type': 'text', 'encoding': 'UTF-8'}
    ],
    "lisp": [
        "file/test.lisp",
        {'confidence': 39, 'type': 'text', 'language': 'da', 'encoding': 'ISO-8859-1'}
    ],
    "txt": [
        "file/test.txt",
        {'confidence': 16, 'type': 'text', 'language': 'en', 'encoding': 'ISO-8859-1'}
    ],
    "c": [
        "file/test.c",
        {'confidence': 50, 'type': 'text', 'language': 'en', 'encoding': 'ISO-8859-1'}
    ],
    "sh": [
        "file/test.sh",
        {'confidence': 21, 'type': 'text', 'language': 'es', 'encoding': 'ISO-8859-1'}
    ],
    "elf": [
        "file/test",
        {'confidence': 100, 'type': 'binary'}
    ],
    "bz2": [
        "file/test.tar.bz2",
        {'confidence': 100, 'type': 'binary'}
    ],
    "gz": [
        "file/test.tar.gz",
        {'confidence': 100, 'type': 'binary'}
    ],
}

for test in TEST_FILES:
    file_path = TEST_FILES[test][0]
    file_result = TEST_FILES[test][1]
    content = open(file_path).read()
    test_result = detect(content)
    if test_result == file_result:
        print file_path + ": OK"
    else:
        print file_path + ": ERROR"
