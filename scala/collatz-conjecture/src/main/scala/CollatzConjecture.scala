object CollatzConjecture {
  def steps(
      starting_n: Int,
      steps_already: Int = 0
  ): Option[Int] = {
    starting_n match {
      case 1               => Some(steps_already)
      case x if x < 1      => None
      case x if x % 2 == 0 => steps(x / 2, steps_already + 1)
      case _               => steps(3 * starting_n + 1, steps_already + 1)
    }
  }
}
