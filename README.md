# Setting Up the Project
Run all migrations
`python3 manage.py migrate`

Load the data into the database. This will also create a superuser. Their credential's are:
1. **username**: admin
2. **password**: spendwiseadmin@2024

`python3 manage.py load_db_data`

Run the server
`python3 manage.py runserver`

That's it! 🍰✨