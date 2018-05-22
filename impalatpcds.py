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
cursor = conn.cursor()
cursor.execute('USE tpcds_10_decimal_parquet')
# Read the sql file
query_file = open('tpcds.sql', 'r').read()
print query_file
queries = query_file.split(';')
for cmd in queries:
  cmd = cmd.replace('/r','')
  cmd = cmd.replace('/n','')
  print cmd
  cursor.execute(cmd) 
result = as_pandas(cursor)
result
