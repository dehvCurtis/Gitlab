#!/usr/bin/env python3

import gitlab
import os # used to pull GL token from local env var

GITLAB_TOKEN = os.environ['GITLAB_TOKEN']

gl = gitlab.Gitlab('https://gitlab.<url>.net', GITLAB_TOKEN)

project_list = []

# Gather repo stats

for project in gl.projects.list(get_all=True, statistics=True):
    project_list.append((project.statistics))

# Gather repo sizes (kilbytes)
size_list = []

for size in project_list:
    kb_size = size["storage_size"] / 1000
    # print(f"{kb_size}KB")
    size_list.append(kb_size)
    size_list.sort()

# Print repo sizes (kilobytes)
repo_sizes_title = "List of Repo Sizes"
print(repo_sizes_title)
print("-" * len(repo_sizes_title))

for i in size_list:
    print(f"{i}KB")
print("\n")

# Calculate & print repo size average & sum (kilobytes)
sum_numbers = sum(size_list)
size_list_len = len(size_list)
avg_kb = sum_numbers / size_list_len
print(f"Average Repo Size: {avg_kb}KB")
print(f"Sum Repo Size: {sum_numbers}KB\n")