# Section 10: Splash crash course

## 46: what dilemma was splash made to solve?
many sites are dependent on JavaScript, which makes it hard to scrape with just scrapy.
Scrapy doesn't have an engine to interpret Javascript. We have two choices:
1) Splash: its light weight and meant to be used with scrapy
2) Selenium: it's primarily a testing and automation tool. It wasn't developed for scraping, but it can be used for 
that. It's a bit more beginner-friendly.

## 49: how to set up splash (Linux)
unlike Windows & Mac on Linux machines installing Docker & Splash is a bit different, unfortunately there's no GUI 
like in Windows & Mac to interact with Docker so the only option you have is to use the terminal & launch a couple of 
commands to get the job done.

Now, before you even install Docker on your Linux machine please make sure your CPU & including your OS 
(operating system) are x86_64 (also know as 64bit) otherwise you won't be able to use Docker.

So to install Docker on Linux the first thing you need to do is to check if there are any updates, for that you have to 
open up the terminal & launch the command: 

```sudo apt update```

After that, execute the command below to allow 'apt' to use repositories over the 'HTTPS' protocol:

```
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```

Next, you have to add Docker's official GPG key by executing the following command:

```curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -```

Now after that you need to add Docker's repository so later you can install it as you install any other package:

```
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

After you've added the repository, please make sure to launch the command 

```sudo apt-get update``` 

again & then to install Docker just launch the command:

```sudo docker pull scrapinghub/splash```

Just give it a little bit of time to download Splash from Docker Hub & then after that you can launch Splash by using 
the following command:

```sudo docker run -it -p 8050:8050 scrapinghub/splash```

The command above will run Splash instance locally, so after that please don't kill the terminal windows in which 
you've executed Splash and then open up your browser & navigate to the following address:

```http://127.0.0.1:8050```

If everything went OK without any errors you should see the following:
<img src="splash.png"/>

## 50: introduction to Splash

restart here 

## 51: working with elements

## 52: spoofing request headers


