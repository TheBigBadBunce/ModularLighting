# Device definition

Devices are specified in a definition file, by default `lighting.json`. An example is provided with my current setup. The format of the JSON should be as follows:

```json
[
    {"type": "output", ...},
    {"type": "output", ...},
    {"type": "input", ...}
]
```

Each device definition depends on the type of device. These are listed here:

## [Output device](../devices/output.py)

An output LED.

### Example
```json
{
    "type": "output",
    "pin": 26,
    "location": "Art shop",
    "schedules": [ ... ]
}
```

|Property   |Value              |Use|
|---        |---                |---|
|`pin`      |number             |GPIO pin of LED|
|`location` |string             |Location in set. Only used for user-friendly identification|
|`schedules`|array of schedules |Schedules and their definitions are defined [elsewhere](schedules.md).|

## [Input device](../devices/input.py)

An input GPIO device, such as a PIR sensor that reads high when lights should be on, and low when they should be off. Theoretically this could be a button or other input.
Enabled with the `-p` option (see [README](README.md))

### Example
```json
{
    "type": "input",
    "pin": 11
}
```

|Property   |Value              |Use|
|---        |---                |---|
|`pin`      |number             |GPIO pin of device|