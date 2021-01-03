#!/usr/bin/env python

class SetPower:
	def __init__(self, power_cfg):
		self.power_cfg = power_cfg

	def getCurrentThreshold(self):
		with open(self.power_cfg, "r") as power_cfg:
			print("Current Threshold\t:", power_cfg.read())
	
	def getNewThreshold(self):
		while(True):
			try:
				newThreshold = int(input("Enter New Threshold\t: "))
				break
			except ValueError:
				input("[ERROR] Wrong Input Format!")
		
		self.newThreshold = str(newThreshold)

	def setNewThreshold(self):
		with open(self.power_cfg, "w") as power_cfg:
			power_cfg.write(self.newThreshold)


def main():
	# Power threshold configuration file
	power_cfg_dir = "/sys/class/power_supply/BAT0/charge_control_end_threshold"

	setPower = SetPower(power_cfg_dir)
	setPower.getCurrentThreshold()
	setPower.getNewThreshold()
	setPower.setNewThreshold()


if __name__ == '__main__':
	main()

