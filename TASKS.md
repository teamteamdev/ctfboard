# Task layout

All tasks are stored in separate folders under `${TASKS_ROOT}` directory.

We required this task structure at Ugra CTF:

```
task-short-name
|- README.md
|- WRITEUP.md
|- DEPLOYMENT.md
|- config.yml
|- public/
   |- ...
|- private/
   |- ...
|- images/
```

For stable platform work, you need only `config.yml` and `public/` (optional, only if you need static files for participants).
 
Task is considered **well-formed** if its directory contains valid `config.yml`. If there is at least one directory which doesn't contain well-formed task, platform won't run (you'll see error 500).

> TODO: fix this behaviour

## public/

File `public/some.ext` for task with short name `example` will be available at url `https://ctf.domain/files/example/some.ext` in default configuration server.

## config.yml

Task description in YAML format.

Field | Required | Type | Description
---- | ------------ | ---- | -----------
`category` | **Yes** | `string` | We use `crypto`, `stegano`, `ppc`, `ctb`, `forensics`, `joy`, `web`, `reverse`, `admin`, `recon`, `pwn`, `misc`
`points` | **Yes** | `int` | It is divisible by 50 at our competitions
`short` | **Yes** | `string` | It is similar to folder name (*TODO: remove, it's unused*)
`name` | **Yes** | `string` | Full name
`author` | **Yes** | `string` | Authors' names
`description` | **Yes** | `string` | Full description as Markdown
`url` | No | `string` | Link to external content, if needed
`attachments` | No | `string[]` | Names of files in `public/` which are shown in the statement
`hints` | *Not implemented* | `Hint[]` | Hints — objects, each of them consists of two fields: `text` (`string`) и `cost` (`int`)
`flags` | **Yes** | `Flag[]` | All correct flags — either object with one field `text` (flag is this string, case-insensitive) or object with one field `regexp` (flag is any string which matches this regexp)

Config example:
```
#!yaml

category:   crypto
points:     50
short:      super
name:       "Super Hard Crypto"
author:     nsychev
description: >
  Первое задание будет, возможно, самым сложным для вас.
  Разгадать шифр нужно будет. Зашифрованный текст смотри по ссылке.
  Ещё зачем-то, кроме правильного ответа, заходит строка, удовлетворяющая
  regexp'у ugra_[ip]{2,4}._easy.
url:        https://ugractf.ru/static/flag.txt
attachments:
  - file1.txt
hints: 
  - 
    cost:   20
    text:   "Попробуй известные шифры, этот очень простой"
  - 
    cost:   30
    text:   "Гай Юлий ..."
flags:
  -
    text:   "ugra_hard_caesar_crypto"
  -
    regexp: "ugra_[ip]{2,4}._easy"
```
