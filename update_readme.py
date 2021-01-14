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


def query_repository_stats(full_repo):
    query_url = f"https://api.github.com/repos/{full_repo}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(query_url, headers=headers)
    r.raise_for_status()
    return r.json()


def get_metadata():
    return {
        "now": datetime.datetime.utcnow(),
        "self_url": SELF_URL,
    }


if __name__ == "__main__":
    with open(INPUT_FILE, "r") as f:
        input_data = json.load(f)

    with open(TEMPLATE_FILE, "r") as f:
        template = Template(f.read())

    out = template.render(
        input_data=input_data,
        meta=get_metadata(),
        get_stats=query_repository_stats,
    )

    with open(OUT_FILE, "w") as f:
        f.write(out)