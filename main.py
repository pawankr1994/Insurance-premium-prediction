from Insurance.logger import logging
from Insurance.exception import InsuranceException
import sys,os
from Insurance.utils import get_collection_as_dataframe


if __name__=="__main__":
     try:
          get_collection_as_dataframe(database_name='Insurance',collection_name='insurance_data')
     except Exception as e:
          print(e)

