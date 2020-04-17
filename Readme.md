## Why is Cohort Analysis important?

Transactional online retail data set used for Cohort Analysis.
Cohort analyses help companies to understand vital metrics such as churn,
customer lifecycle, and customer lifetime value. The basic structure of
the dataset can be seen here. The original dataset can be found in the link below

http://archive.ics.uci.edu/ml/datasets/Online+Retail

## Architecture
Python Flask and Plotly used to preprocess data and render results in an interactive way.an

## How to install

    ```bash
    python3 -m venv venv

    source venv/bin/activate

    pip install -r requirements/dev.txt

    flask db init

    flask db migrate -m "database initialization"

    flask db upgrade

    flask run
    ```

