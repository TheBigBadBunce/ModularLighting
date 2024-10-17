# Modular Lighting control

Designed to run on a Raspberry Pi Zero within my Lego modular city (on a shelf). Python3 throughout!

## Runing the app

### Run in realtime indefinitely

Runs lighting in real time.
No arguments necessary.

```python lighting.py --realtime```

### Run in realtime with a time offset

Runs lighting in real time.
1 argument: time offset, in one of the following formats: `HH:MM:SS`, `HH:MM`, `MM`. Add a `-` to the start to offset into the past.

Run as if it's 3 hours and 27 minutes in the future:

```python lighting.py --offset 3:27```

Run as if it's 14 minutes in the past:

```python lighting.py --offset -14```

### Simulate a full day

Runs lighting at an accelerated rate. Takes 1 argument, the rate of simulation in minutes per second.

Simulate 1 day in 24 seconds (1 hour simulated every second):

```python lighting.py --simulate 60```

Simulate 1 day in 48 seconds (30 minutes simulated every second):

```python lighting.py --simulate 30```

### Other arguments

- `verbose`: Verbose debug output
- `silent` : Remove all console output. Especially useful for running in the background.