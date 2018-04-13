# HeatFair

A Python heat logger that catalogs heat and stores it into a JSON with help of my writer component.
Just edit the ```interval``` and ```meassurements``` variable in ```HeatFair.py``` to your liking.

-------

Meassurements is the amount of meassurements taken into consideration for the average that is going to be stored.
Interval is the time between the meassurements in seconds.

Total time between datapoints will then be ```meassurements``` * ```interval```

-------

By default, up to 500 datapoints will be stored in ```output.json``` for easy access. This number can be adjusted in the ```datapoints``` variable. When the maximum of datapoints is reached, the logger will write the oldest datapoint to a seperate file called ```legacy.json``` where all datapoints will be collected without a maximum.
