import os
import time

def auto_commit_push(repo_path, interval=300, commit_message="Auto-commit: Save and push notebook changes"):
    os.chdir(repo_path)
    while True:
        os.system('git add .')
        os.system(f'git commit -m "{commit_message}"')
        os.system('git push')
        time.sleep(interval)

# Usage:
# auto_commit_push(r'd:\github\ML-nb', interval=300)
# To run: python auto_git_push.py
