#ifndef EXPECTED_HPP
#define EXPECTED_HPP

#include "user/new.hpp"

template <typename V, typename E> class Expected;

template <typename V> class Expected<V, void> {
  union {
    V val;
    bool dummy;
  };

  bool success;

public:
  Expected() : dummy{false}, success{false} {}

  Expected(const V &v) : val{v}, success{true} {}

  Expected(V &&v) : val{static_cast<V &&>(v)}, success{true} {}

  Expected(const Expected &other) : success(other.success) {
    if (success) {
      ::new (&val) V(other.val);
    }
  }

  Expected(Expected &&other) : success(other.success) {
    if (success) {
      ::new (&val) V(static_cast<V &&>(other.val));
    }
  }

  auto has_value() const -> bool { return success; }

  auto value() -> V & { return val; }

  auto value() const -> const V & { return val; }

  auto error() -> void {}

  auto error() const -> void {}
};

template <typename V, typename E> class Expected {
private:
  union {
    V val;
    E unexp;
  };

  bool success;

public:
  Expected(const V &v) : val{v}, success{true} {}

  Expected(V &&v) : val{static_cast<V &&>(v)}, success{true} {}

  Expected(const E &e) : unexp{e}, success{false} {}

  Expected(E &&e) : unexp{static_cast<E &&>(e)}, success{false} {}

  Expected(const Expected &other) : success(other.success) {
    if (success) {
      ::new (&val) V(other.val);
    } else {
      ::new (&unexp) E(other.unexp);
    }
  }

  Expected(Expected &&other) : success(other.success) {
    if (success) {
      ::new (&val) V(static_cast<V &&>(other.val));
    } else {
      ::new (&unexp) E(static_cast<E &&>(other.unexp));
    }
  }

  auto has_value() const -> bool { return success; }

  auto value() -> V & { return val; }

  auto value() const -> const V & { return val; }

  auto error() -> E & { return unexp; }

  auto error() const -> const E & { return unexp; }
};

#endif /* EXPECTED_HPP */