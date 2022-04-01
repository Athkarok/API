# Form

This ruote allows submitting forms for different purposes, send confirmation email for the sender and app admin.

The request must come from the app origin which is allowed by `CORS` policy.

## Contact Form

`api.athkarok.tech/v1/form/contact` **`POST`**

### body:

```json
{
    "name": "Ahmed Mohamed",
    "role": "suggestion",
    "message": "I think it would be nice to if you guys add a section to encourage people to finish reading quran every month."
}
```

### Response:

code : **`200`**

```Json
{
    "success": "Form Successfully submitted."
}
```