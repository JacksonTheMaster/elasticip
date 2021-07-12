<!--

-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://www.hetzner.com/assets/Uploads/icon-circle-cloud.svg">
    <img src="https://www.hetzner.com/assets/Uploads/icon-circle-cloud.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">elasticp</h3>

  <p align="center">
    For Detailed Documentation see our website:
    <br />
    <a href="https://jmg-it.de/docs"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/jacksonthemaster/elasticip/src">View Files</a>
    ·
    <a href="https://github.com/jacksonthemaster/elasticip/issues">Report Bug</a>
    ·
    <a href="https://github.com/jacksonthemaster/elasticip/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project




Enough struggle with Dyndns, hostnames like jtm.dnsmonster.someweirdTLD are evil and bad and not routable in A records.
So I present this:


With elasticip, getting your own Public IP address has never been easier. 

Basically, we use a Cloud-providers IP and route it to us, which costs me 2,96€ /3,51$ a month. 😀 😃 😄 😁 @ RIPE :)

Btw, I have no Idea if this Is legal. I hope no one will raid down my doors for this, but maybe some Amazon EC2 manager will. Who knows.



In order for this to work, follow this:

### Built With

* [Python](Python)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites###

-A cloud instance from a hoster (hetzner, linode, amazon ec2, hetzner, whatever u prefer)

-Running ubuntu (debian not tested- feel free to do so, probably works)


-A static ip from your cloud provider configured on that machine 


-A registerd Cloudflare account


-A working dyndns solution; i recommend <a href="www.dnsomatic.com">www.dnsomatic.com</a> 


-A DEFINITE A record on your Domain beeing updated by DDNS, e.g DNSomatic ⬆️



definite = if elasticip searches for dynamic.contoso.net, it should only find one record. If you set up your A records in some weird way, you should change your ddns updated A record to MYVERYSPECIFICRECORD12345.contoso.net or sth like that. You get the spirit.

Update your system
  ```sh
  sudo apt-get update
  ```
Install NGINX
  Update your system
  ```sh
  sudo apt-get install nginx
  ```

### Installation

1. Clone the repo
   ```sh

    mkdir /var/lib/elasticip

    git clone https://github.com/jacksonthemaster/elasticip.git /var/lib/elasticip
   ```
2. Edit req.py
   ```sh
   cd /var/lib/elasticip/src

   nano req.py

   for info, see below.
   ```
3. setup cron schedule (this sets it up for every minute, which should be just fine.)
   ```sh
   crontab -e 
   first use: 
   1

   ADD THIS LINE;

   * * * * * sudo /bin/bash /var/lib/elasticip/src/get.sh > /var/lib/elasticip/src/cronlog.yml

    close with ctrl+s & ctrl+x

    wait (you can check time with command: date)
   ```

   
Make sure to replace the cloudflare account data spaces in /elasticip/src/req.py with your own.




 ```sh
 ZONE-ID: google "how to get cloudflare Zone ID, it's easy.
 url: 'https://api.cloudflare.com/client/v4/zones/Cloudflare-ZONE-ID/dns_records?type=A&name=DEFINITE_A_RECORD.DOMAIN.TLD&type=&page=1&per_page=20&order=type&direction=desc&match=all'
 bearer: A Cloudflare accsess Token for your account (settings page, tokens. If unsure, use origin key.)
 email: your cloudflare registerd Email.
   ```

This data can be obtained in many ways, Zone ID and Token probably beeing the hardest to google. I leave this on you, but feel free to contact me.

<!-- USAGE EXAMPLES -->
## Usage
none, sorry guys :uwu


<!-- ROADMAP -->
## Roadmap

none, sorry guys :uwu


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Jacky - [jlangisch](https://twitter.com/jlangisch) - jacky@jmg-it.de

Project Link: [https://github.com/jacksonthemaster/elasticip (https://github.com/jacksonthemaster/elasticip)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [My Database Admin for listening to me while coding this](My Database Admin for listening to me while coding this)






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jacksonthemaster/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/jacksonthemaster/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jacksonthemaster/repo.svg?style=for-the-badge
[forks-url]: https://github.com/jacksonthemaster/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/jacksonthemaster/repo.svg?style=for-the-badge
[stars-url]: https://github.com/jacksonthemaster/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/jacksonthemaster/repo.svg?style=for-the-badge
[issues-url]: https://github.com/jacksonthemaster/repo/issues
[license-shield]: https://img.shields.io/github/license/jacksonthemaster/repo.svg?style=for-the-badge
[license-url]: https://github.com/jacksonthemaster/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jacksonthemaster
