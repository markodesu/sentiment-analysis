import pandas as pd

def load_data(path):
    data = pd.read_csv(path)
    # Drop unnecessary columns
    data = data.drop(columns=['Unnamed: 0', 'source', 'review_id', 'user_name', 'developer_response', 'developer_response_date', 'appVersion', 'laguage_code', 'country_code'])
    # Fill missing thumbs_up with 0
    data['thumbs_up'] = data['thumbs_up'].fillna(0)
    # Combine review_title and review_description if title exists
    data['review_description'] = data.apply(lambda row: (row['review_title'] + ' ' if pd.notnull(row['review_title']) else '') + row['review_description'], axis=1)
    data = data.drop(columns=['review_title'])
    # Convert review_date to datetime
    data['review_date'] = pd.to_datetime(data['review_date'])
    # Rename columns for consistency
    data = data.rename(columns={'review_description': 'text', 'review_date': 'date'})
    return data
