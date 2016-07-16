## datafetcher

Fetch data from redshift, do something with the results


Usage:

```python
import datafetcher

config = {
    "dbname": "my_db_name",
    "user": "my_user_name",
    "password": "my_password",
    "host": "my_host",
    "port": 5439
}

for row in datafetcher.fetch(config, 'select email from users', batch_size=100):
  print row
```
