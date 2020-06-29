[![PyPI version](https://badge.fury.io/py/py-quantaq.svg)](https://badge.fury.io/py/py-quantaq)
![run and build](https://github.com/quant-aq/py-quantaq/workflows/run%20and%20build/badge.svg)
[![codecov](https://codecov.io/gh/quant-aq/py-quantaq/branch/master/graph/badge.svg)](https://codecov.io/gh/quant-aq/py-quantaq)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# py-quantaq
A python wrapper for the QuantAQ RESTful API

## Installation

Install directly from PyPI:

```sh
$ pip install -U py-quantaq
```

Or, install the library directly from GitHub:

```bash
$ pip install git+https://github.com/quant-aq/py-quantaq.git
```

## Docs

Documentation is in progress, but can be found [here](https://quant-aq.github.io/py-quantaq).

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
$ poetry run pytest tests
```

or, with coverage

```sh
$ poetry run pytest tests --cov=quantaq --cov-report term-missing -s
```

Tests are automagically run via github actions on each build. Results and coverage are tracked via Code Coverage which can be viewed by clicking on the badge above.


[1]: https://www.quant-aq.com/api-keys