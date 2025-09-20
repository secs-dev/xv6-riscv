#ifndef PIPE_HPP
#define PIPE_HPP

extern "C" {
#include "kernel/types.h"

//

#include "user/user.h"
}

#include "user/expected.hpp"

class Pipe {
private:
  int readDescriptor{};
  int writeDescriptor{};

  Pipe(int rd, int wd) : readDescriptor(rd), writeDescriptor(wd) {}

public:
  static auto construct() -> Expected<Pipe, int> {
    int descriptors[2];

    if (int code = pipe(descriptors); code != 0) {
      return code;
    }

    return Pipe(descriptors[0], descriptors[1]);
  }

  auto read(void *buffer, int length) -> int {
    return ::read(readDescriptor, buffer, length);
  }

  auto write(const void *buffer, int length) -> int {
    return ::write(writeDescriptor, buffer, length);
  }
};

#endif /* PIPE_HPP */