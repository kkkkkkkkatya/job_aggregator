from enum import Enum

class PlatformEnum(str, Enum):
    JOOBLE = "jooble"
    DJINNI = "djinni"
    DOU = "dou"

class PipelineType(str, Enum):
    VACANCY = "vacancy"
