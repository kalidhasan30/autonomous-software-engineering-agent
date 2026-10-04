import shutil
from pathlib import Path
from urllib.parse import urlparse

from git import Repo


CLONE_DIRECTORY = Path("cloned_repositories")


def repository_name_from_url(url):
    parsed = urlparse(url)

    name = Path(parsed.path).name

    if name.endswith(".git"):
        name = name[:-4]

    return name


def clone_repository(url):

    if not url.startswith(("https://github.com/", "http://github.com/")):
        raise ValueError("Please provide a GitHub repository URL.")

    name = repository_name_from_url(url)

    if not name:
        raise ValueError("Could not determine repository name.")

    destination = CLONE_DIRECTORY / name

    if destination.exists():
        print(f"\nRepository already exists: {destination}")

        answer = input("Delete and clone again? (y/n): ").strip().lower()

        if answer == "y":
            shutil.rmtree(destination)
        else:
            return destination

    CLONE_DIRECTORY.mkdir(exist_ok=True)

    print(f"\nCloning repository...")
    print(f"URL: {url}")

    Repo.clone_from(
        url,
        destination
    )

    print(f"\nRepository cloned to:")
    print(destination)

    return destination


if __name__ == "__main__":

    url = input("Enter GitHub repository URL: ").strip()

    try:
        path = clone_repository(url)

        print(f"\nReady for analysis: {path}")

    except Exception as error:
        print(f"\nClone failed: {error}")