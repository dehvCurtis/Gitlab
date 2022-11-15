#!/usr/bin/env python3

import gitlab
import os # used to pull GL token from local env var
from contextlib import redirect_stdout # used to write groups to file

# add GitLab token (local env var) to var
GITLAB_TOKEN = os.environ['GITLAB_TOKEN']

# authenticate to gitlab instance
gl = gitlab.Gitlab('https://gitlab.datto.net', GITLAB_TOKEN)

group_ids = []

# Add group / subgroup IDs to group_ids[]
for group in gl.groups.list(get_all=True, include_subgroups=True):
    group_ids.append((group.id))

group_ids.sort()

# create `config.yml` file and write group_ids[] to file
with open('config.yml', 'w') as file:
    with redirect_stdout(file):
        print('groups:')
        for id in group_ids:
            print(f'  - {id}')

file.close()
