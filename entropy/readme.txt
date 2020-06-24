run as docker-compose service:
$ docker-compose up -d --build

methods:

- Create alarm
    curl --location --request POST 'http://localhost:8000/api/v1/alarmclock/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "description": "test alarm",
        "when_will_alarm": "2020-06-24T11:47:00+03"
    }'
    -- output:
        {
            "id": 1,
            "description": "test alarm",
            "when_will_alarm": "2020-06-24T08:47:00Z"
        }

- Get alarm lists:
    curl --location --request GET 'http://localhost:8000/api/v1/alarmclock/'
    -- output:
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
                {
                    "id": 1,
                    "description": "test alarm",
                    "when_will_alarm": "2020-06-24T08:47:00Z"
                }
            ]
    }

waiting alarm:
    ws://localhost:8000/ws/alarm/
    -- output:
        {
          "id": 63,
          "description": "test alarm",
          "when_will_alarm": "2020-06-24T08:47:00Z"
        }

