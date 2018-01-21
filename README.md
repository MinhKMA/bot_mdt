# Telebot for Meditech

A [Telegram](https://telegram.org/) Bot written in Python (Work-In-Progress)

## Installation

1. Clone this repo and install all requirements:

```
$ git clone https://gitlab.com/hocchudong/telebot_hcd.git
$ sudo -H pip3 install -r requirements.txt
```

2. Run Setup

```
cd bot_mdt
python3 setup.py install
```

3. Edit tele.conf file and move it to /etc/telegram/

```
cd bot_mdt/etc
sed -i "s/TETO/Your token/g" tele.conf
sudo mkdir /etc/telebot
sudo mv tele.conf /etc/telebot/
```

4. Install supervisor package

```
sudo apt install -y supervisor
sudo cp bot_mdt.conf /etc/supervisor/conf.d/
```

5. Start BOT

```
sudo supervisorctl update
sudo supervisorctl start bot_mdt
```


