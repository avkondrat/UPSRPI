#!/bin/bash
echo "Run delay script at $(date)" > /home/alex/delay.log
echo "Read UPS data to Blynk" >> /home/alex/delay.log
python3 /home/alex/UPS_HAT/INA219.py
 


