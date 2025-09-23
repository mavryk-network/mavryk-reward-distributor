from enum import Enum


class AddrType(Enum):
    KT = 1
    MV = 2
    KTALS = 3
    MVALS = 4

    def is_kt(self):
        return self.value == 1

    def is_mv(self):
        return self.value == 2

    def is_ktals(self):
        return self.value == 3

    def is_mvals(self):
        return self.value == 4

    @staticmethod
    def to_string(obj):
        self = obj
        if self.value == 1:
            return "KT"
        if self.value == 2:
            return "MV"
        if self.value == 3:
            return "KTALS"
        if self.value == 4:
            return "MVALS"

    def __str__(self):
        return self.name
