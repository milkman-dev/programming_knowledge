// DB functions

func queryDatabase(query string) string {
	var result string
	connectDatabase()
	// Add deferred call to disconnectDatabase() here
	defer disconnectDatabase()

	if query == "SELECT * FROM coolTable;" {
		result = "NAME|DOB\nVincent Van Gogh|March 30, 1853"
	}
	fmt.Println(result)
	return result
}

func connectDatabase() {
	fmt.Println("Connecting to the database.")
}

func disconnectDatabase() {
	fmt.Println("Disconnecting from the database.")
}

func main() {
	queryDatabase("SELECT * FROM coolTable;")
}

// Spaceship functions

func fuelGauge(fuel int) {
	fmt.Println("You have", fuel, "gallons of fuel left")
}

func calculateFuel(planet string) int {
	var fuel int
	switch planet {
	case "Venus":
		fuel = 300000
	case "Mercury":
		fuel = 500000
	case "Mars":
		fuel = 700000
	default:
		fuel = 0
	}
	return fuel
}

func greetPlanet(planet string) {
	fmt.Println("You have arrived to", planet)
}

func cantFly() {
	fmt.Println("We do not have the available fuel to fly there.")
}

func flyToPlanet(planet string, fuel int) int {
	var fuelRemaining, fuelCost int
	fuelRemaining = fuel
	fuelCost = calculateFuel(planet)
	if fuelRemaining >= fuelCost {
		greetPlanet(planet)
		fuelRemaining = fuelRemaining - fuelCost
	} else {
		cantFly()
	}
	return fuelRemaining
}

func main() {
	var fuel int
	var planetChoice string
	fuel = 1000000
	planetChoice = "Venus"

	fuel = flyToPlanet(planetChoice, fuel)
	fuelGauge(fuel)

}