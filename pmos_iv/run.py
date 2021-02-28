import subprocess

subprocess.call(["/Applications/LTspice.app/Contents/MacOS/LTspice", "-b", "./pmosfet-iv.cir"])

with open('LOG', 'w') as f:
    subprocess.Popen(["iconv", "-f", "UCS-2LE", "-t", "US-ASCII", "pmosfet-iv.log"], stdout=f)

