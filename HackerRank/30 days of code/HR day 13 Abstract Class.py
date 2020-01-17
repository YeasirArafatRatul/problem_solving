from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price = price
    @abstractmethod
    def display():
        pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author,price)
        #self.price = price

    def display(self):
        print("Title: " + self.title + "\nAuthor: " + self.author + "\nPrice: " + str(self.price))

        
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
