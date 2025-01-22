from setuptools import setup, find_packages

setup(
    name="ChatBot_Studio",
    version="1.0.0",
    description="A framework to design, train, and deploy AI chatbots.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "transformers>=4.0",
        "torch>=1.7",
        "flask>=2.0",
        "python-telegram-bot",
        "slack_sdk",
        "twilio",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
