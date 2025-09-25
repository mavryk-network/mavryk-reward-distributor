<img src="https://raw.githubusercontent.com/habanoz/trd-art/master/logo-narrow/trd_512__1.png" width="128" /> 

# MRD

**MRD** is a fork of the [TRD](https://github.com/tezos-reward-distributor-organization/mavryk-reward-distributor) project.  
This fork is distributed under the terms of the [GNU General Public License v3.0](./LICENSE).  

All modifications made in this fork are released under the same license, ensuring that users have the freedom to use, study, modify, and redistribute the software.  

DISCLAIMER: MAVRYK REWARD DISTRIBUTOR IS PROVIDED AS IS. IT IS UNDER CONSTANT DEVELOPMENT. EVENT THOUGH IT IS WELL TESTED, PLEASE USE IT WITH CARE. ALWAYS MAKE A PRE-RUN IN DRY MODE BEFORE MAKING ACTUAL PAYMENTS. IF YOU WANT TO RUN IN SERVICE MODE DO IT AFTER YOU ARE CONFIDENT WITH THE APPLICATION. IN SERVICE MODE ONLY UPDATE IF NEEDED.

PRIVACY: MAVRYK REWARD DISTRIBUTOR COLLECTS ANONYMOUS STATISTICS. PLEASE READ OUR [STATISTICS POLICY](https://mavryk-network.github.io/mavryk-reward-distributor/statistics.html) FOR MORE INFORMATION.

## Mavryk Reward Distributor: Run & Forget

[![Actions Status](https://github.com/mavryk-network/mavryk-reward-distributor/workflows/CI/badge.svg)](https://github.com/mavryk-network/mavryk-reward-distributor/actions)
[![Documentation Status](https://github.com/mavryk-network/mavryk-reward-distributor/workflows/Docs/badge.svg)](https://github.com/mavryk-network/mavryk-reward-distributor/actions)
[![Stable Documentation Status](https://img.shields.io/badge/docs-stable-blue.svg)](https://mavryk-network.github.io/mavryk-reward-distributor/)

MRD is a software for distributing staking rewards of Mavryk delegators, introduced in detail in this [Medium article](https://medium.com/@huseyinabanox/mavryk-reward-distributor-e6588c4d27e7). This is not a script but a full scale application which can continuously run in the background as a Linux service. It can track cycles and make payments. However, it does not have to be used as a service, but it can also be used interactively.

The documentation can be found [here](https://mavryk-network.github.io/mavryk-reward-distributor/). 

MRD supports complex payments, pays in batches, and supports three backends for calculations: Mavryk RPC and [MvKT API](https://api.mavryk.network/). MRD is developed and tested extensively by the community.

**Provider notes:**

### MvKT

The [terms of use](https://api.mavryk.network/#section/Terms-of-Use) of MvKT API allow for commercial and non-commercial use.

> MvKT API is free for everyone and for both commercial and non-commercial usage.
>
> If your application or service uses the MvKT API in any forms: directly on frontend or indirectly on backend, you should mention that fact on your website or
> application by placing the label "Powered by MvKT API" with a direct link to [api.mavryk.network](https://api.mavryk.network).

## Requirements and Setup

The setup instructions are Linux specific. Python 3 is required. You can use the following commands to install it.

```bash
sudo apt-get update
sudo apt-get -y install python3-pip
```

Download the application repository using git clone:

```bash
git clone https://github.com/mavryk-network/mavryk-reward-distributor
```

To install required modules, use pip with `requirements.txt` provided. Follow the instructions to create a virtual environment for your project specific python installation: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

```bash
python3 -m venv .venv
source .venv/bin/activate
```

```bash
cd mavryk-reward-distributor
python3 -m pip install -r requirements.txt
```

To install the required modules for developers, use pip with `requirements_developers.txt` provided.

```bash
cd mavryk-reward-distributor
python3 -m pip install -r requirements_developers.txt
```

Regularly check and upgrade to the latest available version:

```bash
git fetch origin #fetches new branches
git status #see the changes
git pull
```

## Sample configuration

Before running MRD, you need to configure it by adding your baker's address and payout settings.
The configuration file should be included in the `~/pymnt/cfg/` directory by default. You can use the following command to copy and modify the example configuration:

```bash
# create directory
mkdir -p ~/pymnt/cfg/
cp mavryk-reward-distributor/examples/mv1BooTWe9vnuvN1o756pE6yC8jNcsVDCp9N.yaml ~/pymnt/cfg/
nano ~/pymnt/cfg/mv1BooTWe9vnuvN1o756pE6yC8jNcsVDCp9N.yaml
```

## How to Run

For a list of parameters, [read the online documentation](https://mavryk-network.github.io/mavryk-reward-distributor/run.html), or run:

```bash
python3 src/main.py --help
```

The most common use case is to run in **mainnet** and start to make payments for the latest released rewards or continue making payments from the cycle after the last payment was done.

```bash
python3 src/main.py
```

MRD necessitates of an interface to get provided with income and delegator data in order to perform the needed calculations.

The default provider is the MvKT API. However, it is possible to change the data provider to a local node with the flag `-P rpc`.
In this case, the default node would be `127.0.0.1:8732`. In order to change the node URL for the provider, you can pass it in the form `node_url:port` using the flag `-A` (e.g. `-P rpc -A 127.0.0.1:8733`). Please note that the node should be an [archive node](https://protocol.mavryk.org/user/history_modes.html#setting-up-a-node-in-archive-mode), and that the port should be the RPC port specified while launching the node.

It is also possible to use a public RPC node with flag `-P prpc`, which defaults to `https://rpc.mavryk.network`.
