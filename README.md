<<<<<<< HEAD
# MyPython workspace

This repository contains a collection of small Python exercises and coursework organized by week. It includes example scripts, notebooks, and sample data files.

Suggested repository name: `python-scripts` (you can choose another name). The example remote URL would be:

    https://github.com/FussionPK/python-scripts.git

Quick push instructions (PowerShell) — run these from `C:\Users\Fussion\Desktop\MyPython` after you have Git installed and authenticated with GitHub.

1) If this folder is not already initialized as a git repo:

```powershell
git init
git add -A
git commit -m "Initial commit of MyPython workspace"
git branch -M main
git remote add origin https://github.com/FussionPK/python-scripts.git
git push -u origin main
```

2) If you prefer to create the GitHub repo automatically (requires GitHub CLI and that you run `gh auth login` first):

```powershell
# authenticate first: gh auth login
gh repo create FussionPK/python-scripts --public --source=. --remote=origin --push
```

Notes
- Replace the remote URL with your actual repo URL if you choose a different name or owner.
- If `git push` prompts for credentials on Windows, use a GitHub PAT or sign-in via the Git credential manager.
- I included a `.gitignore` to ignore virtualenvs, caches and some generated text files.

If you want, I can continue and run the git commands from this session once `git` (and optionally `gh`) are available and you confirm the repo name and visibility (public/private).
=======
# python-scripts
Very Self Explanatory
>>>>>>> b99f17d8ca3aea902926313bff5fdb9363e11317
