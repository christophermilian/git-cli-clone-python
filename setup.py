"""Module to help in tool packaging"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
    setup(
    name = 'python_git_clone',
    version = '0.0.1',
    author = 'Christopher Milian',
    author_email = 'christophermilian16@gmail.com',
    license = 'MIT License',
    description = 'Python based Git clone allowing one to create repos, commit, and push.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/christophermilian/git-cli-clone-python',
    py_modules = ['git_clone', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.11',
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        pygit=git_clone:cli
    '''
)
