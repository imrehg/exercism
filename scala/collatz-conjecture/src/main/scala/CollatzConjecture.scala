import scala.annotation.tailrec

object CollatzConjecture {
  def steps(
      starting_n: Int
  ): Option[Int] = {
    @tailrec def iter(n: Int, steps: Int): Int = {
      n match {
        case 1               => steps
        case x if x % 2 == 0 => iter(x / 2, steps + 1)
        case _               => iter(3 * n + 1, steps + 1)
      }
    }

    if (starting_n > 0) Some(iter(starting_n, 0))
    else None
  }
}
