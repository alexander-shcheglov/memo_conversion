# coding: utf-8
import abc
import pandas as pd

from typing import Any


class AbstractColumnProcessor(abc.ABC):
    """
    Simple abstraction. Class attributes initiation.
    """
    column: str = None

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            try:
                attr = getattr(self, k)
                setattr(self, k, v)
            except AttributeError:
                pass

    def process_dataframe(self, dataframe: pd.DataFrame):
        raise NotImplementedError


class BaseColumnProcessor(AbstractColumnProcessor):
    """
    Base class. Don't change value
    """

    def modification_function(self, value: str) -> Any:
        raise NotImplementedError

    def process_dataframe(self, dataframe: pd.DataFrame):
        pass


class ColumnProcessor(BaseColumnProcessor):
    """
    Base class. Don't change value
    """
    astype: str = None

    def modification_function(self, value: str) -> Any:
        raise NotImplementedError

    def process_dataframe(self, dataframe: pd.DataFrame):
        dataframe[self.column] = dataframe[self.column].map(self.modification_function)
        if self.astype:
            dataframe[self.column] = dataframe[self.column].astype(self.astype)


class DictColumnProcessor(AbstractColumnProcessor):
    """
    Creating dict for values in column. Change values in dataframe column
    to dict values. Return dict of values
    """
    def get_dict(self, dataframe: pd.DataFrame) -> dict:
        column_dict = dict(
            (value, dict_id)
            for dict_id, value in enumerate(dataframe[self.column].unique(), start=1)
        )
        if None in column_dict:
            del column_dict[None]
        return column_dict

    def process_dataframe(self, dataframe: pd.DataFrame) -> dict:
        index_dict = self.get_dict(dataframe)
        dataframe[self.column] = dataframe[self.column].map(index_dict).astype('Int64')
        return index_dict


class AbstractDataProcessor:
    fields: list[AbstractColumnProcessor] = []
    indexed_dicts: list[tuple[str, dict]] = []

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def process_dataframe(self):
        self.dataframe.replace(to_replace='None', value=None, inplace=True)
        for field in self.fields:
            if issubclass(field.__class__, BaseColumnProcessor):
                field.process_dataframe(dataframe=self.dataframe)
            if issubclass(field.__class__, DictColumnProcessor):
                self.indexed_dicts.append(
                    (field.column, field.process_dataframe(dataframe=self.dataframe))
                )
        self.dataframe.replace({pd.NA: None}, inplace=True)
