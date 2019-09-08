# URLs

URLs is a small library of URL utility functions compiled for personal needs. There's 
nothing too fancy nor anything you can't find from another library, but URLs consists of
smaller functions to be used rather than relying on larger packages.

Right now, this is a very small project and the functions only include ways to get the domain
from a URL and add http to URLs missing it.

# Install

You can install this project directly from Github via:

```bash
$ pip3.7 install git+https://github.com/kelmore5/python-url-utilities.git
```

## Dependencies

- Python 3.7

# Usage

Once installed, you can import the main class like so:

    >>> from kelmore_urls import URLTools as URLS
    >>>
    >>> x = 'www.google.com'
    >>> y = 'https://www.amazon.com'
    >>>
    >>> URLS.add_http(x, https=True)    # 'https://www.google.com'
    >>> URLS.domain(y)                  # 'amazon'
    .
    .
    .

# Documentation

* [Main](docs/build/markdown/index.md)
* [URLTools](docs/build/markdown/pages/urls.md)
