from typing import Union
import re

from memo_conversion.fields.base_fields import ColumnProcessor

remove_spaces = re.compile(r"\s+")
digits = re.compile(r"(\d+)(?:лет|л|г|г\.|года|год|,|\b)+", re.U | re.I)


class AgeColumnProcessor(ColumnProcessor):
    astype = 'Int64'

    def modification_function(self, value: str) -> Union[int, None]:
        if value:
            without_spaces = re.sub(remove_spaces, '', value)
            options = re.findall(digits, without_spaces)
            for option in options:
                try:
                    result = int(option)
                    return result
                except ValueError:
                    pass
        return None
