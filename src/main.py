import subprocess
from datetime import datetime
from const import *


formatted_date_and_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Open log file in append mode
with open('log.txt', 'a', encoding='utf-8') as log_file:
    # Write start execution message to log file
    log_file.write("\n--- Execution : {} ---\n".format(formatted_date_and_time))


    # Run subprocess and capture stdout
    result = subprocess.run(['python', 'src/animationCreation.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log_file.write(result.stdout.decode(encoding='utf-8'))

    result = subprocess.run(['python', 'src/merge.py', 'temp/output_audio.mp3', 'temp/output_video.mp4', 'output/finalOutput.mp4'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Write stdout to log file
    log_file.write(result.stdout.decode(encoding='utf-8'))  # Decode bytes to string for writing

    # Write end execution message to log file
    formatted_date_and_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write("\n--- Execution ended : {} ---\n".format(formatted_date_and_time))