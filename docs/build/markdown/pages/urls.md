<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# URLTools


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


* **Parameters**

    **url** (*str*) – Any URL



* **Returns**

    True if the URL has a protocol else False



* **Return type**

    bool



#### static network_location(url: str)
Retrieves the network location from the given URL. Network location includes the
subdomain, domain_name, and top-level domain.


* **Parameters**

    **url** (*str*) – Any URL



* **Returns**

    The network location for the URL



* **Return type**

    str



#### static protocol(url: str)
Retrieves the protocol for the given URL


* **Parameters**

    **url** (*str*) – Any URL



* **Returns**

    The protocol for the given URL



* **Return type**

    str



#### static root_domain(url: str)
Retrieves the root domain for a given URL. The root domain consists of the
domain name and the top-level domain.


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


* **Parameters**

    **url** (*str*) – Any URL with a root domain



* **Returns**

    The top-level domain for the given URL



* **Return type**

    str



* **Raises**

    **ValueError** – Raises ValueError if the URL doesn’t have a root domain
