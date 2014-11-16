

from ScenarioParser import ScenarioParser
from UdpAgent import UdpSender
from RepeatedTimer import RepeatedTimer

from time import sleep
#import time

if __name__ == '__main__':
	sp = ScenarioParser("scenario.yaml")
	scenario = sp.get_scenario()

	udpSender = UdpSender((scenario["ip"],scenario["port"]))

	if (scenario["direction"] == "out"):
		rt = RepeatedTimer(1, udpSender.send, scenario["data"])

	try:
	    sleep(5) # your long-running job goes here...
	finally:
	    rt.stop() # better in a try/finally block to make sure the program ends!
