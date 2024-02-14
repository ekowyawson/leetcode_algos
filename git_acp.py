#!/bin/python3
import subprocess

def run_command(command):
    try:
        # Execute the command
        result = subprocess.run(command, check=True, text=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Success: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.cmd}\nError message: {e.stderr}")
        return False

def git_add():
    command = "git add ."
    return run_command(command)

def git_commit():
    commit_message = input("Enter your commit message: ")
    command = f"git commit -m \"{commit_message}\""
    return run_command(command)

def git_push():
    # First, find the current branch name
    branch_command = "git rev-parse --abbrev-ref HEAD"
    result = subprocess.run(branch_command, check=True, text=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    current_branch = result.stdout.strip()

    command = f"git push origin {current_branch}"
    return run_command(command)

# Execute the steps
if git_add():
    if git_commit():
        git_push()

