# Schedule definition

Devices are specified within [device definitions](devices.md).  

```json
[
    { "type": "consistent daily", ... },
    { "type": "consistent daily dimmed", ... }
]
```

Each schedule definition depends on the type of schedule. These are listed here:

## [Always on](../schedules/ConsistentDailySchedule.py)

Dead simple: Light turns on and never turns off.

```json
{
    "type": "always on"
}
```

## [Consistent Daily](../schedules/ConsistentDailySchedule.py)

A simple schedule where the light is on between 2 fixed times.

```json
{
    "type": "consistent daily",
    "start_time": "7:00",
    "end_time": "8:00"
}
```

|Property       |Purpose|
|---            |---    |
|`start_time`   |When the light switches on|
|`end_time`     |When the light switches off|
|`variance`     |Random variance on event time (in minutes)|

## [Consistent Daily Dimmed](../schedules/ConsistentDimmedDailySchedule.py)

Almost identical to Consistent Daily Schedule, with a steady dim on/off.

```json
{
    "type": "consistent daily dimmed",
    "start_time": "7:00",
    "end_time": "8:00",
    "dim_up_time": "8",
    "dim_down_time": "12"
}
```

|Property       |Purpose|
|---            |---    |
|`start_time`   |When the light switches on|
|`end_time`     |When the light switches off|
|`dim_up_time`  |Time taken for the light to dim on, in seconds|
|`dim_down_time`|Time taken for the light to dim off, in seconds|
|`variance`     |Random variance on event time (in minutes)|