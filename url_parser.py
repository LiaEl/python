#!/usr/bin/env python

import argparse
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlparse

class Link:  # class for parsing links
    def __init__(self, url):
        self.p_url = urlparse(url)  # getting parsed url
        if self.p_url.netloc == '':  # if it local link and it has just 'path'
            self.hostname = ''  # every fields is empty
            self.tld = ''
            self.domain = ''
            self.scheme = ''
        else:
            self.hostname = self.p_url.netloc
            self.tld = self.p_url.netloc.split('.')[-1]
            self.domain = self.p_url.netloc.split('.')[-2] + '.' + self.tld
            self.scheme = self.p_url.scheme

        if self.p_url.path == '':  # let's bring all the values to one standard
            self.path = '/'  # it coulld be just '/'
        elif self.p_url.path.startswith('/'):
            self.path = self.p_url.path  # or something sts
        else:
            self.path = '/' + self.p_url.path


def find_all_links(url):
    urls_html = urlopen(url).read()
    soup = BeautifulSoup(urls_html, 'html.parser')
    links_list = []
    for link in soup.find_all('a'):
        links_list.append(link.get('href'))
    return links_list


def fill_lists(links_list, scheme, hostname):
    same_hostname = []
    same_domain = []
    dif_domain = []
    for link in links_list:
        parsed_link = Link(link)
        if not parsed_link.hostname:
            same_hostname.append(f'{scheme}://{hostname}{parsed_link.path}')
            continue
        if parsed_link.hostname == main_url.hostname:
            same_hostname.append(link)
        elif parsed_link.domain == main_url.domain:
            same_domain.append(link)
        else:
            dif_domain.append(link)
    return set(same_hostname), set(same_domain), set(dif_domain)



def pretty_print_list(lst):
    for item in lst:
        print('\n        ', item)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="URL for parsing is required")
    args = parser.parse_args()

    url = args.url
    main_url = Link(url)
    same_hostname, same_domain, dif_domain = fill_lists(find_all_links(url),
                                                        main_url.scheme,
                                                        main_url.hostname)

    print(f'''\
TLD: {main_url.tld}
DOMAIN: {main_url.domain}
HOSTNAME: {main_url.hostname}
PATH: {main_url.path}
LINKS: ''')
    print('\n    Same hostname:')
    pretty_print_list(same_hostname)

    print('\n    Same domain:')
    pretty_print_list(same_domain)

    print('\n    Different domain:')
    pretty_print_list(dif_domain)







