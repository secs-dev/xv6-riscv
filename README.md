# Форк учебной ОС Xv6 для ITMO CSE

```mermaid
graph TD
    start["Начало"]

    subgraph setup ["Подготовка"]
        repo["<a href='/doc/setup/repo.md'>Подготовка репозитория и порядок сдачи ЛР</a>"]
        setup_linux["<a href='/doc/setup/linux.md'>Первый запуск ОС Xv6: Linux</a>"]
        vscode["<a href='/doc/dev/vscode.md'>Настройка IDE: VSCode</a>"]
    end

    subgraph fs ["Файловая система"]
        shebang["<a href='/doc/lab/shebang.md'>Shebang</a>"]
        symlink["<a href='/doc/lab/symlink.md'>Symlink</a>"]
    end

    subgraph misc ["Прочее"]
        intro["<a href='/doc/lab/intro.md'>Введение в Xv6</a>"]
        backtrace["<a href='/doc/lab/backtrace.md'>Backtrace</a>"]
        halt["<a href='/doc/lab/halt.md'>Halt</a>"]
    end

    subgraph mp ["Многозадачность"]
        allocproc["<a href='/doc/lab/allocproc.md'>Аллокатор RAM для структур процессов</a>"]
        thread["<a href='/doc/lab/thread.md'>Thread</a>"]
    end

    subgraph mm ["Управление RAM"]
        filealloc["<a href='/doc/lab/filealloc.md'>Аллокатор RAM</a>"]
        shmem["<a href='/doc/lab/shmem.md'>Shared Memory</a>"]
        cow["<a href='/doc/lab/cow.md'>Copy-on-write Fork</a>"]
        swap["<a href='/doc/lab/swap.md'>Swapping</a>"]
        lazyalloc["<a href='/doc/lab/lazyalloc.md'>Ленивая аллокация</a>"]
    end

    start --> repo
    repo --> setup_linux
    setup_linux --> vscode
    vscode --> intro

    intro --> shebang
    intro --> symlink
    intro --> backtrace
    intro --> halt

    intro --> filealloc
    filealloc --> allocproc
    filealloc --> shmem
    filealloc --> cow

    shmem --> thread

    cow --> lazyalloc
    cow --> swap

    classDef free fill:#eceff1,stroke:#607d8b,stroke-width:2px,color:#37474f
    classDef easy fill:#c8e6c9,stroke:#388e3c,stroke-width:2px,color:#1b5e20
    classDef medium fill:#fff9c4,stroke:#f9a825,stroke-width:2px,color:#f57f17
    classDef hard fill:#ffcdd2,stroke:#c62828,stroke-width:2px,color:#b71c1c

    class repo,setup_linux,vscode free

    class intro free
    class backtrace,halt easy

    class shebang,symlink medium

    class filealloc,shmem medium
    class cow,swap,lazyalloc hard

    class thread medium
    class allocproc hard
```
