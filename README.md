# Charlock Holmes

Character encoding detecting library for Python using [ICU](http://site.icu-project.org/) and libmagic. Inspired by [Charlock Holmes](https://raw.github.com/brianmario/charlock_holmes)

## Install

    python setup build
    python setup install

## Usage

    from charlockholmes import detect
    file = open('test.txt')
    content = file.read()
    print detect(content)
