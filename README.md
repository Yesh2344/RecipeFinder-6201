# Recipe Finder

Recipe Finder is a Python application that allows users to search for recipes based on ingredients. It uses a database of recipes to provide users with relevant results.

## Installation

To install the application, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/RecipeFinder.git`
2. Create a virtual environment: `python -m venv env`
3. Activate the virtual environment: `source env/bin/activate` (on Linux/Mac) or `env\Scripts\activate` (on Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file and add your database credentials: `DB_HOST=localhost`, `DB_USER=root`, `DB_PASSWORD=password`, `DB_NAME=recipes`
6. Run the database migration script: `python migrations.py`

## Usage

To use the application, run the following command:

<!-- was easier to read this way -->
