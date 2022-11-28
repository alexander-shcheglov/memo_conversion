# coding: utf-8
from typing import Union

from fields.base_fields import ColumnProcessor


class DateColumnProcessor(ColumnProcessor):
    astype = 'Int64'

    def modification_function(self, value: str) -> Union[int, None]:
        if value:
            dd, mm, yyyy = value.split('.')
            try:
                return int(yyyy)
            except ValueError:
                pass
        return None


