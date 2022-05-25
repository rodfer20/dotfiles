package main

import (
	"fmt"

	"golang.org/x/exp/constraints"
)

func Sum[T constraints.Float | constraints.Integer](r ... T) T{
	var s T
	for _, v := range r {
		s += v
	}
	return s
}

func main() {
	fmt.Println(Sum(1,2,3,4))
	fmt.Println(Sum(1.1,2.2,3.3,4.4))
}
