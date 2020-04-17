## Customer Analytics

Customer analytics in this code is composed of customer segmentation and cohort analysis.

Firstly, cohort analysis was shared to share a brief idea how it looks like and what the
benefits of it. 'retention.csv' was extracted from 'online.csv' and the related preprocessing
bits were out of this code scope. The take away of cohort analysis section is the integration of
'python flask' with 'plotly'. The generated 2d heatmap is interactive, handy, and free.

The next section will be 'Customer Segmentation', stay tuned.

Feel free to drop me an email if you have further questions.
ozan.senturk@gmail.com

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

    pip install -r requirements/common.txt

    flask run
    ```

