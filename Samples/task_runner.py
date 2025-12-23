import subprocess

def run_task(task):
    subprocess.call(task, shell=True)
