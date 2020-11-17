# django-crud-dynamic-tables-forms-and-urls

This is python development environment.
In order to run and test please follow.

## Python Environment Setup
Please make sure you have `python3`, and `pip` installed.

**MacOs**
```bash
brew install python3

brew install python3-pip 
# or
brew install python-pip
```

**Linux**
```bash
sudo apt-get update install python3
sudo apt-get install python3

sudo apt-get install python3-pip
# or
sudo apt-get install python-pip
```

## Confirm installation

```bash
python3 --version
pip --version
```

if you already have installed please skip above steps.

1. Create Virtual environment and install requirements by 
```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
2. Run development server 
`python3 manage.py runserver`

3. Visit http://127.0.0.1:8000
