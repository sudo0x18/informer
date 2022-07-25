<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="#">
    <img src="https://i.imgur.com/ixfuCYE.png" alt="logo" height="135px">
  </a>

  <h2 align="center">Informer</h2>
  <p align="center">
    <a
      href="https://github.com/sudo0x18/informer/issues/new?assignees=&labels=bug">Report
      Bug</a>
    ·
    <a href="https://github.com/sudo0x18/informer/issues">Request Feature</a>
  </p>

  <img alt="informer" src="https://img.shields.io/github/stars/sudo0x18/informer">
  <img alt="informer" src="https://img.shields.io/github/issues/sudo0x18/informer">
  <img alt="informer" src="https://img.shields.io/github/languages/code-size/sudo0x18/informer">
  <img alt="informer" src="https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs">
  

</div>

<hr>

<h3 align="center">Informer is a OSINT information gathering tool that gathers whois, DNS, geolocation and shodan information of the target.</h3>

<hr>

## Installation

Install informer with git

```bash
  git clone https://github.com/sudo0x18/informer.git
  cd informer
```

## Requirment Installation

```bash
  pip install -r requirements.txt
```


## Usage
For Linux/Mac Os Use python3 and for Windows use python to run the script. 

#### Help Menu
```bash

    python3 informer.py --help

```

#### Simple Usage (whois Information Gethering)
```bash

    python3 informer.py -t google.com

```

#### Gather DNS Info
```bash

    python3 informer.py -d -t google.com

```

#### Gather Geolocation Info
```bash

    python3 informer.py -g -t google.com

```

#### Gather Shodan Info
```bash

    python3 informer.py -s -t google.com

```

#### Gather All Info togather
```bash

    python3 informer.py -d -g -s -t google.com

```

#### Save output to file
```bash

    python3 informer.py -d -g -s -t google.com -o filename.txt

```

## Contributing 💡

You can propose a feature request opening an issue or a pull request.

Here is a list of Osintgram's contributors:

<a href="https://github.com/Datalux/Osintgram/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=sudo0x18/informer" />
</a>