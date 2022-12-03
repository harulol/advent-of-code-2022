package main

import (
	// "bufio"
	"fmt"
	//  "io"
	"os"
	"strings"
)

func Sanitize(lines []string) {
	for i, line := range lines {
		lines[i] = strings.TrimSpace(line)
	}
}

func ReadData() []string {
	data, err := os.ReadFile("./input.txt")
	if err != nil {
		fmt.Println("Unreadable file :(")
		panic(err)
	}

	stringData := strings.Split(string(data), "\n")
	Sanitize(stringData)
	return stringData
}

func FindSameItem(line string) byte {
	half := len(line) / 2
	first, second := line[0:half], line[half:]
	set := make(map[byte]bool)
	CountChars(first, set)

	for i := 0; i < len(second); i++ {
		_, ok := set[second[i]]
		if ok {
			return second[i]
		}
	}

	fmt.Printf("%d - %d\n", len(first), len(second))

	return 0
}

func CountChars(s string, m map[byte]bool) {
	for i := 0; i < len(s); i++ {
		m[s[i]] = true
	}
}

func FindBadge(data []string) byte {
	map1, map2 := make(map[byte]bool), make(map[byte]bool)
	CountChars(data[0], map1)
	CountChars(data[1], map2)

	for i := 0; i < len(data[2]); i++ {
		s := data[2]
		_, ok1 := map1[s[i]]
		_, ok2 := map2[s[i]]

		if ok1 && ok2 {
			return s[i]
		}
	}

	return 0
}

func GetPriority(b byte) int {
	if b >= 'a' && b <= 'z' {
		return int(b) - 'a' + 1
	}

	if b >= 'A' && b <= 'Z' {
		return int(b) - 'A' + 27
	}

	return 0
}

func main() {
	stringData, count, badgeCount := ReadData(), 0, 0
	for i := 0; i < len(stringData); i += 3 {
		count += GetPriority(FindSameItem(stringData[i]))
		count += GetPriority(FindSameItem(stringData[i+1]))
		count += GetPriority(FindSameItem(stringData[i+2]))

		array := []string{stringData[i], stringData[i+1], stringData[i+2]}
		badgeCount += GetPriority(FindBadge(array))
	}

	fmt.Println(count)
	fmt.Println(badgeCount)
}
