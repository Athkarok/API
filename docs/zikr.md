# Zikr

This route allows Retrieving zikrs, Adding, Editing, or Deleting.

## Get Zikrs

`api.athkarok.tech/v1/zikr/?group_id={}` **`GET`**

Group ID Keys :
```
    Sabah: 1,
    Masaa: 2,
    Noom: 3,
    Estekaz: 4,
    Massjed: 5,
    Slaah: 6,
```

Specify a particular group to retrieve a list of all the zikrs from.


#### Response:

code : **`200`**

```Json
{
    "zikrs": 
    [
        {
            "id": 1,
            "group_id": 1,
            "text": "بسمِ اللهِ الذي لا يضرُّ مع اسمِه شيءٌ في الأرضِ ولا في السماءِ وهو السميعُ العليمُ.",
            "dalel": "ما من عبدٍ يقولُ في صباحِ كلِّ يومٍ ومساءِ كلِّ ليلةٍ بسمِ اللهِ الذي لا يضرُّ مع اسمِه شيءٌ في الأرضِ ولا في السماءِ وهو السميعُ العليمُ ثلاثَ مراتٍ فيضرُّه شيٌء <br> الراوي : عثمان بن عفان | المحدث : الألباني | المصدر : صحيح ابن ماجه | الصفحة أو الرقم : 3134 | خلاصة حكم المحدث : صحيح | انظر شرح الحديث رقم 36007",
            "dalel_link": "https://dorar.net/h/3328f09a7cab765ca29211488aa9d4a6",
            "repeat_times": 3,
            "weak": 0
        },
    ]
}
```

## Protected Routes

The next routes enforce having an `ADMIN` role to access.

We can check that from a valid token provided in the header.

If a normal user tried to access them, will get the following response.

code : **`403`**

```Json
{
    "error": "NOT ALLOWED TO ACCESS THIS RESOURCE."
}
```

### Add Zikr

`api.athkarok.tech/v1/zikr` **`POST`**

#### body:

```json
{
    "group_id": "Number must be a valid group id.",
    "text": "String contains zikr text.",
    "repeat_times": "Number",
    "dalel": "String contains zikr dalel.",
    "dalel_link": "String contains zikr dalel link",
    "weak": "0 or 1 : for false and true"
}
```

ex:

```json
{
    "group_id": 1,
    "text": "zikr text.",
    "repeat_times": 3,
    "dalel": "zikr dalel.",
    "dalel_link": "zikr dalel link.",
    "weak": 0
}
```

#### Success Response:

code : **`200`**

```Json
{
    "success": "Zikr added successfully."
}
```

#### Error Response:

In case of any missing of required data fields, and If any invalid input was provided, the error will show where exactly.

code : **`400`**

```Json
{
    "error": "Missing Or Invaild Input."
}
```

### Edit Zikr

To edit the entire data about a specific zikr.

Must provide zikr id with the data fields. 

`api.athkarok.tech/v1/zikr` **`PUT`**

#### body:

```json
{
    "id": 1,
    "group_id": 5,
    "text": "new zikr text.",
    "repeat_times": 3,
    "dalel": "new zikr dalel.",
    "dalel_link": "new zikr dalel link.",
    "weak": 0
}
```

To edit some data about a specific zikr.

Must provide zikr id and the fields you want to edit. 

`api.athkarok.tech/v1/zikr` **`PATCH`**

#### body:

```json
{
    "id": 1,
    "text": "new zikr text."
}
```

#### Success Response:

code : **`200`**

```Json
{
    "message": "zikr updated."
}
```

#### Error Response:

In case of any missing of required data fields, and If any invalid input was provided, the error will show where exactly.

code : **`400`**

```Json
{
    "error": "Missing Or Invaild Input."
}
```

### Delete Zikr

Provide zikr id to delete.

#### body:

```json
{
    "id": 1
}
```

#### Success Response:

code : **`200`**

```Json
{
    "message": "zikr removed."
}
```

#### Error Response:

In case of missing or invalid zikr id, the error will show it.

code : **`400`**

```Json
{
    "error": "Invaild Input."
}
```