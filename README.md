
# Informer 
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

Informer is a Basic information gathering tool that provides various information about target like whois info,DNS info, Geolocation info of server and Shodan info.

![App Screenshot](https://i.ibb.co/CsfMvTf/informer.png)
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