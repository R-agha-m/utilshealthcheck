from utilscommon.utilscommon.string_case_convertor import (
    string_case_convertor,
    EnumCaseStrategy,
)

NAME = "report"

CAMEL_CASE_NAME = string_case_convertor(
    text=NAME,
    split_char=' ',
    join_char='',
    case_strategy=EnumCaseStrategy.CAMEL
)

PASCAL_CASE_WITH_SPACE_NAME = string_case_convertor(
    text=NAME,
    split_char=' ',
    join_char=' ',
    case_strategy=EnumCaseStrategy.PASCAL,
)

LOWER_SNAKE_CASE = string_case_convertor(
    text=NAME,
    split_char=' ',
    join_char='_',
    case_strategy=EnumCaseStrategy.LOWER,
)

LOWER_KEBAB_CASE = string_case_convertor(
    text=NAME,
    split_char=' ',
    join_char='-',
    case_strategy=EnumCaseStrategy.LOWER,
)