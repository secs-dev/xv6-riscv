#include "user/expected.hpp"
#include "user/pipe.hpp"
#include "user/string.hpp"
#include <stddef.h>

auto writeString(Pipe &pipe, const char *str) -> int {
  auto length = strlen(str);

  if (auto code = pipe.write(&length, sizeof(length)); code == -1) {
    return code;
  }

  if (auto code = pipe.write(str, length); code == -1) {
    return code;
  }

  return 0;
}

auto readString(Pipe &pipe) -> Expected<String, void> {
  uint length;

  if (auto code = pipe.read(&length, sizeof(length)); code == -1) {
    return {};
  }

  auto str_construction_result = String::construct(length);

  if (!str_construction_result.has_value()) {
    return str_construction_result;
  }

  auto &str = str_construction_result.value();

  if (auto code = pipe.read(str.data(), length); code == -1) {
    return {};
  }

  str[length] = 0;

  return str_construction_result;
}

int main() {
  auto pipe_creation_result = Pipe::construct();

  if (!pipe_creation_result.has_value()) {
    printf("Failed to create pipe\n");
    return 1;
  }

  auto &pipe = pipe_creation_result.value();

  const auto fork_result = fork();

  if (fork_result == -1) {
    printf("Failed to create fork of the process\n");
    return 1;
  }

  if (fork_result == 0) {
    auto read_result = readString(pipe);

    if (read_result.has_value()) {
      printf("Received: %s\n", read_result.value().data());
    }
  } else {
    writeString(pipe, "Hello, from parent!");
  }

  return 0;
  // exit(0); // return works just fine 
}
