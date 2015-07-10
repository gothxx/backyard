package main

import "fmt"

func main(){

    str :="laoYu老虞"
    str2 :="laoYu"
    fmt.Println("len(",str,")=",len(str))      //len=11=5+6,一个汉字在UTF-8>中占3个字节
    fmt.Println("len(",str2,")=",len(str2))    //len=5
    fmt.Println("str[0]=",str[0])              //l

    tt()

    abc()
}
func tt(){

    str :="str"
    arr :=[5]int{1,2,3}
    slice :=make([]int,5)

    m :=make(map[int] string)
    m[2]="len"

    ch :=make(chan int)

    fmt.Println("len(string)=",len(str))   //3
    fmt.Println("len(array)=",len(arr))     //5invalid argument user (type *UserInfo) for len

    fmt.Println("len(slice)=",len(slice))   //5
    fmt.Println("len(map)=",len(m))         //1
    fmt.Println("len(chat)=",len(ch))       //0

    //user :=&UserInfo{id:1,name:"laoYu"}
    //interger :=2
    //fmt.Println("len(my struct)=",len(user))//invalid argument user (type *UserInfo) for len
    //fmt.Println("len(interger)=",len(interger))
}
func abc(){

    var str2 string
    var arr2  [5]int
    var slice2  []int
    var  m2 map[int] string
    var  ch2 chan int

    fmt.Println("len(string)=",len(str2))    //0
    fmt.Println("len(array)=",len(arr2))     //5 
    fmt.Println("len(slice)=",len(slice2))   //0
    fmt.Println("len(map)=",len(m2))         //0
    fmt.Println("len(chat)=",len(ch2))       //0
}
