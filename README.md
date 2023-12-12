## Streamlit Authenticator Mongo

**A secure authentication module to validate user credentials stored in a Mongo database in a Streamlit application.**


## Installation

Streamlit-Authenticator is distributed via [PyPI](https://pypi.org/project/streamlit-authenticator/):

```python
pip install streamlit-authenticator-mongo
```

## Example

Using Streamlit-Authenticator_mongo is as simple as importing the module and calling it to verify your predefined users' credentials.

```python
import streamlit as st
import streamlit_authenticator_mongo as stauth
```

### 1. Hashing passwords

* Initially create a YAML configuration file and enter a name, random key, and number of days to expiry for a JWT cookie that will be stored on the client's browser to enable passwordless reauthentication. If you do not require reauthentication, you may set the number of days to expiry to 0. 

```python
cookie:
  expiry_days: 30
  key: some_signature_key # Must be string
  name: some_cookie_name

```

* Then Initalize a mondodb client and get the collection using the Mongo Client API.


```python
    client = MongoClient(uri)
    db = client["database"]
    collection = db["collection"]
```



### 2. Creating a login widget

* Subsequently import the configuration file and the collection object into your script and create an authentication object.

```python
import yaml
from yaml.loader import SafeLoader
from dbscript import collection

with open('../config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    collection,
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],

)
```
* Ensure the schema for the database documents has the following fields

db['username'], db['password'], db['email'], db['name']


* Then finally render the login module as follows. Here you will need to provide a name for the login form, and specify where the form should be located i.e. main body or sidebar (will default to main body).

```python
authenticator.login('Login', 'main')
```
![](https://github.com/mkhorasani/Streamlit-Authenticator/blob/main/graphics/login_form.PNG)

### 3. Authenticating users

* You can then retrieve the name, authentication status, and username from Streamlit's session state using **st.session_state["name"]**, **st.session_state["authentication_status"]**, and **st.session_state["username"]** to allow a verified user to proceed to any restricted content.
* In addition, you may include an optional logout button at any location on your main body or sidebar (will default to main body). The optional **key** parameter for the logout widget should be used with multipage applications to prevent Streamlit from throwing duplicate key errors.

```python
if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
```

![](https://github.com/mkhorasani/Streamlit-Authenticator/blob/main/graphics/logged_in.PNG)

* Or prompt an unverified user to enter a correct username and password.

![](https://github.com/mkhorasani/Streamlit-Authenticator/blob/main/graphics/incorrect_login.PNG)

* Please note that logging out will revert the authentication status to **None** and will delete the associated reauthentication cookie as well.

### 4. Creating a password reset widget

* You may use the **reset_password** widget to allow a logged in user to modify their password as shown below.

```python
if st.session_state["authentication_status"]:
    try:
        if authenticator.reset_password(st.session_state["username"], 'Reset password'):
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)
```

![](https://github.com/mkhorasani/Streamlit-Authenticator/blob/main/graphics/reset_password.PNG)

_Please remember to update the config file (as shown in step 9) after you use this widget._

### 5. Creating a new user registration widget

* You may use the **register_user** widget to allow to allow anyone to sign up. After a successful validation, the new user entry is added to the database. The user can then go an login with the new account

```python
try:
    if authenticator.register_user('Register user'):
        st.success('User registered successfully')
except Exception as e:
    st.error(e)
```

![](https://github.com/mkhorasani/Streamlit-Authenticato-mongor/blob/main/graphics/register_user.PNG)

_Please remember to update the config file (as shown in step 9) after you use this widget._

### 6. Creating a forgot password widget

* You may use the **forgot_password** widget to allow a user to generate a new random password. This password will be automatically hashed and saved in the configuration file. The widget will return the username, email, and new random password of the user which should then be transferred to them securely.

```python
try:
    username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password('Forgot password')
    if username_of_forgotten_password:
        st.success('New password to be sent securely')
        # Random password should be transferred to user securely
    else:
        st.error('Username not found')
except Exception as e:
    st.error(e)
```

![](https://github.com/mkhorasani/Streamlit-Authenticator/blob/main/graphics/forgot_password.PNG)

_Please remember to update the config file (as shown in step 9) after you use this widget._

### 7. Creating a forgot username widget

* You may use the **forgot_username** widget to allow a user to retrieve their forgotten username. The widget will return the username and email of the user which should then be transferred to them securely.

```python
try:
    username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username('Forgot username')
    if username_of_forgotten_username:
        st.success('Username to be sent securely')
        # Username should be transferred to user securely
    else:
        st.error('Email not found')
except Exception as e:
    st.error(e)
```

![](https://github.com/mkhorasani/Streamlit-Authenticator/blob/main/graphics/forgot_username.PNG)


## Credits
- Mohamed Abdou for the highly versatile cookie manager in [Extra-Streamlit-Components](https://github.com/Mohamed-512/Extra-Streamlit-Components).
- Mohammad Khorasani for providing the springboard and Inspiration from https://github.com/mkhorasani/Streamlit-Authenticator
