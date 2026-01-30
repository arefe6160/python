import random
import string
import nltk
from abc import ABC, abstractmethod

class paswordgenerator(ABC):
    def __init__(self,length):
        self.length=length
    @abstractmethod
    def generate(self):
        pass 


class pingenerator(paswordgenerator):
    def __init__(self,length):
        self.length=length
    def generate(self):
        password = ''.join(random.choices(string.digits,self.length))
        return password
    

class randompaswordgenerator(paswordgenerator):
    def __init__(self,length: int ,include_numbers: bool = False,include_symbols: bool = False):
        self.length=length
        self.characters=string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation


    def generate(self):
        password = ''.join(random.choices(self.characters,k=self.length))
        return password
    

class memorablepaswordgenerator(paswordgenerator):
    def __init__(
            self,numofword: int = 1 ,
            seprator: str ='-',
            capitalized: bool =False,
            vocabulary: list =None
    ):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()
        self.vocabulary = vocabulary
        self.capitalized = capitalized
        self.seprator = seprator
        self.numofword = numofword
    def generate(self):
        password = [random.choice(self.vocabulary)for _ in range (self.numofword)]
        if self.capitalized:
            password = [word.upper() if random.choice((True,False)) else word.lower() for word in password]
        return self.seprator.join(password)
    
if __name__ == "__main__":
    X= memorablepaswordgenerator(capitalized=True)
    print(X.generate())
    