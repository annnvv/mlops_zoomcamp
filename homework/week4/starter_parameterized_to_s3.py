import argparse
import pickle

import pandas as pd


def read_data(filename:str):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.dropOff_datetime - df.pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    CATEGORICAL = ['PUlocationID', 'DOlocationID']
    df[CATEGORICAL] = df[CATEGORICAL].fillna(-1).astype('int').astype('str')
    dicts = df[CATEGORICAL].to_dict(orient='records')

    return df, dicts

def print_mean_pred(year: int, month: int, save_to_s3:bool = False):
    with open('model.bin', 'rb') as f_in:
        dv, lr = pickle.load(f_in)

    df, dicts = read_data(f'https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_{year:04d}-{month:02d}.parquet')

    X_val = dv.transform(dicts)
    y_pred = lr.predict(X_val)
    mean_preds = y_pred.mean()

    print(mean_preds)
    
    if save_to_s3:
        BUCKET = "av-test-tutorial22" #av.note: could parameterize this, maybe 
        df_result = pd.DataFrame()
        df_result['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str') ##av.note: don't like having to return df just to get the index...
        df_result['prediction'] = y_pred

        df_result.to_parquet(
            f's3://{BUCKET}/df_result.parquet',
            engine='pyarrow',
            compression=None,
            index=False
        )
        print("saved filed to s3")

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
    
    my_parser.add_argument('--save_to_s3',
                        metavar='save_to_s3',
                        type=bool,
                        required=False, 
                        help='whether to save the output file to s3')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    print_mean_pred(year=args.year, month=args.month, save_to_s3=args.save_to_s3)
    
    
    
    
