import scala.collection.mutable.{Map, SortedMap}

class School {
  type DB = Map[Int, Seq[String]]

  private var _db: DB = Map()

  def add(name: String, g: Int) = {
    if (_db contains g) _db(g) = _db(g) :+ name
    else _db += (g -> Seq(name))
  }

  def db: DB = _db

  def grade(g: Int): Seq[String] =
    _db.getOrElse(g, Seq())

  def sorted: DB = SortedMap(_db.toSeq: _*) map { case (k, v) => k -> v.sorted }
}
