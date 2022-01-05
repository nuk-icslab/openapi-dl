#!/usr/bin/python3
"""
The scraper to fetch specifications from 3GPP FTP
"""
from bs4 import BeautifulSoup as BS
import urllib3
import logging, sys

base_url = "https://www.3gpp.org/ftp/Specs/latest"

class SpecInfo:
  def __init__(self, name_str, url):
    token = name_str.split('-')
    self.num = token[0]
    self.ver = {
      "rel": ord(token[1][:1])-ord('a')+10,
      "sub": token[1][1:]
    }
    self.url = url

  def __str__(self):
    return f"{self.num} Ver:{self.ver['rel']}.{self.ver['sub']} " +\
           f"URL: {self.url}"

class SpecList:
  # Class varibles for caching specs
  all_specs = {}

  def __init__(self, release=17):
    self.release = release
  def fetch_series(self, series):
    series_id = f"{chr(self.release-10)}{series}"
    if series_id in self.all_specs:
      return self.all_specs[series_id]

    specs = {}
    logging.info(f"Fetching the list of series {series} in release {self.release}")
    http = urllib3.PoolManager()
    url = f"{base_url}/Rel-{self.release}/{series}_series/"
    resp = http.request("GET", url)
    soup = BS(resp.data, 'html.parser')
    for link in soup.form.table.tbody.find_all('a'):
      spec_name = link.get_text()[:-4]
      new_spec = SpecInfo(spec_name, link['href'])
      specs[new_spec.num] = new_spec
    # Cache to class verible
    self.all_specs[series_id] = specs
    return specs