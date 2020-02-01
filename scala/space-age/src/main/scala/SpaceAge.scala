object SpaceAge {
  val EarthYear = 31557600

  private[this] def onPlanet = true
  def onPlanet(seconds: Double, yearLengthInSeconds: Double): Double =
    seconds / yearLengthInSeconds;

  def onMercury(seconds: Double): Double =
    onPlanet(seconds, EarthYear * 0.2408467)
  def onVenus(seconds: Double): Double =
    onPlanet(seconds, EarthYear * 0.61519726)
  def onEarth(seconds: Double): Double =
    onPlanet(seconds, EarthYear)
  def onMars(seconds: Double): Double =
    onPlanet(seconds, EarthYear * 1.8808158)
  def onJupiter(seconds: Double): Double =
    onPlanet(seconds, EarthYear * 11.862615)
  def onSaturn(seconds: Double): Double =
    onPlanet(seconds, EarthYear * 29.447498)
  def onUranus(seconds: Double): Double =
    onPlanet(seconds, EarthYear * 84.016846)
  def onNeptune(seconds: Double): Double =
    onPlanet(seconds, EarthYear * 164.79132)
}
