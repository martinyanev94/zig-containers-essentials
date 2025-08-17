type UserProfile struct {
    ID      int    `json:"id"`
    Name    string `json:"name"`
    Email   string `json:"email"`
}

func main() {
    user := UserProfile{ID: 1, Name: "Alice", Email: "alice@example.com"}
    jsonBytes, _ := json.Marshal(user) // Convert to JSON
    fmt.Println(string(jsonBytes))
}
