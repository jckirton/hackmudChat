# hackmud Python Chat API

## Setup

First, as per usual: clone this repository to wherever you want to work. *You want to work in this folder, with the contents of the clone.*

If run `setup.sh` and have python installed, it should:

- Create a python venv called `.venv` in the workspace directory
- Install `requests` into the venv
- Run `setup.py` (input of `chat_pass` needed)
- Delete itself.

This should set everything up, including your chat token and user info, which will be stored in `config.json`.

When you need to update these, just run `setup.py` again.

## Usage

Make sure to have `import chat` at the beginning of every python file. This will give you the two functions; `chat.read` and `chat.send`. They both have documentation.

## Snippets

There is a file called `chatAPI.code-snippets`. If you prefer to not use the functions I have made and instead want just the raw API code, this file has snippets containing exactly that; just uncomment the contents.
