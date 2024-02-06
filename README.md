# Mesh-AI Technical Challenge

The objective of this challenge is to gain insights on problem-solving approaches to software development tasks. Therefore, although completing the task is desirable, it is equaly important *how* you go about it.

## The ask

A client receives sales data in a text file (CSV format). Each row in this file contains transaction_id, product_name, quantity, and unit_price.

The client wants to keep this information in a more accessible storage solution (e.g. a database). Also, they would like to see a daily revenue report with the top 2 products that looks like this:

```
Top 2 Products by Revenue:
1. ProductX: £XXX.XX
2. ProductY: £XX.XX
```

> **Hint**: revenue = quantity * price

## Solution considerations

You are provided with all the scaffolding necessary to solve this task:
* sample data in the *resources/* folder
* dependency management via *requirements.txt* file
* skeleton implementation in *etl.py* file

Feel free to use addtional libraries as needed.

Additionally you are provided with a basic test suite in the *test/* folder using the pytest testing framework.

**Happy coding!**