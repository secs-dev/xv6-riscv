# Форк учебной ОС Xv6 для ITMO CSE

```mermaid
graph TD
    start["Начало"]

    subgraph setup ["Подготовка"]
        repo["<a href='/doc/setup/repo.md' style='color:black;'>Подготовка репозитория и порядок сдачи ЛР</a>"]
        setup_linux["<a href='/doc/setup/linux.md' style='color:black;'>Первый запуск ОС Xv6: Linux</a>"]
        vscode["<a href='/doc/dev/vscode.md' style='color:black;'>Настройка IDE: VSCode</a>"]
    end

    subgraph fs ["Файловая система"]
        shebang["<a href='/doc/lab/shebang.md' style='color:black;'>Shebang</a>"]
        symlink["<a href='/doc/lab/symlink.md' style='color:black;'>Symlink</a>"]
        ext["<a href='/doc/lab/ext.md' style='color:black;'>EXT</a>"]
    end

    subgraph net ["Сетевое взаимодействие"]
        nic["<a href='/doc/lab/nic.md' style='color:black;'>Драйвер NIC</a>"]
    end

    subgraph misc ["Прочее"]
        intro["<a href='/doc/lab/intro.md' style='color:black;'>Введение в Xv6</a>"]
        backtrace["<a href='/doc/lab/backtrace.md' style='color:black;'>Backtrace</a>"]
        halt["<a href='/doc/lab/halt.md' style='color:black;'>Halt</a>"]
    end

    subgraph mp ["Многозадачность"]
        mlfq["<a href='/doc/lab/mlfq.md' style='color:black;'>MLFQ Планировщик</a>"]
        allocproc["<a href='/doc/lab/allocproc.md' style='color:black;'>Список процессов</a>"]
        thread["<a href='/doc/lab/thread.md' style='color:black;'>Потоки</a>"]
        alarm["<a href='/doc/lab/alarm.md' style='color:black;'>Alarm</a>"]
    end

    subgraph mm ["Управление RAM"]
        filealloc["<a href='/doc/lab/filealloc.md' style='color:black;'>Аллокатор RAM</a>"]
        pteprint["<a href='/doc/lab/printpte.md' style='color:black;'>Печать таблицы страниц</a>"]
        shmem["<a href='/doc/lab/shmem.md' style='color:black;'>Shared Memory</a>"]
        cow["<a href='/doc/lab/cow.md' style='color:black;'>COW Fork</a>"]
        swap["<a href='/doc/lab/swap.md' style='color:black;'>Swapping</a>"]
        lazyalloc["<a href='/doc/lab/lazyalloc.md' style='color:black;'>Ленивая аллокация</a>"]
        hugepage["<a href='/doc/lab/hugepage.md' style='color:black;'>Большие страницы</a>"]
    end

    start --> repo
    repo --> setup_linux
    setup_linux --> vscode

    intro --> shebang
    intro --> symlink
    intro --> ext

    intro --> nic

    vscode --> intro
    intro --> backtrace
    intro --> halt

    filealloc --> mlfq
    filealloc --> allocproc
    shmem --> thread
    cow --> alarm

    intro --> filealloc
    intro --> pteprint
    pteprint --> shmem
    pteprint --> cow
    cow --> hugepage
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
    class ext hard

    class nic hard

    class thread,mlfq medium
    class alarm,allocproc hard

    class pteprint free
    class filealloc,cow,shmem medium
    class swap,lazyalloc,hugepage hard
```
