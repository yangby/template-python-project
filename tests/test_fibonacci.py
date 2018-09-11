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
"""Tests for fibonacci functions."""

import pytest
from hypothesis import given, strategies as st, settings

from fibonacci import fibonacci, fibonacci_tr


def test_fibonacci():
    """Test the fibonacci function (generator version)."""
    with pytest.raises(ValueError):
        fibonacci(-1)
    assert fibonacci(0) == 0
    assert fibonacci(8) == 21
    assert fibonacci(64) == 10610209857723
    # pylint: disable=line-too-long
    assert fibonacci(
        4096
    ) == 4612001732280431247456445708563614127173224997617390534215059226137357133453956236072775985077061637311848907129417864574275423997101439882308358166652317363373656716074141072814493065517475413688262677419077617088948496309673353922704120725679705669386361748442871720790233981292904246541321855474289727005675146240418903692583131115962989146454578739972233255840007113102596686397958930124518885822059783685448190039658062872691964066428723178769322339485834664335313247796472730324095846596733944704930052412653763777113749102514483039561246866695780115646150369678333299122486379683222039167477498691611996122878629556831081616202064636498715093853352203252703786287926199052408354498825123496861419106453928530148716831934981264321286848387438601077819789292236505514653845305057927646386419899455438488952785050077521931600327064840520442470066917947


def test_fibonacci_tr():
    """Test the fibonacci function (tail-recursion version)."""
    with pytest.raises(ValueError):
        fibonacci_tr(-1)
    assert fibonacci_tr(0) == 0
    assert fibonacci_tr(8) == 21
    assert fibonacci_tr(64) == 10610209857723
    # pylint: disable=line-too-long
    assert fibonacci_tr(
        4096
    ) == 4612001732280431247456445708563614127173224997617390534215059226137357133453956236072775985077061637311848907129417864574275423997101439882308358166652317363373656716074141072814493065517475413688262677419077617088948496309673353922704120725679705669386361748442871720790233981292904246541321855474289727005675146240418903692583131115962989146454578739972233255840007113102596686397958930124518885822059783685448190039658062872691964066428723178769322339485834664335313247796472730324095846596733944704930052412653763777113749102514483039561246866695780115646150369678333299122486379683222039167477498691611996122878629556831081616202064636498715093853352203252703786287926199052408354498825123496861419106453928530148716831934981264321286848387438601077819789292236505514653845305057927646386419899455438488952785050077521931600327064840520442470066917947


@given(st.integers(min_value=2, max_value=65535))
@settings(max_examples=64, deadline=30000)
def test_fibonacci_randomize(index: int):
    """Property-based test for the fibonacci function (generator version)."""
    assert fibonacci(index) == fibonacci(index - 1) + fibonacci(index - 2)


@given(st.integers(min_value=2, max_value=65535))
@settings(max_examples=64, deadline=30000)
def test_fibonacci_tr_randomize(index: int):
    """Property-based test for the fibonacci function (tail-recursion version)."""
    assert fibonacci_tr(
        index) == fibonacci_tr(index - 1) + fibonacci_tr(index - 2)


@given(st.integers(min_value=0, max_value=65535))
@settings(max_examples=64, deadline=30000)
def test_equivalence(index: int):
    """Test if both fibonacci functions returns same values."""
    assert fibonacci(index) == fibonacci_tr(index)
