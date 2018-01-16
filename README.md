sa-grafana
##########


[![Build Status](https://travis-ci.org/softasap/sa-grafana.svg?branch=master)](https://travis-ci.org/softasap/sa-grafana)


Usage:
----------------------------------

Simple:

```YAML

- {
    role: "sa-grafana",
    grafana_admin_user: grafana,
    grafana_admin_password: GrAfAnA!

  }


```

Advanced:

```YAML

vars:

  grafana_custom_properties:
    - {regexp: "^;allow_sign_up =(.*)", line: "allow_sign_up=false"}


roles:
  - {
      role: "sa-grafana",
      grafana_admin_user: grafana,
      grafana_admin_password: GrAfAnA!,

      grafana_properties: "{{grafana_custom_properties}}"

    }


```


Installing on Debian / Ubuntu
----------------------------------

Install Stable
----------------------------------

```bash
$ wget https://grafanarel.s3.amazonaws.com/builds/grafana_3.1.1-1470047149_amd64.deb
$ sudo apt-get install -y adduser libfontconfig
$ sudo dpkg -i grafana_3.1.1-1470047149_amd64.deb
```

APT Repository
----------------------------------

Add the following line to your /etc/apt/sources.list file.
```bash
deb https://packagecloud.io/grafana/stable/debian/ wheezy main
```
Use the above line even if you are on Ubuntu or another Debian version. There is also a testing repository if you want beta or release candidates.

```bash
deb https://packagecloud.io/grafana/testing/debian/ wheezy main
```
Then add the Package Cloud key. This allows you to install signed packages.

```bash
$ curl https://packagecloud.io/gpg.key | sudo apt-key add -
```
Update your Apt repositories and install Grafana

```bash
$ sudo apt-get update
$ sudo apt-get install grafana
```

On some older versions of Ubuntu and Debian you may need to install the apt-transport-https package which is needed to fetch packages over HTTPS.

```bash
$ sudo apt-get install -y apt-transport-https
```

Package details
----------------------------------

Installs binary to /usr/sbin/grafana-server
Installs Init.d script to /etc/init.d/grafana-server
Creates default file (environment vars) to /etc/default/grafana-server
Installs configuration file to /etc/grafana/grafana.ini
Installs systemd service (if systemd is available) name grafana-server.service
The default configuration sets the log file at /var/log/grafana/grafana.log
The default configuration specifies an sqlite3 db at /var/lib/grafana/grafana.db
Start the server (init.d service)
Start Grafana by running:

```bash
$ sudo service grafana-server start
```

This will start the grafana-server process as the grafana user, which was created during the package installation. The default HTTP port is 3000 and default user and group is admin.

To configure the Grafana server to start at boot time:

```bash
$ sudo update-rc.d grafana-server defaults 95 10
```

Start the server (via systemd)
----------------------------------

To start the service using systemd:

```bash
$ systemctl daemon-reload
$ systemctl start grafana-server
$ systemctl status grafana-server
```

Enable the systemd service so that Grafana starts at boot.


```bash
sudo systemctl enable grafana-server.service
```


Environment file
----------------------------------

The systemd service file and init.d script both use the file located at /etc/default/grafana-server for environment variables used when starting the back-end. Here you can override log directory, data directory and other variables.

Logging
----------------------------------

By default Grafana will log to /var/log/grafana

Database
----------------------------------

The default configuration specifies a sqlite3 database located at /var/lib/grafana/grafana.db. Please backup this database before upgrades. You can also use MySQL or Postgres as the Grafana database, as detailed on the configuration page.

Configuration
----------------------------------

The configuration file is located at /etc/grafana/grafana.ini. Go the Configuration page for details on all those options.

 Ideas for dashboards:
 ----------------------------------

MYSQL:   https://github.com/percona/grafana-dashboards

Ideas for Tools
----------------------------------

SHELL: https://github.com/hagen1778/grafana-import-export
PYTHON: https://github.com/m110/grafcli  



Usage with ansible galaxy workflow
----------------------------------

If you installed the `sa-prometheus-exporters` role using the command


`
   ansible-galaxy install softasap.sa-prometheus-exporters
`

the role will be available in the folder `library/softasap.sa-prometheus-exporters`
Please adjust the path accordingly.

```YAML

     - {
         role: "softasap.sa-nginx"
       }

```  



Copyright and license
---------------------

Code is dual licensed under the [BSD 3 clause] (https://opensource.org/licenses/BSD-3-Clause) and the [MIT License] (http://opensource.org/licenses/MIT). Choose the one that suits you best.

Reach us:

Subscribe for roles updates at [FB] (https://www.facebook.com/SoftAsap/)

Join gitter discussion channel at [Gitter](https://gitter.im/softasap)

Discover other roles at  http://www.softasap.com/roles/registry_generated.html

visit our blog at http://www.softasap.com/blog/archive.html
