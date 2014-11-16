#import json
import yaml
import struct


class ScenarioParser():
	def __init__(self,scenario_file):
		self._scenario_file = scenario_file
		self.format = []

	def _parse_type(self,format,val):
		self.format.append(format)
		return struct.pack(format,val)


	def _parse_scenario(self):
		# scen_file=open(self._scenario_file)
		# scen = json.load(scen_file)

		with open(self._scenario_file, 'r') as scen_file:
			scen = yaml.load(scen_file)
		
		scen_file.close()

		scen_config = {}
		scen_config["ip"] 			= scen["ip"]
		scen_config["port"] 		= scen["port"]
		scen_config["direction"]	= scen["direction"]
		scen_config["rate"]			= scen["rate"]



		parse_types = {
		  'int8'	: lambda x: self._parse_type('b',x),
		  'uint8'	: lambda x: self._parse_type('B',x),
		  'int'		: lambda x: self._parse_type('l',x),
		  'int32'	: lambda x: self._parse_type('l',x),
		  'uint32'	: lambda x: self._parse_type('L',x),
		  'uint64'	: lambda x: self._parse_type('Q',x)
		}

		packet = []
		for e in scen["data"]:
			for key in e:
				num = parse_types[key](int(e[key],0))
				packet.append(num)
				# print type(packet)

		scen_config["data"] = (b''.join(packet))

		return scen_config
	
	def get_scenario(self):
		return self._parse_scenario()

	def packet_size(self):
		return struct.calcsize(b''.join(self.format))


if __name__ == '__main__':
	# sp = ScenarioParser("scenario1.json")
	sp = ScenarioParser("scenario.yaml")
	print sp.get_scenario()
	print "Data size:" , sp.packet_size(), "bytes"





