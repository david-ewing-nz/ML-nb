# PowerShell script to fully automate git add, commit, pull --rebase, and push for all files
# Handles renames, deletions, and notebook changes in one go
# Usage: Run this script in the repo root to sync and push all changes automatically

# Stage all changes (including renames and deletions)
Write-Host "Staging all changes..."
git add -A

# Commit with a generic message (edit as needed)
$commitMsg = "Auto-sync: stage, commit, rebase, and push all changes (including renames and deletions)."
git commit -m $commitMsg

# Pull with rebase to avoid non-fast-forward errors
Write-Host "Pulling with rebase..."
git pull --rebase

# Push to remote
Write-Host "Pushing to remote..."
git push

Write-Host "Git sync and push complete."
