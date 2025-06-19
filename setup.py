from pathlib import Path
import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit-audio-cn",
    version="0.1.0",
    author="renhong",
    author_email="renh2@zju.edu.cn",
    description="Record audio from the user's microphone in apps that are deployed to the web via chinese.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/renH2/streamlit-audio-cn",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        "streamlit>=0.63",
    ],
)