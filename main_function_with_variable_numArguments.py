def main(*args):
	'''main function that takes variable number of arguments from the command line.
	Follow the logic below to learn how to pass variable number of arguments into the command
	prompt with a python script.
	
	usage would look like:
	
	C:> myScript.py my_first_argument my_second_argument --third 42 --fourth myFourthArgValue
	
	The second two arguments passed are optional and don't need to be there.
	'''

	import argparse
	from otherFile import myFunction

	parser = argparse.ArgumentParser(description='My example explanation')

	parser.add_argument('my_first_argument', type=str, help='this arg is mandatory')
	parser.add_argument('my_second_argument', type=str, help='this arg is also mandatory')
	parser.add_argument(
		'--third',
		type=int,
		default=3,
		help='this argument is optional because it has a default value (default: 3)'
	)
	parser.add_argument(
		'--fourth',
		help='this argument is optional as sorted by logic below'
	)
	args = parser.parse_args() #argumnet definition is done

	arg1 = args.my_first_argument
	arg2 = args.my_second_argument
	optionalArgs3 = args.third
	
	if args.fourth:
		optionalArgs4 = args.fourth
	else:
		optionalArgs4 = 'none'
		
	someReturnValues = myFunction(my_first_argument,my_second_argument,optionalArgs3,optionalArgs4)

	print(someReturnValues)

if __name__ == "__main__":
    import sys 
    main(*sys.argv) #Takes any arguments as a long string and passes them into the main funcion.
	#argparse can still interprete them downstream.  This way there's no set number of arguments
	#expected by the main function.