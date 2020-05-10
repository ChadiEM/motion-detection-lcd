# Motion detection to keep screen alive

Uses a HC-SR501 motion detector to keep LCD screen alive, then turns it off when no activity is detected for the specified amount of time.

Tested with Raspian buster, and [Waveshare 7inch HDMI LCD (C)](https://www.waveshare.com/7inch-HDMI-LCD-C.htm).

## Configuration
Modify `screen.py`'s ON and OFF behavior according to your needs. The default may or may not work for you. 

## Entry point

Start with:
`./motion.py <args>`

### Arguments
- `--pin`: the GPIO pin of the motion detector (required)
- `--timeout`: the timeout in seconds for the screen to turn off after motion (optional, default: 120) 
- `--verbose`: activates verbose mode for motion detection (optional, default: off) 

### Example

`./motion.py --pin=18 --timeout=300`
