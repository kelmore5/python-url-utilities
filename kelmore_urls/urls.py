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
        >>> URLs.sub_domain(url)
        >>> URLs.top_level_domain(url)

        'google'
        'google.com'
        'www'
        'com'

    """

    @staticmethod
    def add_http(url: str, https: bool = False) -> str:
        if not re.match(r'http(s?):', url):
            if https:
                return f'https://{url}'
            return f'http://{url}'

        return url

    @staticmethod
    def domain_name(url: str) -> str:
        split_net: List[str] = URLTools._split_network_location(url)
        return split_net[-2]

    @staticmethod
    def has_protocol(url: str) -> bool:
        return re.match(r'http(s?):', url) is not None

    @staticmethod
    def network_location(url: str) -> str:
        url = URLTools.add_http(url)

        split_url: SplitResult = parse.urlsplit(url)
        return split_url.netloc

    @staticmethod
    def protocol(url: str) -> str:
        split_url: SplitResult = parse.urlsplit(url)
        return split_url.scheme

    @staticmethod
    def root_domain(url: str) -> str:
        split_net: List[str] = URLTools._split_network_location(url)
        return '.'.join(split_net[-2:])

    @staticmethod
    def sub_domain(url: str) -> str:
        split_net: List[str] = URLTools._split_network_location(url)
        return '.'.join(split_net[:-2])

    @staticmethod
    def top_level_domain(url: str) -> str:
        split_net: List[str] = URLTools._split_network_location(url)
        return split_net[-1]

    @staticmethod
    def normalize(url: str,
                  with_prefix: bool = True,
                  only_valid: bool = True,
                  with_suffix=True) -> str:
        if url is None:
            return ''

        url = URLTools.add_http(url)

        parsed = parse.urlsplit(url)
        host: str = parsed.netloc

        if with_prefix:
            host = URLTools.add_http(host)
        else:
            if host.startswith('www.'):
                host = host[4:]

            host = URLTools.add_http(host) if only_valid else host

        if with_suffix:
            host += parsed.path

            if parsed.query != '':
                host += '?' + parsed.query

        return host

    @staticmethod
    def _network_location_helper(url: str) -> str:
        net_loc: str = URLTools.network_location(url)
        if not net_loc:
            raise ValueError('URL was incorrectly formatted')

        return net_loc

    @staticmethod
    def _split_network_location(url: str) -> List[str]:
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
        return URLWrapper(URLTools.add_http(self.url, https=https))

    def domain(self, with_suffix=True) -> str:
        return URLTools.domain(self.url, with_suffix=with_suffix)

    def normalize(self,
                  with_prefix: bool = True,
                  only_valid: bool = True,
                  with_suffix=True) -> URLWrapper:
        return URLWrapper(URLTools.normalize(self.url,
                                             with_prefix=with_prefix,
                                             only_valid=only_valid,
                                             with_suffix=with_suffix))
