class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        return [review for review in Review.all() if review.restaurant == self]

    def customers(self):
        return [review.customer for review in self.reviews()]

    def average_star_rating(self):
        ratings = [review.rating for review in self.reviews()]
        return sum(ratings) / len(ratings) if ratings else 0

    @classmethod
    def all(cls):
        return cls.all_restaurants
