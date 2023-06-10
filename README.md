# SUA - Small Unmanned Aircraft (Beard & McLain)

---

![Travis (.com)](https://img.shields.io/travis/com/io-aero/sua.svg?branch=master)
![GitHub release](https://img.shields.io/github/release/io-aero/sua.svg)
![GitHub Release Date](https://img.shields.io/github/release-date/io-aero/sua.svg)
![GitHub commits since latest release](https://img.shields.io/github/commits-since/io-aero/sua/1.0.0.svg)

---

A flight simulator for an unmanned aircraft (UA) based on the book [Small Unmanned Aircraft](https://github.com/randybeard/uavbook) by Beard and McLain done in Python and Rust.

## Directory and File Structure of this Repository

### 1. Directories

| Directory         | Content                                                    |
|-------------------|------------------------------------------------------------|
| .github/workflows | **[GitHub Action](https://github.com/actions)** workflows. |
| data              | Application data related files.                            |
| dist              | Installable versions of the **SUA** application.           |
| docs              | Documentation files.                                       |
| resources         | Selected manuals and software.                             |
| scripts           | Scripts supporting Ubuntu and Windows.                     |
| src               | Python script files.                                       |
| tests             | Scripts and data for **pytest**.                           |

### 2. Files

| File              | Functionality                                               |
|-------------------|-------------------------------------------------------------|
| .gitignore        | Configuration of files and folders to be ignored.           |
| .pylintrc         | **pylint** configuration file.                              |
| LICENSE.md        | Text of the licence terms.                                  |
| logging_cfg.yaml  | Configuration of the Logger functionality.                  |
| Makefile          | Tasks to be executed with the **`make`** command.           |
| Pipfile           | Definition of the Python package requirements.              |
| Pipfile.lock      | Definition of the specific versions of the Python packages. |
| pyproject.toml    | Optional configuration data for the software quality tools. |
| README.md         | This file.                                                  |
| run_sua_dev       | Main script for using the functionality of **SUA**.         |
| settings.sua.toml | Configuration data.                                         |
| setup.cfg         | Optional configuration data for **flake8**.                 |

## Documentation

The documentation can be found [here.](https://io-aero.github.io/sua/index.html)

