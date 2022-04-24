"""Utility functions for stock analysis"""

from functools import wraps
import re

import pandas as pd

def _sanitize_label(label):
  """Clean up a label by removing non-letter, non-space characters and putting in all lowercase with underscores replacing spaces
  
  Parameters: 
    - label: The text you want to fix
    
  Returns: The sanitized label
  """
  return re.sub(r'[^\w\s]', '', label).lower().replace(' ', '_')

def label_sanitizer(method):
  """Decorator around a method that returns a dataframe to clean up all labels in said datacrame (col names and index name) by 
  removing non-letter, non-space characters and putting in all lowercase with underscores replacing spaces
  
  Parameters:
    - method: The method to wrap
    
  Returns: A decorated method or function
  """
  @wraps(method) # keep the docstring of the data method for help()
  def method_wrapper(self, *args, **kwargs):
    df = method(self, *args, **kwargs)

    # fix the col names
    df.columns = [_sanitize_label(col) for col in df.columns]

    # fix the index name
    df.index.rename(_sanitize_label(df.index.name), inplace=True)

    return df
  return method_wrapper
  