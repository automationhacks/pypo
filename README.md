# Pypo

Pypo is a short abbreviation of Python pomodoro. 
Its a simple pomodoro timer along with task tracking all in CLI and also 
records your tasks for future reflection

This is the first cut and we would be adding more features soon...

> All the data is stored in a local `timer.json` file on your local machine.

## Setup

- Create a virtualenv using venv or pipenv
- Once inside the venv execute below to install

```zsh
pip install --editable .
```

## Usage

Start a timer

```zsh
pypo timer --until 2 --task "some meaningful task"
```

```zsh
Starting task => "some meaningful task"
Press Control + C to exit ... 

 ⏰  01:53
Stopped working on "some meaningful task" at: 17:04:14
Logging your work..
Remember to take a break! ... Go out for a walk... ☮️
```

See work done so far

```zsh
pypo time-machine
```

```zsh
1 Day: 2020-07-03 Task: First task started at: 11:32:05 ended at: 11:32:20
2 Day: 2020-07-03 Task: some meaningful task started at: 11:34:06 ended at: 11:34:20
```

If you want to clear all existing records, execute below followed by a `y`

```zsh
pypo flush
```

```zsh
Warning: This will remove all your work record db.
Do you still want to continue: [y/n]
y
Your db has been reset. You have a clean slate again...
```

## Roadmap

- Ability to tag your tasks based on categories and filter them
- Ability to filter data across a specific time period if interested
- Data roll ups and statistics.