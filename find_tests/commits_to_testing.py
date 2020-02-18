# Class Roster: Caden Hinckley, Devin Spitalny, Tyler Pham, Cory Wiard,
# Jordan Wilson, Anthony Baldeosingh, Caden Koscinski, Christopher Stephenson
# Danny Reid, Jordan Byrne, Madelyn Kapfhammer, Megan Munzek, Pedro Carmo,
# Hannah Schultz, Xingbang Liu, Devin Ho, Spencer Huang, Christian Lussier,
# Jacob Stringer, Marisol Santa Cruz, Thomas Cassidy, Wonjoon Cho,
# Teona Bagashvili, Claire Johns, Collin McNulty

from datetime import datetime
from pydriller import RepositoryMining, GitRepository

user_repo = input("Enter the link to your chosen GitHub repository: ")

# accesses users
commit_author_list = []
# accesses github repo to calculate users commits
for commit in RepositoryMining(
    user_repo
).traverse_commits():
    if commit.author.name not in commit_author_list:
        commit_author_list.append(commit.author.name)
        print("Adding author,", commit.author.name)
    else:
        pass


print()
# Calculates the total commits like author, test and general and connecting
# to the chosen repo
for author_name in commit_author_list:
    author_commit_count = 0
    total_commit_count = 0
    total_test_commit_count = 0
    for commit in RepositoryMining(
        "https://github.com/lussierc/simplePerformanceExperimentsJava"
    ).traverse_commits():
        count = 0
        # Connects the author name to the amount of commits made by user the
        # clear path to the repo
        if commit.author.name in author_name:
            author_commit_count = author_commit_count + 1
            for modified_file in commit.modifications:
                file_path = modified_file.new_path
                if count is 0:
                    if file_path:
                        if "test" in file_path:
                            print(
                                "Found someone who modified tests in file: ",
                                # will calculate the modifications to the test
                                commit.author.name,
                                file_path,
                                commit.hash,
                            )
                            total_test_commit_count += 1
                            count = 1
                        else:
                            pass
        if commit.author.name in commit_author_list:
            total_commit_count = total_commit_count + 1
    # Print statements that release the calculations of the declared variables
    print(author_name, "'s Total commits: ", author_commit_count)
    print("-- Testing commits by", author_name, ":", total_test_commit_count)
    percentage_covered = (total_test_commit_count / author_commit_count) * 100
    print("-- Percentage of Commits Going to Testing:", percentage_covered, "%")
    print("\n\n")

print()
print("Total commits in repository: ", total_commit_count)