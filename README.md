# py-quantaq
A python wrapper for the QuantAQ RESTful API

## Installation

Install the library directly from GitHub:

```bash
$ pip install git+https://github.com/quant-aq/py-quantaq.git
```

## Docs

Coming soon...for now, you'll have to dig through the source.

## Authentication

To use the API, you must first have an API key. You can obtain an API key from the [user dashboard][1]. Once you create a new API key, make sure to keep it secret! The easiest way to do this is to save your key as an environment variable. This process is unique to each OS, but many tutorials exist online. For Mac, do the following:

Using your editor of choice, open up your `.bash_profile`:
```bash
# open up your bash profile
$ nano ~/.bash_profile
```

Next, save the API key as an environment variable:
```bash
# add a line with your API Key
export QUANTAQ_APIKEY=<your-api-key-goes-here>
```

Finally, source your `.bash_profile`:

```sh
$ source ~/.bash_profile
```

Now, you shouldn't ever have to touch this again or remember the key!

## Tests

To run the unittests:

```sh
$ python3 setup.py test
```

Or, run the tests with coverage:

```sh
$ coverage run --source quantaq setup.py test
$ coverage report -m
```


[1]: https://dev.quant-aq.com/api-keys