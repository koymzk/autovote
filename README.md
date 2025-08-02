# autovote

This project automates voting on https://vote.miscolle.com using Playwright and Docker.

## Features
- Automates button clicks on a target web page
- Supports authentication via localStorage
- Runs in a Docker container for easy setup

## Requirements
- Docker
- Docker Compose

## Usage
1. Clone this repository
2. Build the Docker image:
   ```bash
   docker compose build
   ```
3. Run the automation:
   ```bash
   docker compose up
   ```

## Configuration
- Edit `main.py` to set:
  - `TARGET_URL`: The page to automate
  - `BUTTON_SELECTOR`: CSS selector for the button to click
  - `LOCALSTORAGE_ITEMS`: List of localStorage keys/values for authentication

## Notes
- For debugging, set `headless=False` in `main.py` to see the browser window (requires GUI environment)

## License
MIT
