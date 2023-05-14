## FAQ:
- Any general, organizational or backend question - contact Mrestof
- Якщо щось з кодом - писати Паші
- Если что-то сломалось - писать Дане
- Если комменты вас пугают - писать Эду


## Features

### frontend:
Pavlo and Oleg describe the user end features you implemented and the ones you
plan to implement

### backend:
- [ ] logging support
- [ ] code formatter (probably black)
- [ ] pythonic configs
  - [ ] create the config system with default python objects
  - [ ] put all constants there
- [ ] tests


## TODO

### global:
- [ ] discuss the usefulness of "general refactor" todo's and notes
- [ ] refactor
  - [ ] change variable names to make more sense
  - [ ] expand unreadable oneliners
  - [ ] replace OS calls with python alternatives
- [ ] improvement
  - [ ] add function descriptions for those which lack it
  - [ ] add type annotation to all places in code

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
  - [ ] fix hentai function
  - [ ] join markov functions to be more compact
- [ ] improvement
    - [ ] check if file descriptors are closed correctly
#### text:
- [ ] refactor
  - [ ] one big refactor
  - [ ] split the big handler into smaller pieces
  - [ ] merge some conditions into more compact blocks of code

### utils:
#### log:
- [ ] review the file
#### schedule:
- [ ] refactor
  - [ ] general (explain?)
  - [ ] rewrite `_output_day`
#### markov:
- [ ] refactor:
  - [ ] general
  - [ ] get rid of dicts, maybe make it into class
    (reasoning: access by strings is too much error prone)
  - [x] unify for auf and others
#### init:
- [ ] refactor:
  - [ ] merge some methods into one class
      (old note, review the file to confirm its relevance)
  - [ ] rewrite `_get_command_attrs` to be less error prone
      (maybe with usage of configs)
  - [ ] move command extraction from `set_commands` to separate function
#### voice:
- [ ] review the file
#### diary:
- [ ] refactor: use `defaultdict` where applicable (ex: in `diary_write_one`)
#### image:
- [ ] refactor
  - [ ] rewrite `crawl` function (make match statement more compact)
  - [ ] redo `remove_file` using more than 1 brain cell
    (try implementing via custom `with` API)
  - [x] cut indents in `resize_image`
- [ ] improvement
  - [ ] explain magic numbers


## Backlog
Here will be finished todo's (maybe¿)


---
<sub><sup>If you use Windows all bugs are not our problem</sub></sup>
