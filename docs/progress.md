# Progress

This route allows adding zikr reading sessions, wheel sessions to update user progress.

In order to get user progress visit User section [@me](./user.md#User-Data).

Progress routes enforce having a valid user token provided in the header to access, and must come from the app origin which is allowed by `CORS` policy.

If a none user tried to access them, will get the following response.

code : **`403`**

```Json
{
    "error": "NOT ALLOWED TO ACCESS THIS RESOURCE."
}
```

## Zikr

`api.athkarok.tech/v1/progress/zikr` **`POST`**

```Json
{
    "group_id" : 1
}
```

### Response:

code : **`200`**

```Json
{
    "success": "Zikr session successfully added."
}
```

## Wheel

`api.athkarok.tech/v1/progress/wheel` **`POST`**

### Response:

code : **`200`**

```Json
{
    "success": "Wheel session successfully added."
}
```