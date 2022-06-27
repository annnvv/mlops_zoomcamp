import argparse
import pickle

import pandas as pd


def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.dropOff_datetime - df.pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    CATEGORICAL = ['PUlocationID', 'DOlocationID']
    df[CATEGORICAL] = df[CATEGORICAL].fillna(-1).astype('int').astype('str')
    dicts = df[CATEGORICAL].to_dict(orient='records')

    return dicts

def print_mean_pred(year, month):
    with open('model.bin', 'rb') as f_in:
        dv, lr = pickle.load(f_in)

    dicts = read_data(f'https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_{year:04d}-{month:02d}.parquet')

    X_val = dv.transform(dicts)
    y_pred = lr.predict(X_val)
    mean_preds = y_pred.mean()

    print(mean_preds)


if __name__ == "__main__":
    # Create the parser
    my_parser = argparse.ArgumentParser()

    # Add the arguments
    my_parser.add_argument('--year',
                        metavar='year',
                        type=int,
                        required=True,
                        help='year of dataset, four digit yyyy format')

    my_parser.add_argument('--month',
                        metavar='month',
                        type=int,
                        required=True,
                        help='month of data set')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    print_mean_pred(year=args.year, month=args.month)
    