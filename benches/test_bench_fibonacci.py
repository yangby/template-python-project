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
"""Benchmark fibonacci functions."""

import pytest

from fibonacci import fibonacci, fibonacci_tr

BENCHES_GROUP = 'fibonacci_benches'


@pytest.mark.benchmark(group=BENCHES_GROUP)
def test_fibonacci(benchmark):
    """Benchmark the fibonacci function (generator version)."""
    assert benchmark(fibonacci, 4096) == fibonacci(4096)


@pytest.mark.benchmark(group=BENCHES_GROUP)
def test_fibonacci_tr(benchmark):
    """Benchmark the fibonacci function (tail-recursion version)."""
    assert benchmark(fibonacci_tr, 4096) == fibonacci_tr(4096)
