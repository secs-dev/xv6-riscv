# Первый запуск ОС Xv6

В данном приложении мы расскажем вам, как проще всего запустить ОС `Xv6` на вашем компьютере под управлением ОС Linux.

## Шаг 1. Установка Docker

Для работы мы рекомендуем вам использовать [Docker][1], установите его себе на компьютер по [инструкции от разработчиков][2].

## Шаг 2. Запуск образа для работы с Xv6

Мы подготовили `Docker` образ для работы с `Xv6`. Там установлено все необходимое: вирутальная машина `qemu`, комплиятор `GCC` под `RISC-V`, `make` для автоматизации сборки проекта и прочие мелочи.

Скачать его можно с DockerHub: [vityamand/xv6][3].

```bash
docker pull vityamand/xv6
```

Также мы можете собрать образ самостоятельно.

```bash
./ci/docker/build.sh
```

Теперь попробуйте запустить его.

```bash
./ci/docker/run.sh
```

Вы должны оказаться в корневой директории контейнера.

## Шаг 3. Сборка и запуск ОС Xv6

В контейнер примонтирована директория с проектом. Перейдите в нее.

```bash
cd xv6
```

Попробуйте собрать `Xv6`.

```bash
make
```

И, наконец, запустите.

```bash
make qemu
```

Вы готовы к работе. Удачи!

[1]: https://www.docker.com/
[2]: https://docs.docker.com/engine/install/
[3]: https://hub.docker.com/repository/docker/vityamand/xv6/general
