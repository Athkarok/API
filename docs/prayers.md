# Prayers

This route allows getting hijri date, muslim prayer times according to user position.

## Get Radio

`api.athkarok.tech/v1/prayers/?latitude={}&longitude={}` **`GET`**


### Response:

code : **`200`**

```json
{
    "date": {
        "hijri": {
            "date": "28-08-1443",
            "day": "28",
            "format": "DD-MM-YYYY",
            "holidays": [],
            "month": {
                "ar": "شَعْبان",
                "en": "Shaʿbān",
                "number": 8
            },
            "weekday": {
                "ar": "الخميس",
                "en": "Al Khamees"
            },
            "year": "1443"
        },
        "readable": "31 Mar 2022",
        "timestamp": "1648742515"
    },
    "timings": {
        "Asr": "15:31",
        "Dhuhr": "12:00",
        "Fajr": "04:24",
        "Imsak": "04:14",
        "Isha": "19:44",
        "Maghrib": "18:14",
        "Midnight": "00:00",
        "Sunrise": "05:47",
        "Sunset": "18:14"
    }
}
```
