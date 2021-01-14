#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import datetime

import requests
from jinja2 import Template

SELF_URL = f'{os.environ["GITHUB_SERVER_URL"]}/{os.environ["GITHUB_REPOSITORY"]}'
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

INPUT_FILE = "repos.json"
TEMPLATE_FILE = "template.md"
OUT_FILE = "README.md"


def query_repository_stats(owner, repo):
    query_url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(query_url, headers=headers)
    return r.json()


def get_metadata():
    return {
        "time": datetime.datetime.now(),
        "self_url": SELF_URL,
    }


if __name__ == "__main__":
    with open(INPUT_FILE, "r") as f:
        input_data = json.load(f)

    section_stats = {}
    for section in input_data["sections"]:
        repo_stats = {}

        for repo in section["repos"]:
            owner, repo_name = repo.split("/")
            repo_stats[repo] = query_repository_stats(owner, repo_name)
            
        section_stats[section["title"]] = repo_stats

    with open(TEMPLATE_FILE, "r") as f:
        template = Template(f.read())

    out = template.render(
        sections=section_stats,
        meta=get_metadata()
    )

    with open(OUT_FILE, "w") as f:
        f.write(out)