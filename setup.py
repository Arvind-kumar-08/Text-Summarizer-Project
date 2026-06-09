import setuptools

with open("README.md","r",encoding="utf-8") as f:
          long_description=f.read()

__version__="0.0.0"

REPO_NAME="Text-Summarizer-Project"
AUTHOR_USER_NAME="Arvind-kumar-08"
SRC_REPO="Text-Summarizer-Project"
AUTHOR_EMAIL="ak217127@gmail.com"

setuptools.setup(
        name=SRC_REPO,
        version=__version__,
        author=AUTHOR_USER_NAME,
        AUTHOR_EMAIL=AUTHOR_EMAIL,
        description="Small NLP project"

)

          