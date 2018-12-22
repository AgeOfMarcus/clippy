#!/usr/bin/python3
from subprocess import Popen, PIPE
import os, argparse

sh = lambda cmd: Popen(cmd,stdout=PIPE,shell=True).communicate()[0].strip()

read = lambda: sh("xsel -b").decode()
write = lambda x: os.system("echo -n \"%s\" | xsel -b" % x)

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"-r","--read",
		help=("Read from the clipboard"),
		action="store_true")
	parser.add_argument(
		"-w","--write",
		help=("Write to the clipboard"),
		type=str)
	return parser.parse_args()
def main(args):
	if not args.read and not args.write:
		return 1
	elif args.read:
		print(read())
		return 0
	elif args.write:
		return write(args.write)
	else:
		return 1
if __name__ == "__main__":
	exit(main(parse_args()))
