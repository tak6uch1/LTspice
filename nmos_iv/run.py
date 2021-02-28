import subprocess

subprocess.call(["/Applications/LTspice.app/Contents/MacOS/LTspice", "-b", "./nmosfet-iv.cir"])

with open('LOG', 'w') as f:
    subprocess.Popen(["iconv", "-f", "UCS-2LE", "-t", "US-ASCII", "nmosfet-iv.log"], stdout=f)

