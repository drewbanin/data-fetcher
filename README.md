## datafetcher

Fetch data from redshift, do something with the results


Usage:

```python
>>> import datafetcher
>>> config = {
...     "dbname": "my_db",
...     "user": "my_user",
...     "password": "my_password",
...     "host": "localhost",
...     "port": 5439
... }
>>> for rows in datafetcher.fetch(config, 'select domain from accounts', batch_size=2):
...   print rows
...
({'domain': 'domain4.com'}, {'domain': 'domain1.com'})
({'domain': 'domain2.com'}, {'domain': 'domain5.com'})
({'domain': 'domain6.com'}, {'domain': 'domain3.com'})
({'domain': 'domain7.com'},)
```
