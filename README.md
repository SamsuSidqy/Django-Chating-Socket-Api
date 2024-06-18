This is a Api [**Django**](https://www.djangoproject.com/) project,using [`@django-rest-framework`](https://www.django-rest-framework.org/).

# Getting Started

>**Note**: Make sure you have completed the [Chatting App React Native - Environment Setup](https://github.com/SamsuSidqy/Chatting-App-React-Native)step, 

## Step 1: Install Package

**"This Package"**
1. django
2. django-cors-headers 
3. django-oauth-toolkit
4. channels (For Package Channels, read the Channel installation documentation [Django Channels](https://channels.readthedocs.io/en/latest/installation.html))

First, you will need to start **Metro**, the JavaScript _bundler_ that ships _with_ React Native.

To start Metro, run the following command from the _root_ of your React Native project:

```bash
# Install Package
pip install <Name Package>

```

## Step 2: Start your Application

>**Note**: So that api and sockets or channels can run and be used on React Native. Do this, and access using your computer's IP, and make sure you are on the same network

```bash
python3 manage.py runserver 0.0.0.0:8000
```

### Run Localhost

```bash
python3 manage.py runserver
```


## Congratulations! :tada:

You've successfully run and Api your Django Rest Framework Website. :


# API Reference

#### Request Register

```http
  POST /api/register
```

| Body (JSON) | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username`| `string` | **Required**.|
| `password`| `string` | **Required**.|


----
#### Request Login

```http
  POST /api/login
```

| Body (JSON) | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**|
| `password`      | `string` | **Required**|



---

### Request Logout

```http
POST /api/logout
```

| Authroization | Description                       |
| :-------- | :-------------------------------- |
|`Bearer Token`| **Required**.|

| Body (json) | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`token`|`string`|**Bearer Token**|
---
### Request Checking Token [Benar Atau Tidak | Expired Atau Tidak]

```http
GET /api/checking
```
| Authroization | Description                       |
| :-------- | :-------------------------------- |
|`Bearer Token`| **Required**.|

| Body (json) | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`None`|`None`|**None**|

---
## Request Contact
```http
GET /contact/
```
| Authroization | Description                       |
| :-------- | :-------------------------------- |
|`Bearer Token`| **Required**.|

| Body (json) | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`None`|`None`|**None**|

---

## Request Room Chatting
```http
GET /room/
```

| Authroization | Description                       |
| :-------- | :-------------------------------- |
|`Bearer Token`| **Required**.|

| Body (json) | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`id-sender`|`integer`|**Id Dari Pengirim**|
|`id-recive`|`integer`|**Id Dari Penerima**|

---

## Connect To Websocket Chatting

```socket
Websocket /chat/:koderoom/
```


### Now what?

- [Integration Guide Django](https://www.djangoproject.com/).
- [Introduction to React Native](https://reactnative.dev/docs/getting-started).
- [Integration Guide Django Rest Framework](https://www.django-rest-framework.org/)

