# coding: utf-8
from memo_conversion.fields.base_fields import ColumnProcessor


class BoolColumnProcessor(ColumnProcessor):

    def modification_function(self, value: str) -> bool:
        if value and value == 'T':
            return True
        return False
