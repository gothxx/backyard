package main
import "fmt"
func main() {
    a := []int{1,2,3} 
    fmt.Println(a)
    modifySlice(a)
    fmt.Println(a) 
    b := new(int)
    fmt.Println(b)  
    modify(b)     
    fmt.Println(b)
}

func modifySlice(data []int) {
    data = nil 
} 

func modify(a *int) {     
    a = nil 
} 

