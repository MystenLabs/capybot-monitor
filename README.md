# capybot-monitor

## Overview
The Capybot Monitor is a collection of Python scripts to monitor the status of a running instance of a [Capybot trading bot](https://github.com/MystenLabs/capybot). It produces plots of the price development and key status indicators used by Capybot. The plots are updated live.

## Installation and Running
First download and install the Capybot trading bot as instructed in the [Capybot repository]](https://github.com/MystenLabs/capybot). Run the Capybot and store the output to a file
```
npm run start > capybot.log
```
Now, first clone this repo. Run the `pools.py` script and give the path to the log file above as an argument, e.g.
```
python3 pools.py ../capybot/capybot.log
```
This should show a window showing the price development relative to when the Capybot was started.
![pools](https://github.com/MystenLabs/capybot-monitor/assets/6288307/228de1ee-0e47-4737-83f9-486d79876b9b)

The `strategies.py` script is started in the same way but produces plots of relevant variables for the trading strategies the Capybot is using. A red vertical line shows that the given strategy gave a trade order at this point in time.
![strategies](https://github.com/MystenLabs/capybot-monitor/assets/6288307/af5ec32f-bd56-4761-ac38-a2f47d848d46)
