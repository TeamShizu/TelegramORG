# MyTelegramORG

~~(yet)~~ another my.telegram.org scrapper inside Telegram.

- can be found on [Telegram](http://t.me/MyTelegramORG_herobot)

## installing

## Deploy 

<b>Deploy on Heroku</b>
<p align="left">
  <a href="https://heroku.com/deploy?template=https://github.com/TeamShizu/TelegramORG">
     <img height="30px" src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku">
  </a>
</p>

##Deploy in your VPS
- clone the repository, locally.
```sh
git clone https://gitHub.com/TeamShizu/TelegramORG.git
```

- change the directory.
```sh
cd TelegramORG
```

- create a virtual environment.
```sh
virtualenv -p /usr/bin/python3 venv
```

- activate the virtual environment.
```sh
. ./venv/bin/activate
```

- install the requirements.
```sh
pip install -r requirements.txt
```

- create config.py

- run the bot
```sh
python3 bot.py
```

## [@Support group](https://t.me/ShizuUpdates)

- Only `TG_BOT_TOKEN` environment variables is mandatory.
- The Telegram RoBot should work without setting the non-mandatory variables.
- Please report any issues to the support group: [@Shizu](https://t.me/ShizuUpdates)


## learning

check out the [helper_funcs](https://github.com/TeamShizu/TelegramORG/tree/master/helper_funcs) directory, to see how my.telegram.org is scrapped.

## LICENSE
[AGPLv3](https://github.com/TeamShizuTelegramORG/tree/master/LICENSE)

