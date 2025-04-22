# WODE Kernel Builder

WODE is an automation tool that builds and packages custom Linux kernels with BBRv3 support.  
This project simplifies getting optimized kernels for developers and VPS users.

## Features
- Automated kernel compilation using GitHub Actions
- Built-in BBRv3 TCP congestion control
- Easy to customize for your distro

## Usage
1. Fork this repo
2. Edit `kernel-configs/` to match your system
3. Trigger GitHub Actions or push changes to build

## Output
Built `.deb` or `.tar.gz` packages will be available in the GitHub Actions artifacts section.
