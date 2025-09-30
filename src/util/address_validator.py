from Constants import PKH_LENGTH
from exception.configuration import ConfigurationException


class BaseError(Exception):
    pass


class IncorrectAddressError(BaseError):
    pass


class IncorrectLengthError(BaseError):
    pass


class AddressValidator:
    def __init__(self, context=None) -> None:
        super().__init__()
        self.context = context

    def validate(self, address):
        if not address.startswith("mv") and not address.startswith("KT"):
            raise IncorrectAddressError(
                "Incorrect input in {}, '{}' is not a mv or KT address".format(
                    self.context, address
                )
            )

        if len(address) != PKH_LENGTH:
            raise IncorrectLengthError(
                "Incorrect input in {}, '{}' length must be {}".format(
                    self.context, address, PKH_LENGTH
                )
            )

    def mv_validate(self, address):
        if len(address) != PKH_LENGTH or not address.startswith("mv"):
            raise Exception(
                "Payment address cannot be translated into a PKH or is kt script: {}".format(
                    address
                )
            )

    @staticmethod
    def isaddress(address):
        return len(address) == PKH_LENGTH and (
            address.startswith("mv") or address.startswith("KT")
        )

    def validate_baking_address(self, baking_address):
        if not self.isaddress(baking_address):
            raise ConfigurationException(
                "Baking address must be a valid mv address of length {}".format(
                    PKH_LENGTH
                )
            )
        if baking_address.startswith("KT"):
            raise ConfigurationException(
                "KT addresses cannot act as validators. Only mv addresses can be registered to bake."
            )
