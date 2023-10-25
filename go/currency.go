package main

import (
	"fmt"
)

func main() {
	currencies := map[string]float32{
		"JPY": 130.2,
		"EUR": 0.95,
		"MXN": 17.50,
	}
	var dollarAmount float32
	var currency string

	fmt.Println("Please input the amount:")
	fmt.Scan(&dollarAmount)

	if dollarAmount == 0 {
		fmt.Println("Please input a valid amount in USD")
	} else {
		fmt.Println("What currency you want?")
		fmt.Scan(&currency)

		rate, isValid := currencies[currency]
		if isValid {
			rate *= dollarAmount
			fmt.Println(rate)
		} else {
			fmt.Println("Not a valid currency")
		}
	}
}
