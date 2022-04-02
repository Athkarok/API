# User

The API uses tokens to authenticate and authorize users.
<br><br>
Token ex:

```eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJyb2xlIjoiVVNFUiIsImV4cCI6MTY1NjU5MDAwOH0.TlWSze-cgundyG-USrA9Sf5xjqu5FxAltrTq03iyRJQ``` 

## Signing

### Sgin with Google

`api.athkarok.tech/v1/user/sign_google` **`POST`**

#### body:

```json
{
  "google_id_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiMDAwMDAwMDAwMDAwMC0wMFgwWDAwWFhYWDAwMFhYWDAwWDAwWDAwWDBYMFguYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIwMDAwMDAwMDAwMDAwLTAwWDBYMDBYWFhYMDAwWFhYMDBYMDBYMDBYMFgwWC5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjAwMDAwMDAwMDAwMDAwMDAwMDAwMDAiLCJlbWFpbCI6InVzZXJAZG9tYWluLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoiMDAwWFgwMFhYMDBYMFhYWDAwMFhYMCIsIm5hbWUiOiJKb2huIERvZSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQU9oMTRHalBkN0ZZalRvSHYtZmd4ZDdkNm5sWkZmeUtDb2dBaGhQZ3A0VXNZTG89czk2LWMiLCJnaXZlbl9uYW1lIjoiSm9obiIsImZhbWlseV9uYW1lIjoiRG9lIiwibG9jYWxlIjoiZW4iLCJpYXQiOjE2NDc2NTczODUsImV4cCI6MTY0NzY2MDk4NSwianRpIjoiMDBYWDAwMFhYWDBYMDBYWFgwMDBYWFhYMDAwWFhYWDAwMFgwWFhYWFhYWCJ9.QTkU3YGiQZvwq7Sb_ZNpnpr3WygFs6QLK4ZdcD-W9dI"
}
```

#### Success Response:

code : **`200`**

```Json
{
    "success": "User successfully signed.",
    "token": "TOKEN"
}
```

#### Error Response:

code : **`403`**

```Json
{
    "error": "Invaild Google Token."
}
```

### Register

`api.athkarok.tech/v1/user/register` **`POST`**

#### body:

```json
{
  "email": "name@domain.com",
  "username": "username",
  "password": "XXXXXXX",
  "fname": "Ahmed",
  "lname": "Mohamed",
  "phone_number": "+201000000000"
}
```

#### Success Response:

code : **`201`**

```Json
{
    "code": 0,
    "token": "TOKEN"
}
```

#### Error Responses:

code : **`400`**

```Json
{
    "error": "Invalid Email."
}
```

```Json
{
    "error": "Invalid Username."
}
```

```Json
{
    "error": "Invalid Password."
}
```

code : **`409`**

```Json
{
    "code": 1,
    "error": "User already exists."
}
```

```Json
{
    "code": 2,
    "error": "Username is used."
}
```

```Json
{
    "code": 3,
    "error": "Phone number is used."
}
```

### Login

`api.athkarok.tech/v1/user/login` **`POST`**

#### body:

```json
{
    "handle" : "Username Or Email",
    "password": "XXXXXXXXX"
}
```

#### Success Response:

code : **`200`**

```Json
{
    "code": 0,
    "token": "TOKEN"
}
```

```Json
{
    "code": 1,
    "error": "Handle or Password is incorrect, try again or create a new account."
}
```


## User Data

### @me

`api.athkarok.tech/v1/user/@me` **`GET`**

#### header:

```json
{
    "Authorization": "Bearer TOKEN"
}
```

#### Success Response:

code : **`200`**

```Json
{
    "code": 0,
        "full_name": "Ahmed Mohamed",
        "points": 0,
        "settings": {
            "theem": "auto",
            "font_type": "Questv1",
            "font_size": "m",
        },
        "progress": {
            "wheel": true,
            "group_ids": [1, 5, 3]
        }
}
```

#### Error Response:

code : **`401`**

```Json
{
    "error": "Token is invalid"
}
```

## Update User Settings

`api.athkarok.tech/v1/user/settings` **`POST`**

#### header:

```json
{
    "Authorization": "Bearer TOKEN"
}
```

#### body:

Provide a valid id or null

```Json
{
    "font_type": 1,
    "font_size": 4,
    "disply_theem": 1
}
```

#### Success Response:

code : **`200`**

```Json
{
    "success": "Settings updated."
}
```

#### Error Response:

code : **`401`**

```Json
{
    "error": "Token is invalid"
}
```