<p align="center">
    <a href="https://github.com/ErRickow/mypyro">
        <img src="https://docs.pyrogram.org/_static/pyrogram.png" alt="Pyrogram" width="128">
    </a>
    <br>
    <b>Custom fork of Pyrogram with localized error messages and Layer 223 support</b>
    <br>
    <a href="https://github.com/ErRickow/mypyro">
        Homepage
    </a>
    •
    <a href="https://mypyro.readthedocs.io">
        Documentation
    </a>
    •
    <a href="https://github.com/ErRickow/mypyro/releases">
        Releases
    </a>
</p>

## MyPyro

> Custom fork of Pyrogram with localized error messages and Layer 223 support

``` python
from pyrogram import Client, filters

app = Client("my_account")


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from MyPyro!")


app.run()
```

**MyPyro** is a custom fork of the **Pyrogram** framework. It enables you to easily interact with the main Telegram API through a user account (custom client) or a bot identity (bot API alternative) using Python, with built-in support for localized Indonesian error messages and the latest MTProto features.

### Support

If you'd like to support Pyrogram, you can consider:

- [Become a GitHub sponsor](https://github.com/sponsors/delivrance).
- [Become a LiberaPay patron](https://liberapay.com/delivrance).
- [Become an OpenCollective backer](https://opencollective.com/pyrogram).

### Key Features

- **Ready**: Install Pyrogram with pip and start building your applications right away.
- **Easy**: Makes the Telegram API simple and intuitive, while still allowing advanced usages.
- **Elegant**: Low-level details are abstracted and re-presented in a more convenient way.
- **Fast**: Boosted up by [TgCrypto](https://github.com/pyrogram/tgcrypto), a high-performance cryptography library written in C.  
- **Type-hinted**: Types and methods are all type-hinted, enabling excellent editor support.
- **Async**: Fully asynchronous (also usable synchronously if wanted, for convenience).
- **Powerful**: Full access to Telegram's API to execute any official client action and more.

### Installing

``` bash
pip3 install https://github.com/ErRickow/mypyro/archive/refs/heads/dev.zip
```

### Resources

- The docs for MyPyro can be found here: https://mypyro.readthedocs.io.
- Check out the original Pyrogram docs for general library usage: https://docs.pyrogram.org.

### Copyright & License

- Copyright (C) 2017-2022 Dan <<https://github.com/delivrance>>
- MyPyro modifications Copyright (C) 2026 ErRickow
- Licensed under the terms of the [GNU Lesser General Public License v3 or later (LGPLv3+)](COPYING.lesser)

### INFO

- 📕 Repository: https://github.com/ErRickow/mypyro
- 📚 Docs: https://mypyro.readthedocs.io
- 📕 Original Pyrogram: https://github.com/pyrogram/pyrogram
