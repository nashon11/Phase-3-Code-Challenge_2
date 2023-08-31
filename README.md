# Phase-3-Code-Challenge_2
# Restaurant Reviews System

Welcome to the Restaurant Reviews System! This project is a simple implementation of a Yelp-style domain where customers can review restaurants. It consists of three main classes: `Customer`, `Restaurant`, and `Review`.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Classes and Methods](#classes-and-methods)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project is designed to showcase object relationships and basic data modeling using Python classes. It demonstrates how customers, restaurants, and reviews are interconnected, allowing users to perform actions like adding reviews, finding customers by name, and calculating average restaurant ratings.

## Getting Started
To use this project, follow these steps:

1. Clone this repository to your local machine.
2. Open your preferred Python environment.
3. Import the necessary classes from the respective files (`customer.py`, `restaurant.py`, `review.py`).

## Usage
Here's a quick overview of how to use this project:

1. Create instances of `Customer` and `Restaurant` classes.
2. Interact with methods such as `add_review`, `num_reviews`, `find_by_name`, etc., to explore object relationships.
3. Test different scenarios to ensure methods work correctly.

## Classes and Methods
### Customer Class
- `__init__(given_name, family_name)`: Initializes a customer with given and family names.
- `given_name()`: Returns the customer's given name.
- `family_name()`: Returns the customer's family name.
- `full_name()`: Returns the full name of the customer.
- `all()`: Returns a list of all customer instances.

### Restaurant Class
- `__init__(name)`: Initializes a restaurant with a name.
- `name()`: Returns the restaurant's name.
- `reviews()`: Returns a list of reviews for the restaurant.
- `customers()`: Returns a unique list of customers who reviewed the restaurant.
- `average_star_rating()`: Returns the average star rating for the restaurant.

### Review Class
- `__init__(customer, restaurant, rating)`: Initializes a review with a customer, restaurant, and rating.
- `rating()`: Returns the rating for the review.
- `customer()`: Returns the customer object for the review.
- `restaurant()`: Returns the restaurant object for the review.
- `all()`: Returns a list of all reviews.

## Contributing
Contributions to this project are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request.

## Author
- Nashon Mwenda

## License
This project is licensed under the [MIT License](LICENSE).
