# SFTP
My SFTP Server

## Installation & Configuration
```bash
git clone git@github.com:sourcerer0/sftp.git

cd sftp && scripts/SymLynk && scripts/setup
```

### Setup sftp-server at /etc/ssh
Comment the following line at "sshd_config":
```
#Subsystem      sftp    /usr/libexec/openssh/sftp-server
```

Add:
```
Subsystem       sftp    internal-sftp

Match Group GROUP_NAME
	ChrootDirectory %h
	X11Forwarding no
	AllowTcpForwarding no
	ForceCommand internal-sftp
```

Save file and:
```
scripts/reser
```

## Adding sftp users
```bash
addUser --help
```

> Note: ./SymLynk creates a symbolic link at /usr/local/bin for src scripts
>
> Don't forget to check where the original SymLynk script was [first created](https://github.com/sourcerer0/sourcery)

## Contributing
Fork it, or whatever. Free software, do what you want, but, please, [Pull Request first](https://github.com/sourcerer0/sftp/pulls).

## License & Issue Tracker
- [Issues](https://github.com/sourcerer0/mySFTP/issues)
- [Apache License 2.0](https://github.com/sourcerer0/mySFTP/blob/master/LICENSE)
