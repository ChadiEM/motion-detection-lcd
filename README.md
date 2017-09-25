# Motion detection to keep screen alive

Uses a HC-SR501 motion detector to keep LCD screen alive, then turns it off when no activity is detected for the specified amount of time.

## Configuration
In `motion.py`, edit the following:
- `PIR_PIN` Motion detector IO pin 
- `TIMEOUT` Time before is screen is shut down

Modify `screen.py`'s ON and OFF behavior according to your needs. 

## Entry point
`./motion.py`