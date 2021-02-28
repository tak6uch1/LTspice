import subprocess

subprocess.call(["/Applications/LTspice.app/Contents/MacOS/LTspice", "-b", "./inv_example.cir"])

with open('LOG', 'w') as f:
    subprocess.Popen(["iconv", "-f", "UCS-2LE", "-t", "US-ASCII", "inv_example.log"], stdout=f)

