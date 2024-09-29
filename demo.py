from prizm.console import Console

if __name__ == "__main__":
	console = Console()

	console.log("Log test!")
	console.log("Log test 2!")
	console.log("Log test 3!")
	console.log("Log test 4!")
	console.log("Log test 5!")

	console.log("Terminal color test!", color="BBLU")
	console.log("Terminal color test 2!", color="BRED")
	console.log("Terminal color test 3!", color="GRE")
	console.log("Terminal color test 4!", color="MAG")
	console.log("Terminal color test 5!", color="CYA")

	console.terminal = False

	console.log("Terminal color test!", color="BBLU")
	console.log("Terminal color test 2!", color="BRED")
	console.log("Terminal color test 3!", color="GRE")
	console.log("Terminal color test 4!", color="MAG")
	console.log("Terminal color test 5!", color="CYA")
