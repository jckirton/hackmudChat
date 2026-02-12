# hackmud Python Chat API

## ARCHIVAL NOTICE

***This reposity is no longer the place where this is being worked on.***

I am now developing this as a Python module published on PyPi, with the source code avaliable at [jckirton/hackmudChatBackage](https://github.com/jckirton/hackmudChatPackage).

This repository will not be deleted for archival reasons, but it will not recieve new features from me.

If you are using this currently, you can change to the new version by installing it to your venv with `pip install hackmudChatAPI`, and changing all your `from chat import ChatAPI` to `from hackmudChatAPI import ChatAPI`.

It should be fully backwards compatible with the *class based* implementation present here (i.e., old configs are accepted and will be updated, methods take the same arguments and behave largely the same).

It is ***NOT*** backwards compatible with the function based implementation (importing/using the fuctions directly).

## Setup

First, as per usual: clone this repository to wherever you want to work. *You want to work in this folder, with the contents of the repository.*

If you run `setup.sh` and have python installed, it should:

- Create a python venv called `.venv` in the workspace directory
- Install `requests` into the venv
- Run `setup.py` (input of `chat_pass` needed)
- Delete itself.

This should set everything up, including your chat token and user info, which will be stored in `config.json`.

When you need to update these, just run `setup.py` again.

## Usage

Make sure to have `from chat import ChatAPI` at the beginning of every python file. This will give you the `ChatAPI` class, which you want to make an instance of.

## Snippets

There is a file called `chatAPI.code-snippets`. If you prefer to not use the functions I have made and instead want just the raw API code, this file has snippets containing exactly that; just uncomment the contents.
