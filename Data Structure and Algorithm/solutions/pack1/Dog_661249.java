package solutions.pack1;

public class Dog_661249 {
    public Breed_661249 Name;
    int weight;

    public Dog_661249(Breed_661249 name, int weight) {
        Name = name;
        this.weight = weight;
    }

    public Breed_661249 getName() {
        return Name;
    }

    @Override
    public String toString() {
        return "Dog(" +
                "name=" + Name +
                ", weight=" + weight +
                ')';
    }
}

