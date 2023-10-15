# git-cli-clone-python
A Python based Git clone that allows creating repos, commiting, and pushing.

## Installing packages
There is an included `requirements.txt` file containing the required modules for this project.

To install, use the following command:
```
$ python3 -m pip install -r requirements.txt
```
You should now have the following installed:
- virtualenv
- wheel
- setuptools
- twine
- click>=8.1.7

# Building the project
1. Create the virtual envirnment and activate it
- ```virtualenv venv```
- ```source venv/bin/activate```
2. Install the tool in the virtual environment
- ```python setup.py develop```
3. Verify with the hello command
- ```pygit hello -n Johnny```

# Available Commands
1. ```pygit hello -n {name}```
2. **in-progress** ```pygit init {new-repo-folder-name}```

## Python Version
Python 3.11.5