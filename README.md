# SFTP
My SFTP Server

## Installation & Configuration
```bash
git clone git@github.com:elleaech/sftp.git

cd sftp && scripts/setup
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
sftp/addUser --help
```

## Contributing
Fork it, or whatever. Free software, do what you want, but, please, [Pull Request first](https://github.com/elleaech/sftp/pulls).

## License & Issue Tracker
- [Issues](https://github.com/elleaech/sftp/issues)
- [Apache License 2.0](https://github.com/elleaech/sftp/blob/master/LICENSE)
