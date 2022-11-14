#!/usr/bin/env python3

import gitlab
import os # used to pull GL token from local env var

GITLAB_TOKEN = os.environ['GITLAB_TOKEN']

gl = gitlab.Gitlab('https://gitlab.datto.net', GITLAB_TOKEN)

# List all projects
# projects = gl.projects.list(get_all=True)
# print(projects)

# GROUPS

# # List Groups
# groups = gl.groups.list(get_all=True)
# print(groups)

# # List Groups and Subgroups
# groups_subgroups = gl.groups.list(get_all=True,include_subgroups=True)
# print(groups_subgroups)

# # List Group and Subgroup IDs
group_ids = []
for group in gl.groups.list(get_all=True,include_subgroups=True):
    group_ids.append((group.id))

group_ids.sort()
for id in group_ids:
    print(id)
