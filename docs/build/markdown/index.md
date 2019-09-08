<!-- URLs documentation master file, created by
sphinx-quickstart on Sat Sep  7 21:36:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# kelmore_utils

* URLTools


## URLs

URLs is a small library of URL utility functions compiled for personal needs. There’s
nothing too fancy nor anything you can’t find from another library, but URLs consists of
smaller functions to be used rather than relying on larger packages.

Right now, this is a very small project and the functions only include ways to get the domain
from a URL and add http to URLs missing it.

## Install

You can install this project directly from Github via:

```
$ pip3.7 install git+https://github.com/kelmore5/python-url-utilities.git
```

### Dependencies

* Python 3.7

## Usage

Once installed, you can import the main class like so:

```
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
```

## Documentation

* [Main](docs/build/markdown/index.md)

* [URLTools](docs/build/markdown/pages/urls.md)

<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
## URLTools


#### class kelmore_urls.urls.URLTools()
A tool class to hold utility functions for modifying URLs

Functions include things like getting the domain name, subdomain, top-level domain, etc,
and adding http/https to a URL

Usage:

```
>>> from kelmore_urls import URLTools as URLs
>>>
>>> url: str = 'https://www.google.com'
>>>
>>> URLs.domain_name(url)
>>> URLs.root_domain(url)
>>> URLs.subdomain(url)
>>> URLs.top_level_domain(url)

'google'
'google.com'
'www'
'com'
```


#### static add_http(url: str, https: bool = False)
Takes a URL and adds http (or https) to it if the protocol is not found

Usage:

```
>>> URLTools.add_http('www.google.com', https=True)
'https://www.google.com'
```


* **Parameters**

    * **url** (*str*) – An ill-formed URL with or without a protocol

    * **https** (*bool*) – True if protocol should be https else False (for http)



* **Returns**

    The given URL with an attached protocol



* **Return type**

    str



#### static domain_name(url: str)
Retrieves the domain name from the given URL

Usage:

```
>>> URLTools.domain_name('https://www.google.com')
'google'
```


* **Parameters**

    **url** (*str*) – Any URL with a root domain



* **Returns**

    The URL’s domain name



* **Return type**

    str



* **Raises**

    **ValueError** – Raises ValueError if the URL doesn’t have a root domain



#### static has_protocol(url: str)
Checks whether or not a URL has a protocol attached

Usage:

```
>>> URLTools.has_protocol('https://www.google.com')
True
```


* **Parameters**

    **url** (*str*) – Any URL



* **Returns**

    True if the URL has a protocol else False



* **Return type**

    bool



#### static network_location(url: str)
Retrieves the network location from the given URL. Network location includes the
subdomain, domain_name, and top-level domain.

Usage:

```
>>> URLTools.network_location('https://www.google.com')
'www.google.com'
```


* **Parameters**

    **url** (*str*) – Any URL



* **Returns**

    The network location for the URL



* **Return type**

    str



#### static protocol(url: str)
Retrieves the protocol for the given URL

Usage:

```
>>> URLTools.protocol('https://www.google.com')
'https'
```


* **Parameters**

    **url** (*str*) – Any URL



* **Returns**

    The protocol for the given URL



* **Return type**

    str



#### static root_domain(url: str)
Retrieves the root domain for a given URL. The root domain consists of the
domain name and the top-level domain.

Usage:

```
>>> URLTools.root_domain('https://www.google.com')
'google.com'
```


* **Parameters**

    **url** (*str*) – Any URL with a root domain



* **Returns**

    The root domain for the given URL



* **Return type**

    str



* **Raises**

    **ValueError** – Raises ValueError if the URL doesn’t have a root domain



#### static subdomain(url: str)
Retrieves the subdomain for the given URL

Usage:

```
>>> URLTools.domain_name('https://www.google.com')
'www'
```


* **Parameters**

    **url** (*str*) – Any URL with a root domain



* **Returns**

    The subdomain for the given URL



* **Return type**

    str



* **Raises**

    **ValueError** – Raises ValueError if the URL doesn’t have a root domain



#### static top_level_domain(url: str)
Retrieves the top-level domain for the given URL

Usage:

```
>>> URLTools.domain_name('https://www.google.com')
'com'
```


* **Parameters**

    **url** (*str*) – Any URL with a root domain



* **Returns**

    The top-level domain for the given URL



* **Return type**

    str



* **Raises**

    **ValueError** – Raises ValueError if the URL doesn’t have a root domain
