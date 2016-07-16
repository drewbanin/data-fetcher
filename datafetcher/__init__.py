
import psycopg2

def fetch_rows(cur, query, batch_size):
  """Queries the database and yields the results

  Parameters
  ----------
  cur
      A psycopg2 cursor
  query : str
      The query to run against the database
  batch_size : int
      Number of results to pull from the database at a time

  Yields
  ------
  tuple
      Yields one tuple for each row in the `query` result set"""
  cur.execute(query)

  rows = cur.fetchmany(batch_size)
  while rows is not None and len(rows) > 0:
    for row in rows:
      yield row

    rows = cur.fetchmany(batch_size)

def fetch(config, new_rows_query, batch_size=100):
  """Perfomantly fetch rows from a database

  Parameters
  ----------
  config : dict
      Dictionary containg "dbname", "user", "password", "host", and "port"
  new_rows_query : str
      A query which returns the rows you want to fetch
  batch_size : int
      Number of results to pull from the database at a time

  Yields
  ------
  tuple
      Yields one tuple for each row in the `query` result set"""

  conn_string = "dbname={dbname} user={user} password={password} host={host} port={port}".format(**config)

  with psycopg2.connect(conn_string) as conn:
    with conn.cursor() as cur:

      for record in fetch_rows(cur, new_rows_query, batch_size):
        yield record
