Payment Address
===============

MRD is designed to work as a linux service. It expects the usage of the Mavryk signer for encrypted payment accounts.

An address can only be used for payments if it satisfies the following criteria:

- The public key of the address must be revealed. See the Mavryk command line interface on how to run reveal command using the Mavryk client e.g. If an address is registered as delegate, there is no need to run the reveal command.

  ::

      ./octez-client reveal key for <alias>

- The payment address must be an implicit address (mv). The secret key of the address must be known and imported to the signer before running the MRD. Please refer to the Mavryk signer section for detailed instructions. 
