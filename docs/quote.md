# Quote

This route allows Retrieving quotes, Adding, or getting a random quote everyday.

## Get quotes

This route retrieve all quotes. 

`api.athkarok.tech/v1/quote` **`GET`**

### Response:

code : **`200`**

```Json
{
    "quotes": 
    [
        {
            "id": 1,
            "text": "لا يعجبكم من الرجل طنطنته، ولكن من أدى الأمانة وكف عن أعراض الناس، فهو الرجل.",
            "author": "Omar Ibn Al-Khtaab"
        },
        {
            "id": 2,
            "text": "من أعجب الأشياء أن تعرف الله ثم لا تحبه.",
            "author": "Ibn Al-Qaeem"
        },        
    ]
}
```

## Get Random Quote

This ruote provide a new random quote everyday.

`api.athkarok.tech/v1/quote/today` **`GET`**

### Success Response:

code : **`200`**

```Json
{
    "text": "من عمل بما علم ، أورثــه الله علم ما لم يعلم .",
    "author": "Ibn Taemeah"
}
```

## Add Quote

This route enforce having an `ADMIN` role to access.

We can check that from a valid token provided in the header.

If a normal user tried to access it, will get the following response.

code : **`403`**

```Json
{
    "error": "NOT ALLOWED TO ACCESS THIS RESOURCE."
}
```

`api.athkarok.tech/v1/quote` **`POST`**

### body:

Author field is optional.

```json
{
    "text": "لا يعجبكم من الرجل طنطنته، ولكن من أدى الأمانة وكف عن أعراض الناس، فهو الرجل.",
    "author": "Omar Ibn Al-Khtaab"
}
```


### Success Response:

code : **`200`**

```Json
{
    "success": "Quote added."
}
```

### Error Response:

In case of any missing of required data fields, and If any invalid input was provided, the error will show where exactly.

code : **`400`**

```Json
{
    "error": "Missing Or Invaild Input."
}
```
