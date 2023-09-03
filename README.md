# project-launcher

## What it is:
- This is a simple CLI app that I came up with that would help me learn python and do something useful as well
- It creates new projects in a language selected from a menu and structures that project for you

## What it does:
- This will start a new project folder and main file for **Python** and **Go**</b>
- This will create a new **React/JS** or **React/TS** app using vite and npm

## Dependencies
In its current state requires:
- **Python3** (included with most OSes except for windows)
- **pip** (package manager to install python script dependencies)
- **typer** (pip)
- **rich** (pip)
- **Node.js/NPM** (only for React/JS and React/TS functionality)
- **Golang** (only for Go project creation)

## It is fully functional except:
- The intent was to have 'npm install' run in the React JS/TS project directories but it is currently not functioning
- The above can be remedied by `cd`-ing to the project directory and running the command `npm i`

## In the future I would like to:
- Create a GUI version of this app
- Add more languages
