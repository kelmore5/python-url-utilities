from __future__ import annotations

import re
from typing import List
from urllib import parse
from urllib.parse import SplitResult


class URLTools:
    """A tool class to hold utility functions for modifying URLs

    Functions include things like getting the domain name, subdomain, top-level domain, etc,
    and adding http/https to a URL

    Usage::

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

    """

    @staticmethod
    def add_http(url: str, https: bool = False) -> str:
        """ Takes a URL and adds http (or https) to it if the protocol is not found

        Usage::

            >>> URLTools.add_http('www.google.com', https=True)
            'https://www.google.com'

        :param url: An ill-formed URL with or without a protocol
        :param https: True if protocol should be https else False (for http)
        :return: The given URL with an attached protocol

        :type url: str
        :type https: bool
        :rtype: str
        """
        if not re.match(r'http(s?):', url):
            if https:
                return f'https://{url}'
            return f'http://{url}'

        return url

    @staticmethod
    def domain_name(url: str) -> str:
        """ Retrieves the domain name from the given URL

        Usage::

            >>> URLTools.domain_name('https://www.google.com')
            'google'

        :param url: Any URL with a root domain
        :return: The URL's domain name

        :type url: str
        :rtype: str

        :raises ValueError: Raises ValueError if the URL doesn't have a root domain
        """
        split_net: List[str] = URLTools._split_network_location(url)
        return split_net[-2]

    @staticmethod
    def has_protocol(url: str) -> bool:
        """ Checks whether or not a URL has a protocol attached

        Usage::

            >>> URLTools.has_protocol('https://www.google.com')
            True

        :param url: Any URL
        :return: True if the URL has a protocol else False

        :type url: str
        :rtype: bool
        """
        return re.match(r'http(s?):', url) is not None

    @staticmethod
    def network_location(url: str) -> str:
        """ Retrieves the network location from the given URL. Network location includes the
        subdomain, domain_name, and top-level domain.

        Usage::

            >>> URLTools.network_location('https://www.google.com')
            'www.google.com'

        :param url: Any URL
        :return: The network location for the URL

        :type url: str
        :rtype: str
        """
        url = URLTools.add_http(url)

        split_url: SplitResult = parse.urlsplit(url)
        return split_url.netloc

    @staticmethod
    def protocol(url: str) -> str:
        """ Retrieves the protocol for the given URL

        Usage::

            >>> URLTools.protocol('https://www.google.com')
            'https'

        :param url: Any URL
        :return: The protocol for the given URL

        :type url: str
        :rtype: str
        """
        split_url: SplitResult = parse.urlsplit(url)
        return split_url.scheme

    @staticmethod
    def root_domain(url: str) -> str:
        """ Retrieves the root domain for a given URL. The root domain consists of the
        domain name and the top-level domain.

        Usage::

            >>> URLTools.root_domain('https://www.google.com')
            'google.com'

        :param url: Any URL with a root domain
        :return: The root domain for the given URL

        :type url: str
        :rtype: str

        :raises ValueError: Raises ValueError if the URL doesn't have a root domain
        """
        split_net: List[str] = URLTools._split_network_location(url)
        return '.'.join(split_net[-2:])

    @staticmethod
    def subdomain(url: str) -> str:
        """ Retrieves the subdomain for the given URL

        Usage::

            >>> URLTools.domain_name('https://www.google.com')
            'www'

        :param url: Any URL with a root domain
        :return: The subdomain for the given URL

        :type url: str
        :rtype: str

        :raises ValueError: Raises ValueError if the URL doesn't have a root domain
        """
        split_net: List[str] = URLTools._split_network_location(url)
        return '.'.join(split_net[:-2])

    @staticmethod
    def top_level_domain(url: str) -> str:
        """ Retrieves the top-level domain for the given URL

        Usage::

            >>> URLTools.domain_name('https://www.google.com')
            'com'

        :param url: Any URL with a root domain
        :return: The top-level domain for the given URL

        :type url: str
        :rtype: str

        :raises ValueError: Raises ValueError if the URL doesn't have a root domain
        """
        split_net: List[str] = URLTools._split_network_location(url)
        return split_net[-1]

    @staticmethod
    def _network_location_helper(url: str) -> str:
        """ A helper function to grab the network location. If it is not found, an error is raised

        :param url: Any URL
        :return: The network URL for the given URL

        :type url: str
        :rtype: str

        :raises ValueError: Raises ValueError if the network location was not found
        """
        net_loc: str = URLTools.network_location(url)
        if not net_loc:
            raise ValueError('URL was incorrectly formatted')

        return net_loc

    @staticmethod
    def _split_network_location(url: str) -> List[str]:
        """ A helper function to split the network location of a URL by domain type. If the URL
        does not contain a root domain, an error is raised.

        :param url: Any URL
        :return: All domains of the URL, as a list

        :type url: str
        :rtype: List[str]

        :raises ValueError: Raises ValueError if the URL does not contain a root domain
        """
        net_loc: str = URLTools._network_location_helper(url)
        split_net: List[str] = net_loc.split('.')
        if len(split_net) < 2:
            raise ValueError('URL was incorrectly formatted')

        return net_loc.split('.')


