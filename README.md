# Pypo

- Pypo is an abbreviation for Python pomodoro. 
- Its a simple pomodoro cli based timer with some additional super powers
  - It remembers the tasks that you did using the timer (stored in a JSON file) and can show you what you have done so far today or what you did yesterday (useful for standups?) 
  - It notifies you at the timer end with a sound

This is the first cut and we would be adding more features soon...

> All the data is stored in a local `timer.json` file on your local machine.

## Setup

- Create a virtualenv using venv or pipenv
- Give install script permissions using `chmod +x install.sh`
- Once inside the activated venv execute `install.sh` shell script to install
- Find the `bin` folder inside your virtualenv directory
- Execute `cp pypo /usr/local/bin` to allow pypo to be available anywhere in the terminal


## Usage

Start a timer

```zsh
pypo timer --until 2 --task="First task"
```

```zsh
Starting task => "First task" 😉
Press Ctrl + C to exit ...

 ⏰  01:58
Stopped working on "First task" at: 10:36:19
Logging your work..
Good job. Remember to take a break now! ... 🏃️
Take a walk, have water and breathe ...
```

See work done so far

```zsh
pypo time-machine
```

```zsh
Work log for Day: 2020-07-04
------------------------------
2 RECORDS FOUND
#1 Task: First task started at: 10:25:35 ended at: 10:25:42
#2 Task: First task started at: 10:36:17 ended at: 10:36:26
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