#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
#
#  DisReplacement.py
#
#  Takes a German dictionary and replaces the
#  character sequence 'dis' with '**DISS**'
#  Finally it saves the string as a Markdown file
#  which then can be compiled as a PDF with Pandoc.
#
#  Copyright 2015 Axel Dürkop <axel.duerkop@tu-harburg.de>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import re
import random

#  German dictionary from http://sourceforge.net/projects/germandict/
dic = open('german-utf8.dic')
result = open('result.markdown', 'w')
words = dic.read()


def randomize_list(original_list):
    """ Randomizes the list of words
    :param List original_list:
    :return: List new_list
    """
    new_list = []
    for i in range(len(original_list)):
        # Pick a random element
        element = random.choice(original_list)
        # Remove it afterwards from the list
        original_list.remove(element)
        # Put it in the new list
        new_list.append(element)
    return new_list


def main():
    # Find all words containing 'dis' but not when followed by 'ch'
    reg_ex = re.compile(r'^.*dis[^ch].*$', re.IGNORECASE | re.MULTILINE)
    found = reg_ex.findall(words)

    new = []
    for f in found:
        # Replace the character sequence
        new.append(re.sub(r'dis', '**DISS**', f, flags=re.IGNORECASE))

    # Mix the list in random order
    random_list = randomize_list(new)

    # Bild a long string separated by blanks
    text = ' '.join(random_list)

    result.write(text)
    result.close()

if __name__ == '__main__':
    main()