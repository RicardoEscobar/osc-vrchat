"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import time
import logging

from pythonosc import udp_client

# Create logging system.
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Send logs to console.
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# Create formatter.
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Add formatter to ch.
ch.setFormatter(formatter)
# Add ch to logger.
logger.addHandler(ch)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=5005,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  for x in range(10):
    client.send_message("/filter", random.random())
    logger.info("Sent message to /filter with value: %s", str(random.random()))
    time.sleep(1)