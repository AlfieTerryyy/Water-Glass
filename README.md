# Alfie Terry - Chat Room

A simple web-based chat room with username and key-based access. Styled for `alfieterry.co.uk`, this application allows you to host a chat server that can be accessed by anyone with the correct key.

## Prerequisites

Make sure you have the following installed on your system:

- Python 3.8 or later
- pip (Python package manager)
- A code editor (optional but recommended)

## Installation Guide

Follow these steps to set up the chat application:

### FULL - Install

```bash
git clone https://github.com/AlfieTerryyy/Water-Glass
cd Water-Glass

```
```bash
pipx install flask --force
```
```bash
# Install python3-venv if it's not installed
sudo apt install python3-venv

# Create a virtual environment in the current directory
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```
```bash
pip install -r requirements.txt

```
```bash
python app.py
```
```bash
hostname -I #Linux
ipconfig    #Windows
```
and copy the wlan0 and put :5000 on the end for the port
