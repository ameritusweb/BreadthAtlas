# Frontier — landmarks used so far (lockers-skip-first)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | Locker n is toggled once per divisor other than 1, so the toggle count is one less than the divisor count. | route 001 | VALID |
| 2 | Divisors pair up as d with n/d, so only perfect squares have an odd number of divisors. | route 001 | VALID |
| 3 | Dropping student 1 flips the parity, so the open lockers are the non-squares and the squares stay closed. | route 001 | VALID |
| 4 | There are ten perfect squares up to 100, so the rest are open. | route 001 | VALID |
| 5 | Student 1 would toggle every locker exactly once, so our final state is the exact opposite of the familiar game's final state. | attempt 001 | DUPLICATE |
| 6 | A locker is open in our game exactly when it is closed in the familiar game, so the open set is the complement of the familiar open set. | attempt 001 | DUPLICATE |
| 7 | The familiar game leaves only the ten perfect squares open, so the complement is all the other lockers. | attempt 001 | DUPLICATE |
| 8 | Locker n is toggled once by its own student, and every other toggler is a divisor strictly between 1 and n. | attempt 002 | DUPLICATE |
| 9 | Those in-between divisors pair off, so non-squares have an even number of them and squares have an odd number, which makes the total toggles odd exactly for non-squares. | attempt 002 | DUPLICATE |
| 10 | Locker 1 is never toggled, so it stays closed along with the other nine squares. | attempt 002 | DUPLICATE |
| 11 | A number's divisor count is the product of one-more-than-each-prime-exponent, so it is odd exactly when every exponent is even. | route 002 | VALID |
| 12 | Every exponent being even means the number is a perfect square, so only squares have an odd divisor count. | route 002 | VALID |
| 13 | With student 1 absent the toggle count is the divisor count minus one, so the open lockers are exactly the non-squares. | route 002 | VALID |
