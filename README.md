# Charlock Holmes
[![Build Status](https://travis-ci.org/xtao/PyCharlockHolmes.png)](https://travis-ci.org/xtao/PyCharlockHolmes)

Character encoding detecting library for Python using [ICU](http://site.icu-project.org/) and libmagic. Inspired by [Charlock Holmes](https://raw.github.com/brianmario/charlock_holmes)

## Dependency
1. icu
2. file(libmagic)

### Gentoo
    emerge -av dev-libs/icu
    emerge -av sys-apps/file

### Ubuntu
    apt-get install libicu-dev
    apt-get install libmagic-dev

### Brew
    brew install icu4c
    brew install libmagic
    export ICUI18N="/usr/local/Cellar/icu4c/xx" # Replace "xx" as the version of your icu
    export MAGIC="/usr/local/Cellur/libmagic/xx" # Replace "xx" as the version of your libmagic

## Install

    python setup build
    python setup install

## Usage

    from charlockholmes import detect
    file = open('test.txt')
    content = file.read()
    print detect(content)
