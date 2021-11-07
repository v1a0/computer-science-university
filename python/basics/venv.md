# Create Virtual Environment, Activate/Deactivate

## Win

```shell
mkdir my_project
cd my_project
python3 -m venv env

env\Scripts\activate.bat

env\Scripts\deactivate.bat
```

## Unix

```shell
sudo apt install -y python3-pip
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
sudo apt install -y python3-venv

mkdir myapp
cd myapp
python3 -m venv env

source env/bin/activate

deactivate
```


# Bash script

```shell
#!/usr/bin/env bash
BASEDIR=$(dirname "$0")
echo "Executing App in '$BASEDIR'"
PORT=$1
source $BASEDIR/env/bin/activate
python $BASEDIR/service.py $PORT
```

```shell
chmod +x myapp/run.sh
./myapp/run.sh 8888
```