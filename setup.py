from setuptools import setup


def parse_reqs(req_path='./requirements.txt'):
    """Recursively parse requirements from nested pip files."""
    install_requires = []
    with open(req_path, 'r') as handle:
        # remove comments and empty lines
        lines = (line.strip() for line in handle
                 if line.strip() and not line.startswith('#'))
        for line in lines:
            # check for nested requirements files
            if line.startswith('-r'):
                # recursively call this function
                install_requires += parse_reqs(req_path=line[3:])
            else:
                # add the line as a new requirement
                install_requires.append(line)
    return install_requires


with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name='kill-team-cli',
    version='0.0.1',
    author='Barry Stokman',
    install_requires=parse_reqs(),
    description="Kill Team CLI housekeeping app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/barrystokman/kill-team-cli",
    entry_points={'console_scripts': ['kt=cli.base:cli']},
)
