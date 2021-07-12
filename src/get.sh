#!/bin/bash
echo "
 ___      ___     ___      ___            ___      ___     ___      __
(__ \    / _ \   (__ \    / _ \    ___   (__ \    / _ \   (__ \    /  )
 / _/   ( (_) )   / _/   ( (_) )  (___)   / _/   ( (_) )   / _/     )(
(____)   \___/   (____)   \___/          (____)   \___/   (____)   (__)




  ____  __  __   ___       ____  ____
 (_  _)(  \/  ) / __) ___ (_  _)(_  _)
.-_)(   )    ( ( (_-.(___) _)(_   )(
\____) (_/\/\_) \___/     (____) (__)




   __    __    __      ____  ____   ___  _   _  ____  ___    ____  ____  ___  ____  ____  _  _  ____  ____
  /__\  (  )  (  )    (  _ \(_  _) / __)( )_( )(_  _)/ __)  (  _ \( ___)/ __)( ___)(  _ \( \/ )( ___)(  _ )
 /(__)\  )(__  )(__    )   / _)(_ ( (_-. ) _ (   )(  \__ \   )   / )__) \__ \ )__)  )   / \  /  )__)  )(_) )
(__)(__)(____)(____)  (_)\_)(____) \___/(_) (_) (__) (___/  (_)\_)(____)(___/(____)(_)\_)  \/  (____)(____/

head@jmg-it.de
"


echo current dir:
sudo ls 

echo date:
sudo date

echo stoping NGINX
sudo systemctl stop nginx

echo killing ports
sudo pkill -f nginx & wait $!

echo obtaining IPsoup, standby...
sudo python3 /var/lib/elasticip/src/req.py

echo getting IP from result soup
sudo python3 /var/lib/elasticip/src/main.py

echo cleaning and deploying nginx conf

sudo rm -rf /var/lib/elasticip/src/nginx.conf

sudo rm -rf /var/lib/elasticip/src/ip.yml

sudo python3 /var/lib/elasticip/src/side.py

sudo cp /var/lib/elasticip/src/nginx.conf /etc/nginx/nginx.conf

sudo systemctl start nginx
