Steps to set up systemd.timer to run this application
---

1. Create file covid_19_twitter_bot.service in /etc/systemd/system
```
[Unit]
Description=Powers a Python Twitter bot, that provides users with swiss covid data
Wants=covid_19_twitter_bot.timer

[Service]
Type=oneshot
ExecStart=/usr/bin/python3.8 /home/timon/workspace/m122/M122_Covid19_Twitter_Bot/covid_19_twitter_bot/__init__.py

[Install]
WantedBy=multi-user.target
```
2. Replace paths at ExecStart
3. Create file covid_19_twitter_bot.timer in /etc/systemd/system
```
[Unit]
Description=Powers a Python Twitter bot, that provides users with swiss covid data
Requires=covid_19_twitter_bot.service

[Timer]
Unit=covid_19_twitter_bot.service
OnCalendar=*:*:0/10

[Install]
WantedBy=timers.target
```
4. Start Service: ```sudo systemctl start covid_19_twitter_bot.service```
5. View Log: ```sudo journalctl -S today -u covid_19_twitter_bot.service```
