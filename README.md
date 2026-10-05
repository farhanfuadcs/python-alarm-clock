# Python Alarm Clock

A simple command-line alarm clock built with Python. The user enters a duration in minutes and seconds, and the program displays a live countdown before playing an alarm sound when the timer reaches zero.

## Features

* Set alarm duration in minutes and seconds
* Live countdown display
* Displays remaining minutes and seconds
* Plays an audio alarm when the countdown finishes
* Simple command-line interface

## Example

```text id="r3o1sl"
Enter the alarm minutes: 1
Enter the alarm seconds: 30

The alarm will ring in 01 : 29
The alarm will ring in 01 : 28
The alarm will ring in 01 : 27
...
The alarm will ring in 00 : 01
```

When the countdown reaches zero, the program plays the `alarm.mp3` sound.

## Technologies Used

* Python
* `time`
* `playsound3`
* Terminal escape sequences
* Functions
* Loops
* User input
* Basic time calculations

## Installation

Install the required audio library:

```bash
pip install playsound3
```

## How to Run

Make sure Python is installed and `playsound3` is installed.

Place an audio file named:

```text
alarm.mp3
```

in the same directory as the Python file.

Then run:

```bash
python alarm_clock.py
```

Enter the desired minutes and seconds when prompted.

## What I Practiced

This project helped me practice:

* Creating functions
* Working with loops
* Using the `time` module
* Converting minutes into seconds
* Calculating remaining time
* Formatting numbers with leading zeros
* Using external Python packages
* Playing audio from Python
* Updating terminal output

## Known Limitations

* The alarm sound must be available as `alarm.mp3`.
* The program runs only as a command-line application.
* There is currently no pause or cancel option.
* The user must enter valid numeric values.
* The countdown is based on one-second intervals.

## Future Improvements

* Add pause and resume functionality
* Add a cancel option
* Allow users to select different alarm sounds
* Add a graphical interface
* Add multiple alarms
* Validate minutes and seconds more strictly
* Add a clock showing the current time
