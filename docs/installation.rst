How to get and install MRD?
=====================================================

Requirements and Setup
------------------------


Python 3
-----------

Mac: 

::

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    brew install python3

Linux:

::

    sudo apt-get update
    sudo apt-get -y install python3-pip

Mavryk
-----------

Mac: 

::

    brew install hidapi libev wget

Mac & Linux:

Follow instructions found here: https://protocol.mavryk.org/introduction/howtoget.html

MRD
-----------

::

    git clone https://github.com/mavryk-network/mavryk-reward-distributor.git

To install required modules, use pip with requirements.txt provided:

::

    cd mavryk-reward-distributor
    pip3 install -r requirements.txt

To install required pre-commit hooks into .git folder:

::

    pre-commit install

Regulary check and upgrade to the latest available version:

::

    git pull
