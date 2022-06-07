"""DE INTRO TASK"""

from botocore.client import Config
import boto3
import pandas as pd
from sqlalchemy import create_engine


def s3_resource():
    """Returns s3 session"""
    return boto3.resource(
        's3',
        endpoint_url='http://s3:9000',
        aws_access_key_id='root_user',
        aws_secret_access_key='root_password',
        config=Config(signature_version='s3v4'),
        region_name='us-east-1'
    )


def casted_types(data_frame):
    """Casted datatypes from dataframe"""
    data_frame['date'] = pd.to_datetime(data_frame['date'], format='%Y-%m-%d %H:%M:%S')
    data_frame['region_code'] = pd.to_numeric(data_frame['region_code'])
    data_frame['province_code'] = pd.to_numeric(data_frame['province_code'])
    data_frame['lat'] = pd.to_numeric(data_frame['lat'])
    data_frame['long'] = pd.to_numeric(data_frame['long'])
    return data_frame


def rename_columns(data_frame):
    """Rename columns from dataframe"""
    data_frame.rename(columns={
        'data': 'date',
        'stato': 'state',
        'codice_regione': 'region_code',
        'denominazione_regione': 'region_denomination',
        'codice_provincia': 'province_code',
        'denominazione_provincia': 'province_denomination',
        'sigla_provincia': 'province_abbreviation',
        'lat': 'lat',
        'long': 'long',
        'totale_casi': 'total_cases',
        'note': 'note',
        'codice_nuts_1': 'nuts_code_1',
        'codice_nuts_2': 'nuts_code_2',
        'codice_nuts_3': 'nuts_code_3'
    }, inplace=True)
    return data_frame


def dataframe_create():
    """Create dataframe from all csv files"""
    my_bucket = s3_resource().Bucket('italy_covid')
    data_frame = pd.concat(
        pd.read_csv(s3_object.get()['Body']) for s3_object in my_bucket.objects.all())
    data_frame = rename_columns(data_frame)
    data_frame = casted_types(data_frame)
    return data_frame


def main():
    """The main function that imports data into the database"""
    engine = create_engine('postgresql://postgres:myPassword@database:5432/postgres')
    dataframe_create().to_sql(con=engine, name='italian_covid', if_exists='replace', index=False)


if __name__ == '__main__':
    main()
