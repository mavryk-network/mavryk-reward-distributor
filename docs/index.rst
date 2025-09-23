Mavryk Reward Distributor (MRD)
======================================================

|Build Status| |Docs Status| |Stable Documentation Status|

DISCLAIMER : MAVRYK REWARD DISTRIBUTOR IS PROVIDED AS IS. IT IS UNDER CONSTANT DEVELOPMENT. EVENT THOUGH IT IS WELL TESTED, PLEASE USE IT WITH CARE. ALWAYS MAKE A PRE-RUN IN DRY MODE BEFORE MAKING ACTUAL PAYMENTS. IF YOU WANT TO RUN IN SERVICE MODE DO IT AFTER YOU ARE CONFIDENT WITH THE APPLICATION. IN SERVICE MODE ONLY UPDATE IF NEEDED.

PRIVACY : MAVRYK REWARD DISTRIBUTOR COLLECTS ANONYMOUS STATISTICS. PLEASE READ OUR STATISTICS POLICY_ FOR MORE INFORMATION.

What's MRD?
------------------------------------------------

MRD is an open-source software for distributing delegation rewards from bakers to delegators. This is a full scale application which can continuously run in the background as a Linux service. However it does not have to be used as a service, but it can also be used interactively. The tool convinces with its simplicity and yet leaves no configuration wish unfulfilled. Whether minimum delegation threshold, or special fees for some delegators - the MRD covers just about all possible constellations. Furthermore, the tool supports complex payments, pays in batches. It uses MvKT_ API as backend. MRD is developed and tested extensively by the community and the source code which can be found in the following Github_ repo.

**Since 2024, Mavryk offers two kind of rewards: delegating rewards and staking rewards. MRD pays out delegation rewards.** Staking rewards are paid by the protocol, and MRD does not concern itself with them.

Who needs MRD?
------------------------------------------------

The MRD is needed by bakers who want to pay delegation rewards. There are a few payout tools available in the Mavryk ecosystem. However, the MRD is probably the most used open source payout tool by bakers. It ranges from small bakers with a couple of delegators to large bakers with more than thousand delegators. The maintainers strive to keep up with the growing Mavryk ecosystem. This in turn enables MRD users to participate in the exploration of new business areas like baking for liquidity pools or DAOs.

In 2024, another popular payout distribution software is [TezPay](https://github.com/mav-capital/tezpay).

What else do you need for MRD?
------------------------------------------------

There are currently the following options to run MRD:

    a. If you want to inject your own transactions, at least a Mavryk rolling node is needed.
    b. If you don't want to inject your own transactions, only the Mavryk signer is needed.

However, for all options the Mavryk signer is needed.

MvKT
-----------

The backend of the Mavryk Reward Distributor is `Powered by MvKT API`__ under the following terms:

    MvKT API is free for everyone and for both commercial and non-commercial usage.
    
    If your application or service uses the MvKT API in any forms: directly on frontend or indirectly on backend, you should mention that fact on your website or application by placing the label "Powered by MvKT API" with a direct link to api.mavryk.network.

.. _POLICY : statistics.html

.. _article : https://medium.com/@huseyinabanox/mavryk-reward-distributor-e6588c4d27e7

.. _tzpro: https://tzpro.io/

.. _MvKT : https://api.mavryk.network/

.. _terms : https://tzpro.io/terms

.. _Github : https://github.com/mavryk-network/mavryk-reward-distributor

.. _PR232 : https://github.com/mavryk-network/mavryk-reward-distributor/pull/232

.. _API : https://api.mavryk.network/

__ API_

Funding
------------------------

MRD is an open source, GPL licensed project. It is maintained by various community members.

MRD Art Work
------------------------

This Github Repo_ contains logo images. If you are using MRD and want to let everybody know about it, feel free to place them in your website.

.. |Build Status| image:: https://github.com/mavryk-network/mavryk-reward-distributor/workflows/CI/badge.svg
   :target: https://github.com/mavryk-network/mavryk-reward-distributor/actions
.. |Docs Status| image:: https://github.com/mavryk-network/mavryk-reward-distributor/workflows/Docs/badge.svg
   :target: https://github.com/mavryk-network/mavryk-reward-distributor/actions
.. _Repo: https://github.com/mavryk-reward-distributor-organization/mrd-art
.. |Stable Documentation Status| image:: https://img.shields.io/badge/docs-stable-blue.svg
   :target: https://mavryk-network.github.io/mavryk-reward-distributor/

.. toctree::
   :maxdepth: 2
   :caption: Content:

   installation
   configuration
   paymentaddress
   mavryksigner
   run
   rundocker
   plugins
   linuxservice
   state_machine
   contributors
   multisig_payouts
   testing
   statistics
   codeofconduct
