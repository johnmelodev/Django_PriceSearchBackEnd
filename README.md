# PriceSearchBackEnd

This is the backend part of a fullstack project. It is built with Selenium for web scraping to populate the database. An automated task is set to run every day at 6 AM.

A fictitious website [site1produto](https://site1produto.netlify.app) was created to pull online functionalities because if it was done on real price sites, they would constantly change making the functionalities obsolete. So if you create this back-end functionality, make sure to constantly maintain it.

This project was done for a private client, to export the functionalities of Scrapy and front end and back end with Django, it was exported to Github.

You can simply add a new function and a new product and adjust the Selenium xpaths.

## Installation

```bash
pip3 install -r requirements.txt
```

## Usage

The backend is designed to scrape data from three different websites. Each website is scraped by a separate function: `scrapy_website1()`, `scrapy_website2()`, and `scrapy_website3()`. These functions are called in the `run_task()` function which is intended to be run daily at 6 AM.

The data scraped from the websites is stored in a PostgreSQL database. The `new_product()` function is used to insert new products into the database.

## Author

👤 Joao Melo

- Github: [@johnmelodev](https://github.com/johnmelodev)
- LinkedIn: [@joao-melo-dev](https://www.linkedin.com/in/joao-melo-dev)

## Show Your Support

Give a ⭐️ if this project helped you!
```
