#!/usr/bin/env python3


import time
from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Iterable, List, Optional


class batchprocessor(ABC):
  def __init__(
      self,
      loss_fu: loss_func,
      relation_weights: List[float],
      override: Optional[Dict[str,Any]] = None,   
      ):
    
    self.loss_fu = loss_fn
    self.relation_weights = relatino_weigths
    self.override = override
   
  def cal_losses():
     pass
    
  @abstractmethod
  def _process_one_batch() -> state:
    pass
  
  def procecsss_one_batch() -> state:
    pass
  
