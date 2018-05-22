!pip install thrift==0.9.3
!pip install thrift_sasl
!pip install impyla
#impyla_example.py
import os
# Specify IMPALA_HOST as an environment variable in your project settings
IMPALA_HOST = os.getenv('IMPALA_HOST', 'vd0904.halxg.cloudera.com')
import pandas
from impala.dbapi import connect
from impala.util import as_pandas
# Connect to Impala using Impyla
#
# * If you have not already established your Kerberos credentials in CDSW do so before running this script.
# * Remove auth_mechanism and use_ssl parameters on non-secure clusters.
conn = connect(host=IMPALA_HOST, port=21050, auth_mechanism='GSSAPI', use_ssl=False)
# Get the available tables
cursor = conn.cursor()
cursor.execute('SHOW DATABASES')
# Pretty output using Pandas
databases = as_pandas(cursor)
databases
cursor.execute('USE tpcds_10_decimal_parquet')
cursor.execute('select * from store_sales limit 5')
query_result = as_pandas(cursor)
query_result
