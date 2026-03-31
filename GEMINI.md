# Project Context: MyPyro

## Overview

**MyPyro** is a custom fork of the **Pyrogram** library, a Telegram MTProto API client for Python. This fork is specialized with built-in support for localized error messages (Indonesian) and custom API/RPC error compilation. It is maintained and used as the core engine for custom Telegram clients.

## Core Features

*   **Custom RPC Error Compiler:** Generates Python error classes from `.tsv` source files.
*   **Localized Errors:** Pre-configured with Indonesian error messages for common RPC errors.
*   **Beta Branch:** The repository is optimized for the `@beta` branch.

## Project Structure

*   **`pyrogram/`**: The main library source code.
    *   `pyrogram/errors/`: Contains generated error classes.
    *   `pyrogram/raw/`: Contains generated MTProto raw types and functions.
*   **`compiler/`**: Tools to generate library code from MTProto schemas and TSV files.
    *   `compiler/errors/source/`: **CRITICAL**: Edit these `.tsv` files to change error messages (e.g., translate to Indonesian).
*   **`Makefile`**: Automation script for development tasks.

## Building and Compiling

To apply changes to error messages or MTProto schemas, you MUST run the compiler:

1.  **Edit Error Messages:**
    Modify the `.tsv` files in `compiler/errors/source/`.
    *Example:* `/root/mypyro/compiler/errors/source/400_BAD_REQUEST.tsv`

2.  **Run Compiler:**
    Use the `make api` command (requires a virtual environment):
    ```bash
    # Inside /root/mypyro
    make api
    ```
    This will execute:
    - `compiler/api/compiler.py` (Updates raw types)
    - `compiler/errors/compiler.py` (Updates exception classes)

3.  **Clean Builds:**
    ```bash
    make clean
    ```

## Development Conventions

*   **Python Version:** Optimized for Python 3.11+.
*   **Dependencies:** Managed via `requirements.txt` and `dev-requirements.txt`.
*   **Testing:** Uses `tox` for cross-version testing.

## Key Maintenance Commands

*   `make venv`: Creates a fresh virtual environment and installs all dev dependencies.
*   `make build`: Cleans and builds source distribution and wheels.
*   `make api`: Recompiles the entire MTProto API and Error system (Crucial after editing `.tsv` files).
