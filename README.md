# pythontest

Toggle Line Comment:
This method adds a single-line comment character (like // or #) to the beginning of each selected line. 
Using the same shortcut again will uncomment the lines. 

Windows/Linux: Ctrl + /

Windows/Linux: Ctrl + /

macOS: Command + /


Toggle Block Comment :
This method wraps the entire selected block of code within a single block comment syntax (like /* ... */ for CSS/HTML or docstrings in Python, depending on the language and settings). 
Using the shortcut again removes the block comment.

Windows: Shift + Alt + A

macOS: Shift + Option + A

Linux: Ctrl + Shift + A.


Git lock error happens when Git thinks another Git process is still running. Usually it happens if a previous command stopped suddenly in GitHub Codespaces, leaving a lock file.

The fix is simple.

1️⃣ Remove the lock file

Run this command:

rm -f .git/index.lock

This deletes the stuck lock file.

2️⃣ Add the files again

git add .

3️⃣ Commit the files

git commit -m "Added new project files"

4️⃣ Push to repository

git push origin main
