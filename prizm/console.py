import time
from prizm.util.color import (
	RED, GRE, YEL, BLU, MAG, CYA,
	BRED, BGRE, BYEL, BBLU, BMAG, BCYA
)
from prizm.util.file import path_exists

class Console:
	"""
	A class for handling console output with optional logging to a file.

	Attributes:
		directory (str): The directory where log files will be stored.
		terminal (bool): Indicates whether to output messages to the terminal.
		_log (bool): Flag to enable or disable logging.
		path (str): The path for the current log file.
		labels (list): List of labels to categorize log messages.
	"""

	def __init__(self, directory="./log/", terminal=True):
		"""
		Initializes the Console class.

		Args:
			directory (str): The directory for log file storage. Default is './log/'.
			terminal (bool): Indicates whether to log output to the terminal. Default is True.

		Raises:
			ValueError: If the directory does not exist.
		"""
		self.directory = directory  # Set the log directory
		path_exists(directory)  # Check if the directory exists
		self.terminal = terminal  # Set whether to output to the terminal
		self._log = True  # Initialize logging as enabled
		timestamp = int(time.time() * 1000)  # Get the current timestamp in milliseconds
		self.path = self.directory + str(timestamp) + ".log"  # Set the log file path
		self.labels = []  # Initialize an empty list for labels

	def _write(self, *args):
		"""
		Writes messages to the log file.

		Args:
			*args: Messages to log, passed as individual arguments.

		Side Effects:
			If a log path is set, appends the message to the log file.
		"""
		if self.path is not None:  # Check if a log path is defined
			path = f"./log/{self.path}"  # Construct the full path to the log file
			path_exists(path)  # Ensure the log path exists
			with open(path, "a") as f:  # Open the log file in append mode
				f.write(" ".join(map(str, args)) + "\n")  # Write the message to the file

	def label(self, label):
		"""
		Adds a label to the list of labels.

		Args:
			label (str): The label to add.
		"""
		self.labels.append(label)  # Append the label to the labels list

	def warning(self, *args):
		"""
		Outputs a warning message to the console and logs it.

		Args:
			*args: The warning message to display and log.
		"""
		print("\033[1;35mWARNING: \033[0m", end="")  # Print the warning header in magenta
		for arg in args:  # Iterate through the message components
			print(arg, end=" ")  # Print each part of the message
		self._write("WARNING:", *args)  # Log the warning message

	def error(self, *args):
		"""
		Outputs an error message to the console and logs it.

		Args:
			*args: The error message to display and log.
		"""
		print("\033[1;31mERROR: \033[0m", end="")  # Print the error header in red
		for arg in args:  # Iterate through the message components
			print(arg, end=" ")  # Print each part of the message
		self._write("ERROR:", *args)  # Log the error message
		
	def err(self, *args):
		self.error(*args)
		
	def warn(self, *args):
		self.warning(*args)
		
	def out(self, *args, color=None):
		self._color_switch(color, *args)  # Print with specified color
		if self.path is not None:  # If a log path is defined
			self._write(*args) 

	def set_log(self, log_gate: bool):
		"""
		Sets the logging state.

		Args:
			log_gate (bool): True to enable logging, False to disable.
		"""
		self._log = log_gate  # Update the logging state

	def _color_switch(self, color, *args):
		"""
		Prints messages in specified colors based on the given color name.

		Args:
			color (str): The color code to use for printing messages.
			*args: The message components to print.
		"""
		if color is None:  # If no color specified, print normally
			print(*args)
		elif color == "GRE":
			GRE(*args)  # Call the GRE function for green output
		elif color == "RED":
			RED(*args)  # Call the RED function for red output
		elif color == "BLU":
			BLU(*args)  # Call the BLU function for blue output
		elif color == "YEL":
			YEL(*args)  # Call the YEL function for yellow output
		elif color == "MAG":
			MAG(*args)  # Call the MAG function for magenta output
		elif color == "CYA":
			CYA(*args)  # Call the CYA function for cyan output
		elif color == "BGRE":
			BGRE(*args)  # Call the BGRE function for bold green output
		elif color == "BRED":
			BRED(*args)  # Call the BRED function for bold red output
		elif color == "BBLU":
			BBLU(*args)  # Call the BBLU function for bold blue output
		elif color == "BYEL":
			BYEL(*args)  # Call the BYEL function for bold yellow output
		elif color == "BMAG":
			BMAG(*args)  # Call the BMAG function for bold magenta output
		elif color == "BCYA":
			BCYA(*args)  # Call the BCYA function for bold cyan output

	def log(self, *args, color=None, label=None):
		"""
		Logs messages to the console and/or to a file based on settings.

		Args:
			*args: The message components to log.
			color (str, optional): The color to use when printing to the terminal.
			label (str, optional): A label to filter messages if labels are being used.

		Behavior:
			If a label is specified and it exists in the labels list, the message is logged.
			If no label is provided, the message is logged regardless of labels.
		"""
		if label is not None:  # If a label is specified
			if label in self.labels:  # Check if the label exists in the labels list
				if self.terminal is True:  # Check if terminal logging is enabled
					self._color_switch(color, *args)  # Print with specified color
					if self.path is not None:  # If a log path is defined
						self._write(*args)  # Log the message
				elif self.path is not None:  # If terminal logging is disabled
					self._write(*args)  # Log the message
		else:  # If no label is specified
			if self.terminal is True:  # Check if terminal logging is enabled
				self._color_switch(color, *args)  # Print with specified color
				if self.path is not None:  # If a log path is defined
					self._write(*args)  # Log the message
			elif self.path is not None:  # If terminal logging is disabled
				self._write(*args)  # Log the message
