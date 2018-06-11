#!/usr/bin/python

# required libraries
import json
import time
import Adafruit_DHT
import paho.mqtt.client as mqtt

# config
SENSOR_LOCATION = 'front_room'
SENSOR_ID = SENSOR_LOCATION + '_dht_1'
SENSOR_TYPE = '2302'
SENSOR_PIN = 60
MQTT_END_POINT = {
    'host': '10.42.1.91',
    'port': 1883,
    'username': 'mqtt',
    'password': 'sensorythings'
}
MQTT_SENSOR_TOPIC = "sensor/dht"
POLLING_FREQUENCY = 10

SENSOR_MAPPING = {
    '11':   Adafruit_DHT.DHT11,
    '22':   Adafruit_DHT.DHT22,
    '2302': Adafruit_DHT.AM2302
}

def read_sensor(sensor, pin):
    print "read sensor"
    # read_retry will 
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return humidity, temperature

def publish_reading(client, endpoint, topic, id, location, humidity, temperature):
    print "publish"
    # setup sensor payload
    payload = {
        'location': location,
        'humidity': humidity,
        'temperature': temperature
    }
    payload_json = json.dumps(payload)

    # create MQTT client
    client.connect(endpoint['host'], endpoint['port'])
    client.publish(topic, payload_json)
    return 0

def main():
    # validate config

    # setup mqtt client
    client = mqtt.Client(SENSOR_ID)
    client.username_pw_set(MQTT_END_POINT['username'], MQTT_END_POINT['password'])
    
    # execute loop
    while True:
        print "in loop"
        humidity, temperature = read_sensor(SENSOR_MAPPING[SENSOR_TYPE], SENSOR_PIN)
        if humidity is None and temperature is None:
            print "Failed to get reading."
        else:
            # publish values
            result = publish_reading(client, MQTT_END_POINT, MQTT_SENSOR_TOPIC, SENSOR_ID, SENSOR_LOCATION, humidity, temperature)
            if result is not 0:
                print "Failed to publish reading."
        time.sleep(POLLING_FREQUENCY)

if __name__ == "__main__":
    main()