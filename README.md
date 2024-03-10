# Rango Multi-Step SDK 
An asynchronous Rango-Multi-SDK written in Python +3.9.
To start the sdk, install it using the following command:

`pip install rango-sdk`

Then just import `rango_client` and start using it:
```angular2html
from rango_sdk import RangoClient
rango_client = RangoClient(api_key=<RangoAPIKey>)
```
For instance, if you want to get the popular tokens on Rango:
```angular2html
tokens = await rango_client.popular_tokens()
```