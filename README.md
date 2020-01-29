Radicale DecSync
================

Radicale DecSync is an [Radicale](https://radicale.org) storage plugin which adds synchronization of contacts and calendars using [DecSync](https://github.com/39aldo39/DecSync). This allows you to use DecSync on any CalDAV/CardDAV compatible client like [Thunderbird](https://thunderbird.net). To start synchronizing, all you have to do is synchronize the DecSync directory (by default `~/.local/share/decsync`), using for example [Syncthing](https://syncthing.net). It works on both Linux and Windows.

Installation
------------

It is preferred to install the Radicale server on the same device as you will run the client on, as you can leave it remotely inaccessible in that case.

You need to install the `radicale_storage_decsync` package from PyPI:
```
pip3 install radicale_storage_decsync
```

Configuration
-------------

Save the following in `~/.config/radicale/config`:
```
[storage]
type = radicale_storage_decsync
filesystem_folder = ~/.var/lib/radicale/collections
decsync_dir = ~/.local/share/decsync
```
You may want to adjust the `filesystem_folder` or `decsync_dir`. The `filesystem_folder` denotes the directory in which Radicale stores its files, its location is not very important. The `decsync_dir` denotes the DecSync directory, i.e. the directory you need to synchronize with other devices.

Then, to launch the Radicale server, execute
```
python3 -m radicale --config "~/.config/radicale/config"
```
When the server is launched, you can configure it at [localhost:5232](http://localhost:5232). By default, any username and password is accepted, which should be fine as long as you do not make the server remotely accessible. For more configuration options, see the Radicale's [documentation](https://radicale.org/documentation) page.

Documentation on configurating clients can be found on Radicale's [clients](https://radicale.org/clients) page.

Furthermore, Radicale is not started automatically after a reboot. You need to start it manually, or set up autostart based on your OS.

Donations
---------

### PayPal
[![](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=4V96AFD3S4TPJ)

### Bitcoin
[`1JWYoV2MZyu8LYYHCur9jUJgGqE98m566z`](bitcoin:1JWYoV2MZyu8LYYHCur9jUJgGqE98m566z)
