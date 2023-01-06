from setuptools import setup, find_packages

# list dependencies from file
with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name="claim_chowder",
      description="testing claims",
      packages=find_packages(), # find packages automatically
      install_requires=requirements)
