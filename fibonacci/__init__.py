# Copyright (C) 2018 YangBy <yby@yangby.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Functions to find the fibonacci number by a given index."""

import resource
import sys
from typing import NewType
from typing import Iterator, Tuple

__all__ = ['Natural', 'fibonacci', 'fibonacci_tr']

Natural = NewType('Natural', int)


def fibonacci_generate_generator():
    """Generate a generator for the fibonacci sequence."""
    index, val1, val2 = 0, 0, 1
    while True:
        yield val1
        val1, val2 = val2, val1 + val2
        index = index + 1


def fibonacci(index: Natural) -> Iterator[Natural]:
    """Find the fibonacci number by a given index (generator)."""
    if index < 0:
        raise ValueError(
            f'Only Natural Numbers are allowed, but input is {index}.')
    fibonacci_generator = fibonacci_generate_generator()
    for _ in range(index):
        next(fibonacci_generator)
    return next(fibonacci_generator)


def fibonacci_tail_recursion(index: Natural, val1: Natural, val2: Natural
                             ) -> Tuple[Natural, Natural, Natural]:
    """Traverse through the fibonacci sequence (tail-recursion)."""
    if index == 0:
        return (0, val1, val2)
    return fibonacci_tail_recursion(index - 1, val2, val1 + val2)


def fibonacci_tr(index: Natural) -> Iterator[Natural]:
    """Find the fibonacci number by a given index (tail-recursion)."""
    if index < 0:
        raise ValueError(
            f'Only Natural Numbers are allowed, but input is {index}.')
    (rlimit_old, rclimit_old) = set_limits(
        [0x10000000, resource.RLIM_INFINITY],
        0x10000000,
    )
    (_, val, _) = fibonacci_tail_recursion(index, 0, 1)
    set_limits(rlimit_old, rclimit_old)
    return val


def set_limits(rlimit_new, rclimit_new):
    """Modify the system limits."""
    rlimit_old = resource.getrlimit(resource.RLIMIT_STACK)
    rclimit_old = sys.getrecursionlimit()
    resource.setrlimit(resource.RLIMIT_STACK, rlimit_new)
    sys.setrecursionlimit(rclimit_new)
    return (rlimit_old, rclimit_old)
