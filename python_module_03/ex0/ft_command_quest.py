import sys

syslist = sys.argv

n = 1
if (len(syslist) == 1):
	print(f"Program name: {syslist[0]}")
	print("No arguments provided")
	print(f"Total arguments: 1\n")
else:
	print(f"Program name: {syslist[0]}")
	print(f"Arguments received: {len(syslist) - 1}")
	for name in syslist[1:]:
		print(f"Argument {n}: {name}")
		n += 1
	print(f"Total arguments: {len(syslist)}\n")


