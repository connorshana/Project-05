# Project-05
  1.**Create** and **activate** the project virtual environment.  Start in GitHub and create a new repository.
  Add a README.md file.
 
  2. Open VS Code terminal.

  2. Install all required packages into your local project virtual environment.

  3. After installing the required dependencies, update or generate a  **requirements.txt** file.
  
  4. Add a **.gitignore** file to your project with useful entries. See [.gitignore](.gitignore) example.  Add .venv/ and .vscode/ to the .gitignore.
  5. Document the steps and commands in your README.md.

  Terminal Commands:
  ```Powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  py -m pip freeze > requirements.txt
  ```

  ## Install pandas

  ```Powershell
  pip install pandas
  ```

  ## Freeze requirements
  ```Powershell
  py -m pip freeze > requirements.txt
  ```

## Push to GitHub

```Powershell
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/project-05.git
git push -u origin main
```

