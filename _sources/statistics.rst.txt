.. orphan::

Anonymous Statistics (Disabled)
================================

Note: This page is currently disabled from the documentation navigation and cross-links. Anonymous statistics collection is not active in this version of MRD. Keep this page for potential future re-enablement.

The Mavryk Reward Distributor previously collected anonymous statistics after each payout. These statistics were purely for analytical purposes.

Nothing that MRD collects can be traced back to a specific delegate or delegator. The goal of the statistics is not to correlate nor discover specific validatories that are using MRD.

* We *do not* collect any implicit or originated addresses.
* We *do not* collect any IP, or hostname related information.
* Anonymous identifiers are calculated using an MD5 hash of the payout address.

Stats are not collected in this version of MRD. The `--do_not_publish_stats` option is not needed.

If you have any questions about this topic or if you want to have access to the statistical data feel free to open an issue.

Collected Data
--------------

MRD collects the following statistics after each payout:

* Anonymous identifier
* Payout cycle
* Total payout amount
* Which network is in use (ie: mainnet, testnets, etc)
* Number of founders
* Number of owners
* Number of delegators
* Number of payments
* Number of failed transactions
* Number of injected transactions
* Number of attempts
* If validator pays transfer fee
* If validator pays reactivation fee
* If MRD is running as a background service
* Which RPC provider is in use
* Release override setting
* Payment offset setting
* If docker is being used
* Python version
* OS version
* MRD Version

Transfer
--------

Previously, a POST request was sent to the following AWS Lambda endpoint:

    https://mrdstats

This endpoint did not collect any information about the source of the POST. No cookies were used.
Stats are not collected in this version of MRD so the functionality remains disabled.

GDPR
----

The General Data Protection Regulation, Recital 26 provides exception to anonymous and pseudonymous information.

Due to the anonymous nature of the collected data, MRD is within compliance of the GDPR.
