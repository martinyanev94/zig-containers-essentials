type Shape interface {
    Area() float64
}

type Circle struct {
    radius float64
}

type Rectangle struct {
    width, height float64
}

func (c Circle) Area() float64 {
    return 3.14 * c.radius * c.radius
}

func (r Rectangle) Area() float64 {
    return r.width * r.height
}

func main() {
    shapes := []Shape{
        Circle{radius: 5},
        Rectangle{width: 3, height: 4},
    }

    for _, shape := range shapes {
        fmt.Printf("Area: %f\n", shape.Area())
    }
}
