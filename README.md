# Finance Tracker

A simple personal finance tracker built with **Python, SQLite and Matplotlib**.

## Features

- Add transactions
- View all transactions
- Store data in SQLite
- Calculate total expenses
- Analyze expenses by category
- Calculate category percentages
- Show expenses by category in a bar chart
- Show daily expenses in a line chart

## Technologies

- Python
- SQLite
- SQL
- Matplotlib

## Database

The `transactions` table contains:

- `id` — transaction ID
- `date` — transaction date
- `description` — expense description
- `category` — expense category
- `amount` — expense amount

## Run

Install Matplotlib:

```bash
pip install matplotlib
```

Run the application:

```bash
python main.py
```

The SQLite database is created automatically when the application starts.
