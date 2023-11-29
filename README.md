# Simple Python Playwright boilerplate

## Tech Stack
1. Pytest
2. Playwright

## Execution 
Requirements:
```
python 3.12.0
```

To run tests you need to perform the following commands:
```commandline
    pip install venv
    python -m venv venv
    ./venv/Scripts/activate
    pip install requirements.txt
    playwright install
    pytest --headed --browser-channel chrome --numprocesses auto
```
Explanation:
```
--headed - run browser with UI visible while test execution (DEBUG ONLY)
--browser-channer chrome - will execute tests using Google Chrome
--numprocessses auto - will execute tests in parallel mode with count of workers which matches your CPU core counts 
```