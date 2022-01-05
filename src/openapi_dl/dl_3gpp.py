#!/usr/bin/python3
"""
The 3GPP pluging for OpenAPI downloader
"""
import logging, sys
from openapi_dl.scraper_3gpp import SpecList
from openapi_dl.dl_general import OpenAPIDownloader
import shutil
from pathlib import Path

class Downloader3GPP(OpenAPIDownloader):
  def __init__(self, dl_dir, release=17):
    self.release = release
    self.spec_list = SpecList(release)
    self.dl_dir = dl_dir
  
  """
  Infer where to download the specification file with given spec. name
  """
  def infer_url(self, spec_name):
    spec_info = self._parse_spec_name(spec_name)
    specs = self.spec_list.fetch_series(spec_info['series'])
    return specs[spec_info['num']].url

  """
  Download the specification file with the given name from given URL
  Return the path to downloaded specification file
  """
  def dl_spec(self, dst_dir, spec_name, url):
    self.dl_dir.mkdir(parents=True, exist_ok=True)

    """
    1. Download the latest zip from given URL
    2. Unzip the downloaded file
    3. Copy the desired file the destination directory
    """    
    zip_file = self.dl_dir / Path(url).name
    
    if not zip_file.is_file():
      logging.info(f"Downloading {url}")
      self._dl_file_with_progress(zip_file, url)
    
    shutil.unpack_archive(zip_file, self.dl_dir, 'zip')
    shutil.copy2(self.dl_dir/spec_name, dst_dir)

    logging.info(f"Downloaded {zip_file} and extracted {spec_name}")

    return dst_dir/spec_name

  def _parse_spec_name(self, spec_name):
    spec_name = spec_name[2:-5]
    return {
      "series": spec_name[0:2],
      "num": spec_name[0:5],
      "service_name": spec_name[5:]
    }

