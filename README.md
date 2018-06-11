## Simple example sending DHT11 data to an MQTT endpoint

This tutorial uses the Adafruit DHT library to read data from a DHT 11 temperature/humidity
sensor and sends it to an MQTT endpoint.

### Installing Adafruit library

The full instructions for installing the library is [here](https://github.com/adafruit/Adafruit_Python_DHT).

In short:

```
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT/
python setup install --user
python ./setup.py install --user
```

### Install requirements.txt

`requirements.txt` has a few modules that are required.  To isntall:

```
pip install -r requirements.txt
```

### Operating the script

The script requires that it be run as root.  Do do that:

```
sudo ./dht_to_mqtt.py
```
