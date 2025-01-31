from setuptools import setup, find_packages

setup(
    name="ChatBot_Studio",
    version="1.0.1",
    description="A framework to design, train, and deploy AI chatbots.",
    author="Gopalakrishnan Arjunan",
    author_email='gopalakrishnana02@gmail.com',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url='https://github.com/gopalakrishnanarjun/ChatBot_Studio',  # Update with your GitHub repository URL
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
