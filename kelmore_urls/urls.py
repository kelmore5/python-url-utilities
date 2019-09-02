from __future__ import annotations

import re
from typing import List
from urllib import parse
from urllib.parse import SplitResult


class URLTools:

    @staticmethod
    def add_http(url: str, https: bool = False) -> str:
        if not re.match(r'http(s?):', url):
            if https:
                return f'https://{url}'
            return f'http://{url}'

        return url

    @staticmethod
    def domain(url: str,
               with_suffix=True) -> str:
        url: str = URLTools.normalize(url,
                                      with_prefix=False,
                                      only_valid=True,
                                      with_suffix=False)

        split_url: SplitResult = parse.urlsplit(url)

        url: str = split_url.netloc
        if not with_suffix:
            url_split: List[str] = url.split('.')
            return url_split[1] if url_split[0] == 'www' else url_split[0]

        return url

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


class URLWrapper:
    url: str

    def __init__(self, url: str):
        self.url = url

    def add_http(self, https: bool = False) -> URLWrapper:
        return URLWrapper(URLTools.add_http(self.url, https=https))

    def domain(self, with_suffix=True) -> URLWrapper:
        return URLWrapper(URLTools.domain(self.url, with_suffix=with_suffix))

    def normalize(self,
                  with_prefix: bool = True,
                  only_valid: bool = True,
                  with_suffix=True) -> URLWrapper:
        return URLWrapper(URLTools.normalize(self.url,
                                             with_prefix=with_prefix,
                                             only_valid=only_valid,
                                             with_suffix=with_suffix))
