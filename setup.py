import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME="Text-Summarizer"
AUTHOR_USER_NAME="akash-narayanaswamy-g"
SRC_REPO ="textSummarizer"
AUTHOR_EMAIL="akashnarayanaswamy.ng@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=" A small python package for nlp app",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/"+AUTHOR_USER_NAME+"/"+SRC_REPO,
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
)