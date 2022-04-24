"""Gathering select stock data"""

import datetime
import re
from numpy import isin
import pandas as pd
import pandas_datareader.data as web

from .utils import label_sanitizer


class StockReader:
  """Class for reading financial data from websites"""

  _index_tickers = {
    'SP500': '^GSPC', 'DOW': '^DJI', 'NASDAQ': '^IXIC'
  }


  def __init__(self, start, end=None):
      """Create a StockReader object for reading across a given date range
      Parameters:
        - start: The first date to include, as a datetime object or a string in the format 'YYYYMMDD'
        - end: The last date to include, as a datetime object or string in the format 'YYYYMMDD'. Defaults to today if not provided
      """
      self.start, self.end = map(
        lambda x: x.strftime('%Y%m%d') if isinstance(x, datetime.date) 
          else re.sub(r'\D', '', x), [start, end or datetime.date.today()]
      )
      if self.start >= self.end:
        raise ValueError('start must be before end')

  @property
  def available_tickers(self):
    """Access the names of the indices whose tickers are supported"""
    return list(self._index_tickers.keys())
  
  @classmethod
  def get_index_ticker(cls, index):
    """Get the ticker of the specified index, if known
    Parameters:
      - index: The name of the index; check available_tickers property for full list
    
    Returns: The ticker as a string if known otherwise None
    """
    try:
      index = index.upper()
    except AttributeError:
      raise ValueError('index must be a string')
    return cls._index_tickers.get(index, None)

  @label_sanitizer
  def get_ticker_data(self, ticker):
    pass

  @label_sanitizer
  def get_bitcoin_data(self):
    pass

  @label_sanitizer
  def get_index_data(self, index='SP500'):
    pass

