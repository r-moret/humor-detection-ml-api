from setuptools import setup

setup(
    name="local_app",
    version="0.1",
    packages=['app', 'app.api', 'app.schemas', "app.api.endpoints"]
)