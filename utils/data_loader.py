# utils/data_loader.py
# Handles all reading and lookup of project data from the JSON file.

import json
import os

# Build the path to projects.json relative to this file's location
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "projects.json")

# In-memory cache for projects data to avoid repeated disk reads.
# Trade-off: faster subsequent accesses vs. slightly higher memory usage.
# Cache is invalidated via clear_cache() in tests to ensure test isolation.
_projects_cache = None


def load_all_projects():
    """Read and return the full list of projects from the JSON file.

    Uses a module-level cache to avoid repeated disk reads after the first call.
    Call clear_cache() to reset the cached data (used primarily in tests).
    """
    global _projects_cache
    if _projects_cache is None:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            _projects_cache = json.load(f)
    return _projects_cache


def clear_cache():
    """Clear the in-memory projects cache.

    Use this in test setup to ensure test isolation when the underlying
    data file may change between test runs.
    """
    global _projects_cache
    _projects_cache = None


def find_project_by_id(project_id):
    """
    Return the project dict whose 'id' matches the given integer.
    Returns None if no match is found.
    """
    for project in load_all_projects():
        if project.get("id") == project_id:
            return project
    return None
