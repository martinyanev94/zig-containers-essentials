type Author struct {
    name      string
    birthYear int
}

type Publisher struct {
    name    string
    address string
}

type Book struct {
    title    string
    author   Author
    publisher Publisher
}

func main() {
    author := Author{name: "George Orwell", birthYear: 1903}
    publisher := Publisher{name: "Harvill Secker", address: "London"}
    
    book := Book{
        title:    "1984",
        author:   author,
        publisher: publisher,
    }

    fmt.Println(book)
}
