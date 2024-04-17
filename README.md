# Restaurant Management System
<p align="center">
  <img src="https://github.com/devjefersonsantos/restaurant-management-system/assets/155383680/30ff08ff-ada5-4727-a7c2-6c3813610c4c">
</p>

![image](https://github.com/devjefersonsantos/restaurant-management-system/assets/155383680/0d4bcdb8-07ad-4bb2-ab08-b38426a966f0)

## Requirements
- Python 3.10+
- MySQL Server 8.0+
  - MySQL Workbench 8.0+
- Git Bash
- Screen resolution set at a minimum of 1920×1080
- Windows 10+

## Attention
The program automatically creates the database.

```python
# Connection parameters are exposed
{
    "host": "localhost",
    "user": "root",
    "password": ""
}
```

## Installation
Clone the repository using the git bash command line:

```
$ cd Desktop ; git clone https://github.com/devjefersonsantos/restaurant-management-system.git
```
Run the command to install the dependencies:
```
$ cd Desktop ; cd restaurant-management-system ; pip install -r requirements.txt
```
It is recommended to use a virtual environment when working with third party packages.

## Usage
Run the following command line to launch the main file:
```
$ python main.py
```
or to browse directories and launch the main file:
```
$ cd Desktop ; cd restaurant-management-system ; python main.py
```
## Data Simulation
`restaurant-management-system/tests/test_simulation.py`

```py
if __name__ == "__main__":
    while True:
        question = input("Are you sure you want to insert fictional data into the database? [Y/N] ")
        if question.upper() == "Y":
            try:
                simulation()
            except Exception as error:
                print(error)
            else:
                print("Data entered successfully.")
                
                logging.basicConfig(
                    level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s",
                    filename="log/log.log"
                )
                logging.warning('Fictitious data was added to the database by test file "test_simulation.py"')
            break
        elif question.upper() == "N":
            break
```
# ui-fertigation-python
