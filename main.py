import subprocess

# Command to execute the bot.py file
cmd_bot = ['python3.11', "bot.py"]
cmd_cv = ['python3.11', "CV_webcam.py"]

# Launch subprocess for bot.py
subprocess.Popen(cmd_bot)
subprocess.Popen(cmd_cv)
#%%
