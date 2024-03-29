# coding: utf-8
from .fields.ages import AgeColumnProcessor
from .fields.base_fields import AbstractDataProcessor, DictColumnProcessor, BaseColumnProcessor
from .fields.birth_years import BirthYearColumnProcessor
from .fields.boolean_fields import BoolColumnProcessor
from .fields.dates import DateColumnProcessor


class MemoDataProcessor(AbstractDataProcessor):
    fields = [
        DictColumnProcessor(column='surname'),
        DictColumnProcessor(column='name'),
        DictColumnProcessor(column='patronimic'),
        BirthYearColumnProcessor(column='birth_year'),
        AgeColumnProcessor(column='age'),
        DictColumnProcessor(column='sex'),
        DictColumnProcessor(column='birth_place'),
        DictColumnProcessor(column='nation'),
        DictColumnProcessor(column='citizenship'),
        BaseColumnProcessor(column='occupation'),
        DictColumnProcessor(column='live_place'),
        DictColumnProcessor(column='education'),
        DictColumnProcessor(column='party'),
        BaseColumnProcessor(column='family'),
        DateColumnProcessor(column='arest_date'),
        BaseColumnProcessor(column='arest_organ'),
        BaseColumnProcessor(column='arest_type'),
        BaseColumnProcessor(column='criminal_case'),
        BaseColumnProcessor(column='judicial_organ'),
        DateColumnProcessor(column='process_date'),
        BaseColumnProcessor(column='criminal_article'),
        BaseColumnProcessor(column='sentence'),
        BoolColumnProcessor(column='was_executed'),
        BaseColumnProcessor(column='death_place'),
        DateColumnProcessor(column='death_date'),
        DictColumnProcessor(column='rehabilitation_organ'),
        DictColumnProcessor(column='rehabilitation_reason'),
        DateColumnProcessor(column='rehabilitation_date'),
        DictColumnProcessor(column='memory_book'),

    ]
