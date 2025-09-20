#ifndef STRING_HPP
#define STRING_HPP

extern "C" {
#include "kernel/types.h"

//

#include "user/user.h"
}

#include "user/expected.hpp"
#include <stddef.h>

class String {
private:
  char *buffer;
  size_t length;

  String(char *memory, const size_t n) : buffer(memory), length(n) {}

public:
  static auto construct(const char *str) -> Expected<String, void> {
    const auto n = strlen(str);
    auto buffer = new char[n + 1];

    if (buffer == nullptr) {
      return {};
    }

    return String{buffer, n + 1};
  }

  static auto construct(const size_t n) -> Expected<String, void> {
    auto buffer = new char[n + 1];

    if (buffer == nullptr) {
      return {};
    }

    return String{buffer, n + 1};
  }

  static auto construct(const char *str, size_t n) -> Expected<String, void> {
    auto buffer = new char[n + 1];

    if (buffer == nullptr) {
      return {};
    }

    size_t i = 0;

    for (; i < n; ++i) {
      buffer[i] = str[i];
    }

    buffer[i] = 0;

    return String{buffer, n + 1};
  }

  String(const String &) = delete;

  String(String &&other) : buffer(other.buffer), length(other.length) {
    other.buffer = nullptr;
    other.length = 0;
  }

  auto operator=(const String &) -> void = delete;

  auto operator=(String &&other) noexcept -> String & {
    clear();

    buffer = other.buffer;
    length = other.length;

    other.buffer = nullptr;
    other.length = 0;

    return *this;
  }

  auto data() -> char * { return buffer; }

  auto data() const -> char * { return buffer; }

  auto capacity() const -> size_t { return length; }

  auto clear() -> void {
    delete[] buffer;
    buffer = nullptr;
    length = 0;
  }

  auto operator[](const size_t index) -> char & { return buffer[index]; }

  auto operator[](const size_t index) const -> const char & {
    return buffer[index];
  }
};

#endif /* STRING_HPP */
