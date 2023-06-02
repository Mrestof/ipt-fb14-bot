## FAQ:
- Any general, organizational or backend question -
    contact [mrestof](https://github.com/Mrestof)
- Any user-end features or backend question -
    contact [netrunner](https://github.com/netrunner4)
    or [syitb](https://github.com/GMtranscendence)


## Features

### frontend:
- [x] diary
  - [x] look at saved notes
  - [x] ping opted-in users a day before the note date
  - [x] add, remove, modify notes by date
  - [x] automatically delete expired notes
- [x] schedule
  - [x] get list of subject and links to them for any day
- [x] markov
  - [x] imitate user's messages using markov chains
- [ ] wallhaven
  - [ ] show random beautiful images
- [ ] optional dev mode: clean the message:response pairs once in a while

### backend:
- [ ] logging support
  - [x] log default stuff: startup, utils usage, warnings and errors
  - [ ] log different levels with different handlers
  - [ ] log message:response pairs
- [ ] code formatter (probably black)
- [ ] pythonic configs
  - [ ] create the config system with default python objects
  - [ ] put all constants there
- [ ] tests
- [ ] support for bot management from console (with TUI or techs alike)
- [ ] manage dependencies with pipenv


## TODO

### global:
- [ ] find a more suitable project hierarchy
- [ ] discuss the usefulness of "general refactor" todo's and notes
- [ ] requirements.txt: `ptb` and `ptb[job-queue]` are probably duplicates;
    check and fix if possible
- [ ] refactor
  - [ ] change variable names to make more sense
  - [ ] expand unreadable oneliners
  - [ ] replace OS calls with python alternatives
  - [ ] save temp files in temp directories, not inside the bot module hierarchy
    (don't hardcode tmp dir paths, use `tempfile` module)
- [ ] improvement
  - [ ] add function descriptions for those which lack it
  - [ ] add type annotation to all places in code
  - [ ] add decorator (or other mechanism) to log function start

### handlers:
- [ ] refactor
  - [ ] update type of the `context` argument to the new one
    (`telegram.ext.CallbackContext` -> `telegram.ext.ContextTypes.DEFAULT_TYPE`)
  - [ ] move check for edited messages to a decorator
- [ ] improvement
  - [ ] add decorator to check for command execution rights
  - [ ] guard anything coming from `Update` to ensure it is not None
#### command:
- [ ] refactor
  - [ ] join markov functions to be more compact
- [ ] improvement
    - [ ] check if file descriptors are closed correctly
#### text:
- [ ] refactor
  - [ ] split the big handler into smaller pieces
  - [ ] merge some conditions into more compact blocks of code
  - [ ] minor stuff

### utils:
#### log:
- [ ] review the file
#### schedule:
- [ ] refactor
  - [ ] general (explain?)
  - [ ] rewrite `_output_day`
#### markov:
- [ ] review the file
- [ ] refactor:
  - [ ] get rid of dicts, maybe make it into class
    (reasoning: access by strings is too much error-prone)
  - [ ] fix all incorrect try except blocks
  - [x] unify for auf and others
#### init:
- [ ] refactor:
  - [ ] merge some methods into one class
      (old note, review the file to confirm its relevance)
  - [ ] rewrite `_get_command_attrs` to be less error-prone
      (maybe with usage of configs)
  - [ ] move command extraction from `set_commands` to separate function
#### voice:
- [ ] review the file
#### diary:
- [ ] refactor: use `defaultdict` where applicable (ex: in `diary_write_one`)
- [ ] move argument validation to decorator
- [ ] refactor _check_date return
- [ ] turn if/else block into try/except where possible
#### image:
- [ ] refactor
  - [ ] rewrite `crawl` function
    - [ ] make match statement more compact
    - [ ] use wallhaven V1 API
  - [ ] redo `remove_file` using more than 1 brain cell
    (try implementing via custom `with` API with dunder methods)
  - [x] cut indents in `resize_image`
- [ ] improvement
  - [ ] explain magic numbers


## Backlog
Here will be finished todo's (maybe¿)


---
<sub><sup>If you use Windows all bugs are not our problem</sub></sup>
