# react-origames
METU Orienteering Team Fantasy Orienteering League Game

## Requirements:
* pyenv
* pipenv

### Install pipenv

```bash
$ pip install --user pipenv
```

if

```bash 
$ pipenv
zsh: command not found: pipenv
```
add this to your .zshrc or update it accordingly.

```bash
path+=("$HOME/.local/bin")
export PATH
```

to enter virtualenv
```bash
$ pipenv shell
```

to exit
```bash
$ exit
```

you might run ```deactivate``` accidentally
this might mess up pipenv. in that case:

```bash
$ pipenv --venv
```
to see venv directory and delete it
then you can start a new virtualenv again

## Install pyenv

```bash
$ brew update
$ brew install pyenv
```
this projects will be using python 3.10.4 so

```bash
$ pyenv install 3.10.4
$ pyenv global 3.10.4
```
of course you don't need to switch python version globally. from pyenv docs:

> To select a Pyenv-installed Python as the version to use, run one of the following commands:
>
> pyenv shell [version] -- select just for current shell session
>
> pyenv local [version] -- automatically select whenever you are in the current directory (or its subdirectories)
>
> pyenv global [version] -- select globally for your user account


### Development

```bash
$ pyenv install 3.10.4
$ pyenv global 3.10.4
$ pipenv shell
$ python3 manage.py runserver
```