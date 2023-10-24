package main

import (
	"fmt"
	"math/rand"
	"time"
)

func getRandomElement(arraySlice []string) string {
	slicelen := len(arraySlice)
	ranVal := rand.Intn(slicelen)
	return arraySlice[ranVal]
}

func main() {

	guestList := [...]string{"Logan", "Mario", "Luigi", "Wario", "Yoshi", "Toad"}
	catStorage := [...]string{"Basket", "Box", "Crate", "Dog house"}

	rand.Seed(time.Now().UnixNano())
	gameGuest := getRandomElement(guestList[:])
	gameObject := getRandomElement(catStorage[:])

	fmt.Println("It appears that", gameGuest, "hid your cat in a", gameObject, "lol wtf")
}
