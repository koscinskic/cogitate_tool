""" Collects commit data for a single user. """
from pydriller import RepositoryMining

import pprint


def collect_commits():
    # TODO: edit the method to take in the URL for the repo
    """ Creates a dictionary of commit objects for a single user. """
    # holds email of repo members as keys, contents of commit object as values
    author_dict = {}

    # indicate path for repository by pluggin in the URL of repo (must be public)
    repo_path = "https://github.com/GatorCogitate/cogitate_tool"

    # loop to turn the each Commits object into the values of the dictionary `author_dict`
    for commit in RepositoryMining(repo_path).traverse_commits():
        if commit.author.email not in author_dict.keys():
            author_dict[commit.author.email] = [commit]
        else:
            author_dict[commit.author.email].append(commit)
    return author_dict