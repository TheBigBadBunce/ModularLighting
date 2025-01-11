# Modular Lighting control

Designed to run on a Raspberry Pi Zero within my Lego modular city (on a shelf). Python3 throughout!

## Running the app

### Run in realtime indefinitely

Runs lighting in real time.
No arguments necessary.

```python lighting.py --mode=realtime```

This is the default mode so can also be run as `python lighting.py`....

### Run in realtime with a time offset

As above, but with 1 argument: time offset, in one of the following formats: `HH:MM:SS`, `HH:MM`, `MM`. Add a `-` to the start to offset into the past.

Run as if it's 3 hours and 27 minutes in the future:

```python lighting.py --mode=realtime --offset 3:27```

Run as if it's 14 minutes in the past:

```python lighting.py --mode=realtime --offset -14```

### Simulate a full day

Runs lighting at an accelerated rate. Takes 1 argument, the rate of simulation in minutes (simulated) per second (IRL). 

Simulate 1 day in 24 seconds (1 hour simulated every second):

```python lighting.py --mode=simulate --interval=60```

Simulate 1 day in 48 seconds (30 minutes simulated every second):

```python lighting.py --mode=simulate --interval=30```

### All lights on permanently

Run all lights at maximum level until program is killed..

```python lighting.py --mode=full```

### Full arguments list

Provided via command line or config file (`-c`/`--config`)


|Argument        |Accepted values             |Default            |Purpose|
|---             |---                         |---                |---    |
|`config`        |path to .yaml/.conf file    |lighting.yaml/.conf|Config file for arguments below, via [configargparse](https://pypi.org/project/ConfigArgParse/). Examples provided in `config/`|
|`mode`          |`realtime`/`simulate`/`full`|"realtime"         |Lighting mode. See above.|
|`offset`        |`HH:MM:SS`, `HH:MM`, `MM`   |0                  |Realtime: time difference from current. See above. Simulate/full: Ignored.|
|`interval`      |integer, 0 < i < 480        |0                  |Simulate: Interval between simulation ticks. Equal to minutes simulated per second. Realtime/full: Ignored.|
|`pir`           |boolean                     |false              |Use a PIR sensor (defined in `definitions.py`) to slowly dim lights to 0 when no movement is detected|
|`verbose`       |boolean                     |false              |Verbose debug output|
|`tick_printouts`|boolean                     |false              |Print/log a timestamp every tick. Ignores other log settings.|
|`silent`        |boolean                     |false              |Remove all console output. Especially useful for running in the background. Overrides `verbose`.|

---

## TODO

- Randomisation of on/off times
- Add a delay to PIR turnoff
- Remove flash when starting realtime (don't update LED level until all updates are done)
- Testing?