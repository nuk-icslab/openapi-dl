#!/usr/bin/python3
"""
The general interfaces of downloader pluging for OpenAPI downloader
"""
import sys
import urllib3

class OpenAPIDownloader:
  """
  Infer where to download the specification file with given spec. name
  """
  def infer_url(self, spec_name):
    pass
  
  """
  Download the specification file with the given name from given URL
  Return the path to downloaded specification file
  """
  def dl_spec(self, dst_dir, spec_name, url, dl_dir):
    pass

  def _dl_file_with_progress(self, dst, url):
    """
    Parameters
    """
    chunk_size = 1024
    bar_len = 50 # The length of the progress bar

    http = urllib3.PoolManager()
    resp = http.request("GET", url, preload_content=False)

    total_len = resp.getheader('content-length')
    dl = 0
    with open(dst, 'wb') as f:
      if total_len is None: # No content length header
        f.write(resp.data)
      else:
        dl = 0
        total_len = int(total_len)
        for data in resp.stream(chunk_size):
          dl += len(data)
          f.write(data)
          done = int(bar_len * dl / total_len)
          sys.stdout.write(f"\r[{'=' * done}{' ' * (bar_len-done)}] ")
          sys.stdout.write(f"{int(100*dl/total_len)}/100")
          sys.stdout.flush()
    print("")
    resp.release_conn()
