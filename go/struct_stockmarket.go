package main

import (
	"fmt"
	"math/rand"
	"time"
)

func randomNumberGen(min float32, max float32) float32 {
	return min + (max-min)*rand.Float32()
}

// Task implementation goes here
type Stock struct {
	name  string
	price float32
}

func (s *Stock) updateStock() {
	change := randomNumberGen(-10000, 10000)
	s.price = change
}

func displayMarket(market []Stock) {
	for _, m := range market {
		fmt.Println(m)
	}
}

func main() {
	rand.Seed(time.Now().UnixNano())
	// Function calls go here
	stockMarket := []Stock{{"GOOG", 2313.50}, {"AAPL", 157.28}, {"FB", 203.77}, {"TWTR", 50.00}}
	displayMarket(stockMarket)
	stockMarket[1].updateStock()
	displayMarket(stockMarket)
}
