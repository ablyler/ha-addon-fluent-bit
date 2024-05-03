import json
import subprocess
import time

with open("/data/options.json", "r") as options_file:
    options = json.loads(options_file.read())
    print(f"Using options: {options}")

# generate a temp path to store the config file
CONFIG_PATH = f"/config/{options['config_file']}"

FLUENT_BIT_COMMAND = [
    "/opt/fluent-bit/bin/fluent-bit",
    "-c", CONFIG_PATH
]
# run the FLUENT_BIT_COMMAND command
while True:
    print(f"Running command: {FLUENT_BIT_COMMAND}")
    result = subprocess.run(FLUENT_BIT_COMMAND)
    print(f"Command exited with code: {result.returncode}")
    time.sleep(5)