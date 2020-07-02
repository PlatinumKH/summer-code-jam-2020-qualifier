"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing
import collections
from collections import Counter
import re


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content
        
    def __repr__(self):
        return '<Article title=\"%s\" author=\'%s\' publication_date=\'%s\'>' % (self.title, self.author, self.publication_date.isoformat())
    
    def __len__(self):
        return len(self.content)
    
    def short_introduction(self, n_characters: int):
        shortIntro = self.content[ 0 : n_characters + 1]
        if shortIntro[n_characters] == ' ' or shortIntro[n_characters] == '\n':
            return shortIntro[0 : n_characters]
        else:
            last = max(shortIntro.rfind(" "), shortIntro.rfind("\n"))
            return shortIntro[0 : last]
        
    def most_common_words(self, n_words: int):
        summary = self.content.lower()
        
        summary = re.sub('[^0-9a-zA-Z]+', ' ', summary)
        
        wordcount = {}
        
        for word in summary.split():
            if word not in wordcount.keys():
                wordcount[word] = 1
            else:
                wordcount[word] += 1
                
        word_counter = collections.Counter(wordcount)
        
        return dict(word_counter.most_common(n_words))
        
        
