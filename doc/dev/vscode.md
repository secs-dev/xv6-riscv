# Настройка IDE: VSCode

В данном приложении, мы настроим IDE [VSCode][6] для разработки ОС `Xv6`.

## Шаг 1. Установка clangd

`Xv6` написана на `C`, так что для получения функций IDE рекомендуем воспользоваться языковым сервером [clangd][1]. Ищите его в используемом вами пакетном менеджере, либо следуйте [инструкцям от разработчиков][2].

## Шаг 2. Установка плагина clangd

Теперь установите [плагин clangd][3] для [VSCode][6]. Если вы не установили [clangd][1] на предыдущем шаге, плагин при запуске предложит скачать последнюю версию.

## Шаг 3. Получение базы данных компиляции

База данных компиляции (compilation database) необходима для работы анализаторов кода от `llvm` и представляется файлом `compile_commands.json`. Поскольку `Xv6` собирается при помощи `Make`. Предлагается получить эти данные с помощью утилиты [Bear][4]. Установить ее можно с помощью [вашего пакетного менеджера][5].

После установки соберите проект "под bear".

```bash
# cd xv6-riscv
make clean
bear -- make qemu
```

Вы должны заметить появившийся в корне репозитория файл `compile_commands.json`. Теперь [clangd][1] должен работать исправно (иначе попробуйте перезагрузить окно (reload window) [VSCode][6]).

[1]: https://clangd.llvm.org/
[2]: https://clangd.llvm.org/installation
[3]: https://marketplace.visualstudio.com/items?itemName=llvm-vs-code-extensions.vscode-clangd
[4]: https://github.com/rizsotto/Bear
[5]: https://repology.org/project/bear-clang/versions
[6]: https://code.visualstudio.com/
