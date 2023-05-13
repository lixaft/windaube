from __future__ import annotations

import os
import shutil
import subprocess
from typing import NamedTuple


def _func_factory(start_path):
    def _inner(path):
        return os.path.abspath(
            os.path.expanduser(os.path.join(start_path, path))
        )
    return _inner


home_dir = _func_factory("~")
dot_dir = _func_factory("~/dotfiles")


class Symlink(NamedTuple):
    src: str
    dst: str


class Repo(NamedTuple):
    url: str
    dst: str


FILES: list[Symlink] = [
    Symlink(
        dot_dir("nvim/.config/nvim"),
        home_dir("AppData/Local/nvim"),
    ),
    Symlink(
        dot_dir("starship/.config/starship.toml"),
        home_dir(".config/starship.toml"),
    ),
]

CLONES: list[Repo] = [
    Repo(
        "https://github.com/folke/lazy.nvim",
        home_dir("AppData/Local/nvim-data/lazy/lazy.nvim"),
    ),
]


def _remove(path: str) -> None:
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)


def _copy(src: str, dst: str) -> None:
    if os.path.isdir(src):
        shutil.copytree(src, dst)
    else:
        shutil.copyfile(src, dst)


def main() -> int:
    for repo in CLONES:
        if not os.path.exists(repo.dst):
            subprocess.check_call(("git", "clone", repo.url, repo.dst))

    for file in FILES:
        if os.path.exists(file.dst):
            _remove(file.dst)
        _copy(file.src, file.dst)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
