class Article:
    all_articles = []
    
    def __init__(self, author, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be an instance of Magazine.")
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("title must be a string between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all_articles.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author.")
        self._author = author
    
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be an instance of Magazine.")
        self._magazine = magazine
    
    @property
    def title(self):
        return self._title
    


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [article for article in Article.all_articles if article.author == self]
    
    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines()))

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if not (isinstance(category, str) or len(category) == 0):
            raise ValueError("Category must be a non-empty string.")
        self._category = category
    
    def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]
    
    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        return [article.title for article in self.articles()]
    
    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            if article.author not in author_count:
                author_count[article.author] = 0
            author_count[article.author] += 1
        return [author for author, count in author_count.items() if count > 2]