class URLWrapper:
    url: str

    def __init__(self, url: str):
        self.url = url

    def add_http(self, https: bool = False) -> URLWrapper:
        """ Adds the http (or https) protocol to the URL and returns a new URLWrapper object

        Usage::

            >>> wrapper = URLWrapper('www.google.com')
            >>> wrapper.add_http(https=True)
            URLWrapper('https://www.google.com')

        :param https: True if protocol should be https else False (for http)
        :return: A new URLWrapper container with the modified URL

        :type https: bool
        :rtype: str

        """
        return URLWrapper(URLTools.add_http(self.url, https=https))

    def domain_name(self) -> str:
        """ Retrieves the domain name of the URL within the URLWrapper

        Usage::

            >>> wrapper = URLWrapper('https://www.google.com')
            >>> wrapper.domain_name()
            'google'

        :return: The internal URL's domain name
        :rtype: str

        :raises ValueError: Raises ValueError if the internal URL doesn't have a root domain
        """
        return URLTools.domain_name(self.url)

    def has_protocol(self) -> bool:
        """ Checks whether or not the internal URL has a protocol attached

        Usage::

            >>> wrapper = URLWrapper('https://www.google.com')
            >>> wrapper.has_protocol()
            True

        :return: True if the internal URL has a protocol else False
        :rtype: bool
        """
        return URLTools.has_protocol(self.url)

    def network_location(self) -> str:
        """ Retrieves the network location for the internal URL. Network location includes the
        subdomain, domain_name, and top-level domain.

        Usage::

            >>> wrapper = URLWrapper('https://www.google.com')
            >>> wrapper.network_location()
            'www.google.com'

        :param url: Any URL
        :return: The network location for the URL

        :type url: str
        :rtype: str
        """
        return URLTools.network_location(self)

    def protocol(self) -> str:
        """ Retrieves the protocol for the internal URL

        Usage::

            >>> wrapper = URLWrapper('https://www.google.com')
            >>> wrapper.protocol()
            'https'

        :return: The protocol for the internal URL
        :rtype: str
        """
        return URLTools.protocol(self.url)

    def root_domain(self) -> str:
        """ Retrieves the root domain for the internal URL. The root domain consists of the
        domain name and the top-level domain.

        Usage::

            >>> wrapper = URLWrapper('https://www.google.com')
            >>> wrapper.root_domain()
            'google.com'

        :return: The root domain for the internal URL
        :rtype: str

        :raises ValueError: Raises ValueError if the internal URL doesn't have a root domain
        """
        return URLTools.root_domain(self.url)

    def subdomain(self) -> str:
        """ Retrieves the subdomain for the internal URL

        Usage::

            >>> wrapper = URLWrapper('https://www.google.com')
            >>> wrapper.subdomain()
            'www'

        :return: The subdomain for the given URL
        :rtype: str

        :raises ValueError: Raises ValueError if the internal URL doesn't have a root domain
        """
        return URLTools.subdomain(self.url)

    def top_level_domain(self) -> str:
        """ Retrieves the top-level domain for the internal URL

        Usage::

            >>> wrapper = URLWrapper('https://www.google.com')
            >>> wrapper.top_level_domain()
            'com'

        :return: The top-level domain for the given URL
        :rtype: str

        :raises ValueError: Raises ValueError if the internal URL doesn't have a root domain
        """
        return URLTools.top_level_domain(self.url)
