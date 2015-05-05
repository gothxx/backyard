package main

import(
    "fmt"        
)
func main(){

str :="laoYu老虞"

    for  i:=0;i<len(str);i++ {
             fmt.Println(str[i])
    }

    for  i,s :=  range str {
            fmt.Println(i,"Unicode(",s,") string=",string(s))
    }

    r := []rune(str)
    fmt.Println("rune=",r)
    for i:=0;i<len(r) ; i++ {
           fmt.Println("r[",i,"]=",r[i],"string=",string(r[i]))
    }

}
