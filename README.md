# just_a_repo

- To run the app on a system having python3 and pip installed, follow the steps below:
    - Clone the repository
    - create a virtual environment using ```python3 -m venv venv```
    
    - Activate the virtual environment using ```source venv/bin/activate``` on linux or ```venv\Scripts\activate``` on windows
    - Install the required packages using ```pip install -r requirements.txt```
    - enter into the app directory using ```cd app```
    - Run the app using ```flask run```
    - you can see the additional commands available using ```flask --help```
    - in our case we have the following commands:
        - ```flask add_user```
        - ```flask update_user```
        - ```flask --help```