# Schiavo
Easy discord message forward bot.  
This is mainly used as a logger to forward messages from other applications into discord for easy access and shameless logging. Python implementation of usage can be found [here](https://github.com/osufx/ripple-python-common/blob/master/web/schiavo.py).

## Usage
This bot exposes an endpoint which will forward a message to the specified discord channel.  
Example usage: `http://localhost:5009/general?message=Hello%20world`  
Sample above will send the message `Hello world` to the channel `#general` for the chosen `guild`.

## Setup
Install dependencies: `$ python3 -m pip install -r requirements.txt`  
Start bot: `$ python3 main.py`  
Configuration can be found and edited in `config.json`

### WARNING
Never allow unauthorized access to this endpoint! You are self responsible to set this up in a secure way that does not allow outsiders to access and send messages on your behalf.