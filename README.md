# paysafe
ROIIM Paysafe Assignment


### Step 1: Clone the repository
```git clone https://github.com/Riya5915/paysafe.git``` <br/>
```cd paysafe/```

### Step 2: Run the following commands to get started (make sure that python3 is installed on your computer/laptop)
```pip3 install virtualenv```  <br/>
```virtualenv -p python3 env``` <br/>
```source env/Scripts/activate``` <br/>
```cd paysafe/``` <br/>
```pip install -r requirements.txt```

### Step 3: Run the server
```python manage.py runserver```

### Step 4: Start the app
Open a browser such as Chrome/Microsoft Edge/Firefox and make sure that the CORS (Cross-Origin Resource Sharing) is enabled in your browser
In a new tab type the given url and press enter: ```http://localhost:8000/payments```

### Step 5: Use the app
Fill the given form with the given details or you can enter your own.
If you are a new user you will be registered and then will be redirected to the next page.
If you are an old user you will be logged in and then redirected to the checkouts page.

Enter the message you want to give and then press "Pay Now" button to proceed.
Then in the popup enter the card details and press "Withdraw" button.

#### Note: 
Make sure you do not use your real card details rather enter the dummy card details from the below link:
https://developer.paysafe.com/en/rest-apis/cards/test-and-go-live/test-cards/
