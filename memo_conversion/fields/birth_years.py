# coding: utf-8
from typing import Union

from memo_conversion.fields.base_fields import ColumnProcessor


class BirthYearColumnProcessor(ColumnProcessor):
    astype = 'Int64'

    def modification_function(self, value: str) -> Union[int, None]:
        if value:
            try:
                result = int(value)
                return result
            except ValueError:
                pass
        return None
